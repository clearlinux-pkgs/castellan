#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : castellan
Version  : 3.6.0
Release  : 51
URL      : https://files.pythonhosted.org/packages/15/b8/2ead74892e8192eac3266e1589d60813a2fe134d50043905db8e4159b403/castellan-3.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/b8/2ead74892e8192eac3266e1589d60813a2fe134d50043905db8e4159b403/castellan-3.6.0.tar.gz
Summary  : Generic Key Manager interface for OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: castellan-license = %{version}-%{release}
Requires: castellan-python = %{version}-%{release}
Requires: castellan-python3 = %{version}-%{release}
Requires: cryptography
Requires: keystoneauth1
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: pbr
Requires: python-barbicanclient
Requires: requests
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : keystoneauth1
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-barbicanclient
BuildRequires : requests
BuildRequires : stevedore

%description
Castellan
        =========
        
        Generic Key Manager interface for OpenStack.

%package license
Summary: license components for the castellan package.
Group: Default

%description license
license components for the castellan package.


%package python
Summary: python components for the castellan package.
Group: Default
Requires: castellan-python3 = %{version}-%{release}

%description python
python components for the castellan package.


%package python3
Summary: python3 components for the castellan package.
Group: Default
Requires: python3-core
Provides: pypi(castellan)
Requires: pypi(cryptography)
Requires: pypi(keystoneauth1)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(python_barbicanclient)
Requires: pypi(requests)
Requires: pypi(stevedore)

%description python3
python3 components for the castellan package.


%prep
%setup -q -n castellan-3.6.0
cd %{_builddir}/castellan-3.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600104560
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/castellan
cp %{_builddir}/castellan-3.6.0/LICENSE %{buildroot}/usr/share/package-licenses/castellan/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/castellan/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
