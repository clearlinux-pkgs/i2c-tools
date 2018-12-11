#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : i2c-tools
Version  : 4.1
Release  : 12
URL      : https://www.kernel.org/pub/software/utils/i2c-tools/i2c-tools-4.1.tar.xz
Source0  : https://www.kernel.org/pub/software/utils/i2c-tools/i2c-tools-4.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: i2c-tools-bin = %{version}-%{release}
Requires: i2c-tools-lib = %{version}-%{release}
Requires: i2c-tools-license = %{version}-%{release}
Requires: i2c-tools-man = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
I2C TOOLS FOR LINUX
===================
This package contains an heterogeneous set of I2C tools for the Linux kernel
as well as an I2C library. The tools were originally part of the lm-sensors
project but were finally split into their own package for convenience. The
library is used by some of the tools, but can also be used by third-party
applications. The tools and library compile, run and have been tested on
GNU/Linux.

%package bin
Summary: bin components for the i2c-tools package.
Group: Binaries
Requires: i2c-tools-license = %{version}-%{release}
Requires: i2c-tools-man = %{version}-%{release}

%description bin
bin components for the i2c-tools package.


%package dev
Summary: dev components for the i2c-tools package.
Group: Development
Requires: i2c-tools-lib = %{version}-%{release}
Requires: i2c-tools-bin = %{version}-%{release}
Provides: i2c-tools-devel = %{version}-%{release}

%description dev
dev components for the i2c-tools package.


%package lib
Summary: lib components for the i2c-tools package.
Group: Libraries
Requires: i2c-tools-license = %{version}-%{release}

%description lib
lib components for the i2c-tools package.


%package license
Summary: license components for the i2c-tools package.
Group: Default

%description license
license components for the i2c-tools package.


%package man
Summary: man components for the i2c-tools package.
Group: Default

%description man
man components for the i2c-tools package.


%prep
%setup -q -n i2c-tools-4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544544805
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1544544805
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/i2c-tools
cp COPYING %{buildroot}/usr/share/package-licenses/i2c-tools/COPYING
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/i2c-tools/COPYING.LGPL
%make_install PREFIX=/usr libdir=/usr/lib64

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ddcmon
/usr/bin/decode-dimms
/usr/bin/decode-edid
/usr/bin/decode-vaio
/usr/bin/i2c-stub-from-dump
/usr/bin/i2cdetect
/usr/bin/i2cdump
/usr/bin/i2cget
/usr/bin/i2cset
/usr/bin/i2ctransfer

%files dev
%defattr(-,root,root,-)
/usr/include/i2c/smbus.h
/usr/lib64/libi2c.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libi2c.so.0
/usr/lib64/libi2c.so.0.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/i2c-tools/COPYING
/usr/share/package-licenses/i2c-tools/COPYING.LGPL

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/decode-dimms.1
/usr/share/man/man1/decode-vaio.1
/usr/share/man/man8/i2c-stub-from-dump.8
/usr/share/man/man8/i2cdetect.8
/usr/share/man/man8/i2cdump.8
/usr/share/man/man8/i2cget.8
/usr/share/man/man8/i2cset.8
/usr/share/man/man8/i2ctransfer.8
