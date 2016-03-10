#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : castellan
Version  : 0.4.0
Release  : 5
URL      : https://pypi.python.org/packages/source/c/castellan/castellan-0.4.0.tar.gz
Source0  : https://pypi.python.org/packages/source/c/castellan/castellan-0.4.0.tar.gz
Summary  : Generic Key Manager interface for OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: castellan-python
BuildRequires : Sphinx
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : enum34-python
BuildRequires : extras
BuildRequires : funcsigs-python
BuildRequires : iso8601
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : oslo.config
BuildRequires : oslo.log
BuildRequires : oslo.policy
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : prettytable-python
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pyrsistent-python
BuildRequires : python-barbicanclient
BuildRequires : python-dev
BuildRequires : python-keystoneclient
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : wrapt-python

%description
=========
Castellan
=========
Generic Key Manager interface for OpenStack.
* License: Apache License, Version 2.0
* Documentation: http://docs.openstack.org/developer/castellan
* Source: http://git.openstack.org/cgit/openstack/castellan
* Bugs: http://bugs.launchpad.net/castellan

%package python
Summary: python components for the castellan package.
Group: Default
Requires: cryptography
Requires: oslo.config

%description python
python components for the castellan package.


%prep
%setup -q -n castellan-0.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
