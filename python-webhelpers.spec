%define tarname WebHelpers
%define name	python-webhelpers
%define version	1.3
%define rel	b1
%define release %mkrel 0.%rel

Summary:	Helper functions for writing web applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:        http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}%{rel}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sluggo.scrapping.cc/python/WebHelpers/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-markupsafe >= 0.9.2
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx

%description
Web Helpers is a library of helper functions intended to make writing
web applications easier. It's the standard function library for Pylons
and TurboGears 2, but can be used with any web framework. It also
contains a large number of functions not specific to the web,
including text processing, number formatting, date calculations,
container objects, etc.

WebHelpers itself depends only on MarkupSafe, but certain helpers
depend on third-party packages as described in the docs.

%prep
%setup -q -n %{tarname}-%{version}%{rel}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib*`
make html
rm -f _build/html/.buildinfo
popd docs

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG LICENSE README.txt TODO docs/_build/html

