Name:           psmisc
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  ncurses-devel
BuildRequires:  gettext-tools
Url:            http://sourceforge.net/projects/psmisc/
Version:        22.20
Release:        0
Provides:       ps:/usr/bin/killall
Summary:        Utilities for managing processes on your system
License:        GPL-2.0+
Group:          System/Base
Source:         http://sourceforge.net/projects/psmisc/files/psmisc/%{name}-%{version}.tar.gz
Source1001: 	psmisc.manifest

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%prep
%setup -q
cp %{SOURCE1001} .

%build
CFLAGS="-D_GNU_SOURCE ${RPM_OPT_FLAGS} -pipe"
CXXFLAGS="$CFLAGS"
CC=%__cc
CXX=%__cxx
export CFLAGS CXXFLAGS CC CXX
%reconfigure --disable-rpath		\
	     --with-gnu-ld		\
	     --disable-nls		\
	     --enable-timeout-stat
make %{?_smp_mflags} CFLAGS="$CFLAGS" "CC=$CC"

%install
%make_install

%docs_package

%files
%manifest %{name}.manifest
%defattr (-,root,root,755)
%{_bindir}/fuser
%{_bindir}/killall
%ifnarch aarch64
%{_bindir}/peekfd
%endif
%{_bindir}/prtstat
%{_bindir}/pstree
%{_bindir}/pstree.x11

