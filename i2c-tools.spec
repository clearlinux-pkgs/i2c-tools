#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : i2c-tools
Version  : 3.0.0
Release  : 2
URL      : https://www.kernel.org/pub/software/utils/i2c-tools/i2c-tools-3.0.0.tar.gz
Source0  : https://www.kernel.org/pub/software/utils/i2c-tools/i2c-tools-3.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: i2c-tools-bin
Requires: i2c-tools-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
I2C TOOLS FOR LINUX
===================
This package contains an heterogeneous set of I2C tools for Linux. These tools
were originally part of the lm-sensors package but were finally split into
their own package for convenience.

%package bin
Summary: bin components for the i2c-tools package.
Group: Binaries

%description bin
bin components for the i2c-tools package.


%package dev
Summary: dev components for the i2c-tools package.
Group: Development
Requires: i2c-tools-bin
Provides: i2c-tools-devel

%description dev
dev components for the i2c-tools package.


%package doc
Summary: doc components for the i2c-tools package.
Group: Documentation

%description doc
doc components for the i2c-tools package.


%prep
%setup -q -n i2c-tools-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1516744343
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1516744343
rm -rf %{buildroot}
%make_install prefix=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ddcmon
/usr/bin/decode-dimms.pl
/usr/bin/decode-edid.pl
/usr/bin/decode-vaio.pl
/usr/bin/decode-xeon.pl
/usr/bin/i2cdetect
/usr/bin/i2cdump
/usr/bin/i2cget
/usr/bin/i2cset

%files dev
%defattr(-,root,root,-)
/usr/include/linux/i2c-dev.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
