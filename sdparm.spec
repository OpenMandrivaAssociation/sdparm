Summary:	List or change SCSI disk parameters
Name:		sdparm
Version:	1.02
Release:	%mkrel 2
License:	BSD
Group:		System/Kernel and hardware
URL:		http://www.torque.net/sg/sdparm.html
Source0:	http://www.torque.net/sg/p/%{name}-%{version}.tar.bz2
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
%configure

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README CREDITS AUTHORS COPYING
%{_bindir}/*
%{_mandir}/man*/*


