Summary: PCAP SIP Dump tool
Name: pcapsipdump
Version: 0.1.4
Release: 1
License: GPL v2
Group: System/Servers
BuildRoot: /var/tmp/%{name}-%{version}
Source: http://downloads.sourceforge.net/project/pcapsipdump/pcapsipdump/0.1.4/%{name}-%{version}.tar.gz
Patch0:  pcapsipdump.h.patch

BuildRequires: libpcap-devel
Requires: libpcap

%description
pcapsipdump is a tool for dumping SIP sessions (+RTP
traffic, if available) to disk in a fashion similar
to "tcpdump -w" (format is exactly the same), but one
file per sip session (even if there is thousands of
concurrent SIP sessions).

%prep
%setup -q
%patch0 -p0

%build
make

%install
mkdir -p %{buildroot}/usr/sbin %{buildroot}/etc/sysconfig %{buildroot}/etc/rc.d/init.d %{buildroot}/var/spool
make DESTDIR=%{buildroot} install

%post
chkconfig pcapsipdump --add

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %attr(0755,root,root) /etc/sysconfig/pcapsipdump
%attr(0700,root,root) %dir    /var/spool/pcapsipdump
%attr(0755,root,root)       /etc/rc.d/init.d/pcapsipdump
%attr(0755,root,root)      /usr/sbin/pcapsipdump


%changelog
* Thu Mar 24 2011 zamir <zamir@mandriva.org> 0.1.4-0mdv2011.0
+ Revision: 648338
- fix spec
- first build
- create pcapsipdump

