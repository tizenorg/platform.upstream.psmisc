Name:           psmisc
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  ncurses-devel
BuildRequires:  gettext-tools
Url:            http://sourceforge.net/projects/psmisc/
Version:        22.16
Release:        0
Provides:       ps:/usr/bin/killall
Summary:        Utilities for managing processes on your system
License:        GPL-2.0+
Group:          System/Monitoring
Source:         http://sourceforge.net/projects/psmisc/files/psmisc/%{name}-%{version}.tar.gz
Patch0:         %name-22.16.dif
Patch1:         %name-22.12-tigetstr.patch
Patch2:         %name-22.12-pstree.patch
Patch42:        pstree-segfault.patch
Patch43:        %name-22.16-timeout.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%prep
%setup -q
%patch42 -p1 -b .to
%patch43 -p1 -b .comm
%patch1 -p0 -b .tigetstr
%patch2 -p0 -b .pstree
%patch0 -p0 -b .0

%build
autoreconf -fi
CFLAGS="-D_GNU_SOURCE ${RPM_OPT_FLAGS} -pipe"
CXXFLAGS="$CFLAGS"
CC=gcc
CXX=g++
export CFLAGS CXXFLAGS CC CXX
sh ./configure --prefix=%{_prefix} --mandir=%{_mandir} \
	--disable-rpath		\
	--with-gnu-ld		\
	--disable-nls		\
	--enable-timeout-stat
make %{?_smp_mflags} CFLAGS="$CFLAGS" "CC=$CC"

%install
make DESTDIR=$RPM_BUILD_ROOT install

%docs_package

%files 
%defattr (-,root,root,755)
%{_bindir}/fuser
%{_bindir}/killall
%{_bindir}/peekfd
%{_bindir}/prtstat
%{_bindir}/pstree
%{_bindir}/pstree.x11

