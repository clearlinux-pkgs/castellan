#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : castellan
Version  : 0.20.1
Release  : 25
URL      : https://files.pythonhosted.org/packages/cc/d4/8118e9c332750cfe3aab8b1328224271b53518ad0e799b67e09b07a76782/castellan-0.20.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/d4/8118e9c332750cfe3aab8b1328224271b53518ad0e799b67e09b07a76782/castellan-0.20.1.tar.gz
Summary  : Generic Key Manager interface for OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: castellan-python3
Requires: castellan-license
Requires: castellan-python
Requires: Babel
Requires: cryptography
Requires: keystoneauth1
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: pbr
Requires: python-barbicanclient
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr

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

%description python3
python3 components for the castellan package.


%prep
%setup -q -n castellan-0.20.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537924195
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/castellan
cp LICENSE %{buildroot}/usr/share/doc/castellan/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/castellan/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
