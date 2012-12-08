%define ttf2pt1ver 3.4.4

Summary:	Some utilities for use by drakfont
Name:		font-tools
Version:	0.1
Release:	%mkrel 24
License:	GPLv2+ and BSD
Group:		System/Configuration/Other
URL: 		http://www.mandriva.com
Source:		%{name}-%{version}.tar.bz2
Source1:	http://download.sourceforge.net/ttf2pt1/ttf2pt1-%{ttf2pt1ver}.tgz
BuildRequires:	freetype-devel = 1.3.1
Requires:	t1utils
Requires:	ttmkfdir
Requires:	groff
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

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
perl -pi -e 's/ttf2pt1-3.3.5/ttf2pt1-%{ttf2pt1ver}/g' Makefile
make CC="gcc %{optflags}"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_sbindir},%{_mandir}/man1}

%makeinstall PREFIX=%{buildroot}/usr

install ttf2pt1-%{ttf2pt1ver}/ttf2pt1.1 %{buildroot}%{_mandir}/man1
install ttf2pt1-%{ttf2pt1ver}/ttf2pt1 %{buildroot}%{_sbindir}
install type1inst-0.6.1/type1inst.man %{buildroot}%{_mandir}/man1/type1inst.1

rm -f %{buildroot}%{_sbindir}/t1asm

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README README.ttf2pt1 COPYRIGHT.ttf2pt1
%attr(0755,root,root) %{_sbindir}/*
%{_mandir}/man1/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-22mdv2011.0
+ Revision: 664316
- mass rebuild

* Mon Sep 27 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-21mdv2011.0
+ Revision: 581220
- ttf2pt1 3.4.4
- fix deps

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-20mdv2010.1
+ Revision: 520109
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-19mdv2010.0
+ Revision: 424458
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.1-18mdv2009.1
+ Revision: 351154
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-17mdv2009.0
+ Revision: 220960
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.1-16mdv2008.1
+ Revision: 150078
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.1-15mdv2008.0
+ Revision: 91066
- rebuild for 2008
- new license policy


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1-14mdv2007.0
+ Revision: 119955
- Import font-tools

* Mon May 15 2006 Stefan van der Eijk <stefan@eijk.nu> 0.1-13mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.1-12mdk
- Rebuild

* Fri Feb 11 2005 Nicolas Lécureuil <neoclust@mandrakesoft.com> 0.1-11mdk
- Fix Require 
- Fix #5964

