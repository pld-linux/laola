Summary:	A set of tools to extract data from MS-Word .doc files
Summary(pl):	Zestaw narzêdzi s³u¿±cych do obs³ugi plików zapisanych w formacie MS-Word
Name:		laola
Version:	013
Release:	2
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
URL:		http://www.cs.tu-berlin.de/~schwartz/pmh/laola.html
Source0:	http://www.cs.tu-berlin.de/~schwartz/pmh/%{name}%{version}.zip
Patch0:		%{name}-install.patch
Patch1:		%{name}-include.patch
Requires:	perl >= 4
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_unzipbin	/usr/bin/unzip -o -d %{name}-%{version}

%description
laola is a set of perl-based tools and libraries, able to
extract/modify data in MS-Word .doc files. Can work with MS-Word 6.0,
7.0 files, and in a limited range with MS-W 8.0.

%description -l pl
laola to zestaw narzêdzi i bibliotek, napisanych w perlu, które
umo¿liwiaj± wydobycie oraz modyfikacjê danych zawartych w plikach .doc
MS-Worda. Umo¿liwia pracê z plikami MS-Word 6.0, 7.0, oraz (w
ograniczonym zakresie) 8.0

%prep
%setup -q
%patch0
%patch1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
perl install -g

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/laola
%doc README.gz announce *.html
%doc elser/*.html
%doc elser/word6/*.html
