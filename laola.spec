Summary: a set of tools to extract data from MS-Word .doc files
Summary(pl): zestaw narzêdzi s³u¿±cych do obs³ugi plików zapisanych w formacie MS-Word
Name: laola
Version: 013
Release: 1
Group: Applications/Text
Group(pl): Aplikacje/Tekst
Copyright: GPL
Vendor: PLD
Distribution: PLD
URL: http://www.cs.tu-berlin.de/~schwartz/pmh/laola.html
Source: http://www.cs.tu-berlin.de/~schwartz/pmh/%{name}%{version}.zip
Patch0: %{name}-install.patch
Patch1: %{name}-include.patch
Requires: perl >= 4
BuildArch: noarch
BuildRoot: /tmp/%{name}-%{version}-root

%description
laola is a set of perl-based tools and libraries, able to extract/modify data in MS-Word .doc files. Can work with MS-Word 6.0, 7.0 files, and in a limited range with MS-W 8.0. 

%description -l pl
laola to zestaw narzêdzi i bibliotek, napisanych w perlu, które umo¿liwiaj± wydobycie oraz modyfikacjê danych zawartych w plikach .doc MS-Worda. Umo¿liwia pracê z plikami MS-Word 6.0, 7.0, oraz (w ograniczonym zakresie) 8.0

%prep
%setup -T -c
unzip -q $RPM_SOURCE_DIR/%{name}%{version}.zip
%patch0
%patch1

%build
# no build needed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib}
/usr/bin/perl install -g

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
/usr/lib/laola/
%doc README announce *.html
%doc elser/*.html
%doc elser/word6/*.html

%changelog
* Fri Aug 9 1999 Sebastian Zagrodzki
- initial rpm release
- supress all install questions
- don't install docs in libraries directory
- search for .pl files in /usr/lib/laola
