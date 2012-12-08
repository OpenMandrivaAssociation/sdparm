Summary:	List or change SCSI disk parameters
Name:		sdparm
Version:	1.06
Release:	%mkrel 3
License:	BSD
Group:		System/Kernel and hardware
URL:		http://sg.danny.cz/sg/sdparm.html 
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use
the SCSI command set) such as CD/DVD and tape drives may also find
parts of sdparm useful. Requires the linux kernel 2.4 series or later.
In the 2.4 series SCSI generic device names (e.g. /dev/sg0)
must be used. In the 2.6 series other device names may be used as
well (e.g. /dev/sda).

Warning: It is possible (but unlikely) to change SCSI disk settings
that stop or slow it down. Use with care.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README CREDITS AUTHORS COPYING
%{_bindir}/*
%{_mandir}/man*/*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.06-2mdv2011.0
+ Revision: 669966
- mass rebuild

* Tue Nov 30 2010 Thierry Vignaud <tv@mandriva.org> 1.06-1mdv2011.0
+ Revision: 603553
- new release

* Sun Apr 25 2010 Emmanuel Andry <eandry@mandriva.org> 1.05-1mdv2010.1
+ Revision: 538710
- New version 1.0.5

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.04-1mdv2010.1
+ Revision: 508805
- update to new version 1.04
- update urls

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.03-3mdv2010.0
+ Revision: 427066
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03-2mdv2009.1
+ Revision: 317143
- rebuild

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 1.03-1mdv2009.0
+ Revision: 229951
- New version 1.03

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.02-2mdv2009.0
+ Revision: 225432
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.02-1mdv2008.1
+ Revision: 179500
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-0.2mdv2008.0
+ Revision: 90264
- rebuild

* Tue Jun 12 2007 Erwan Velu <erwan@mandriva.org> 1.02-0.1mdv2008.0
+ Revision: 38116
- 1.02beta

* Mon Apr 23 2007 Erwan Velu <erwan@mandriva.org> 1.01-2mdv2008.0
+ Revision: 17619
- Release 1.01


* Tue Jan 23 2007 Erwan Velu <erwan@mandriva.org> 1.01-1mdv2007.0
+ Revision: 112464
- 1.01
- Import sdparm

* Tue Jul 25 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.99-1mdv2007.0
- new release

* Sat May 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.98-1mdk
- new release

* Wed Feb 22 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.97-1mdk
- final release

* Wed Dec 28 2005 Erwan Velu <erwan@seanodes.com> 0.97-0.1mdk
- 0.97 beta

* Wed Aug 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.94-1mdk
- 0.94
- %%mkrel
- wipe out buildroot at the beginning of %%install
- drop 'INSTALL' doc, no use for it

* Sat Jun 18 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.93-1mdk
- new release

* Tue May 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.91-2mdk
- fix typo in description (pixel) (also fixed upstream in 0.91's README)

* Fri May 20 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.91-1mdk
- new release

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.90-1mdk
- initial release

