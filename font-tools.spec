%define ttf2pt1ver	3.4.3

Summary:	Some utilities for use by drakfont
Name:		font-tools
Version:	0.1
Release:	%mkrel 14
License:	GPL & BSD
Group:		System/Configuration/Other
Url: 		http://www.linux-mandrake.com
Source:		%{name}-%{version}.tar.bz2
Source1:	http://download.sourceforge.net/ttf2pt1/ttf2pt1-%{ttf2pt1ver}.tar.bz2
BuildRequires:	freetype-devel
Requires:	t1utils, freetype-tools, groff
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
font-tools is used by drakfont and include:
- ttf2type1: convert .ttf to .pfb and .afm.
- tt2afm:    convert .ttf to .afm .
- pfm2afm:   convert .pfm to afm.

%prep
%setup -q -a 1

%build
# ttf2pt1 3.3.5 from main sources had IA-32 objects
make clean
perl -pi -e 's/ttf2pt1-3.3.5/ttf2pt1-%{ttf2pt1ver}/g' Makefile
make CC="gcc %{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_sbindir},%{_mandir}/man1}

%makeinstall PREFIX=%{buildroot}/usr
install ttf2pt1-%{ttf2pt1ver}/ttf2pt1.1 %{buildroot}%{_mandir}/man1
install ./ttf2pt1-%{ttf2pt1ver}/ttf2pt1 %{buildroot}%{_sbindir}
install type1inst-0.6.1/type1inst.man %{buildroot}%{_mandir}/man1/type1inst.1

rm -f %{buildroot}%{_sbindir}/t1asm

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README COPYING README.ttf2pt1 COPYRIGHT.ttf2pt1
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*


