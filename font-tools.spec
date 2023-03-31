%define ttf2pt1ver 3.4.4

Summary:	Some utilities for use by drakfont
Name:		font-tools
Version:	0.1
Release:	35
License:	GPLv2+ and BSD
Group:		System/Configuration/Other
Url: 		http://www.mandriva.com
Source0:	%{name}-%{version}.tar.bz2
Source1:	http://download.sourceforge.net/ttf2pt1/ttf2pt1-%{ttf2pt1ver}.tgz
BuildRequires:	freetype-devel
Requires:	t1utils
Requires:	ttmkfdir
Requires:	groff

%description
font-tools is used by drakfont and includes:
- ttf2type1: convert .ttf to .pfb and .afm.
- tt2afm:    convert .ttf to .afm.
- pfm2afm:   convert .pfm to afm.

%prep
%setup -q -a1

%build
# ttf2pt1 3.3.5 from main sources had IA-32 objects
make clean
sed -i -e 's/ttf2pt1-3.3.5/ttf2pt1-%{ttf2pt1ver}/g' Makefile
make CC="gcc %{optflags}"

%install
mkdir -p %{buildroot}{%{_sbindir},%{_mandir}/man1}
%makeinstall PREFIX=%{buildroot}/usr

install ttf2pt1-%{ttf2pt1ver}/ttf2pt1.1 %{buildroot}%{_mandir}/man1
install ttf2pt1-%{ttf2pt1ver}/ttf2pt1 %{buildroot}%{_sbindir}
install type1inst-0.6.1/type1inst.man %{buildroot}%{_mandir}/man1/type1inst.1

rm -f %{buildroot}%{_sbindir}/t1asm

%files
%doc README README.ttf2pt1 COPYRIGHT.ttf2pt1
%{_sbindir}/*
%{_mandir}/man1/*

