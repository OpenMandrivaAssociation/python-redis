%define module redis

Name:           python-%module
Version:	3.3.11
Release:	2
Summary:        Python client for Redis key-value store
License:        MIT
Group:          Development/Python
Url:            http://github.com/andymccurdy/redis-py/
Source0:	https://github.com/andymccurdy/redis-py/archive/%{version}.tar.gz
BuildRequires:  python
BuildRequires:  python2-setuptools
BuildRequires:  python-setuptools
BuildRequires:  python2-pkg-resources
BuildArch:      noarch
Provides: python-redis-py = %{version}-%{release}
Obsoletes: python-redis-py < 3

%description
Python client for Redis key-value store

%package -n python2-%{module}
Summary:        Python client for Redis key-value store
BuildRequires:	python2
BuildRequires:  python2-setuptools
Provides: python2-redis-py = %{version}-%{release}
Obsoletes: python2-redis-py < 3

%description -n python2-%{module}
Python client for Redis key-value store

%prep
%setup -q -n %{module}-py-%{version}

%build
%py2_build
%py3_build

%install
%{__python} setup.py install --root %{buildroot} --install-purelib=%{python_sitelib}
%{__python2} setup.py install --root %{buildroot} --install-purelib=%{python2_sitelib}

%files
%doc LICENSE CHANGES README.rst INSTALL
%{python_sitelib}/*

%files -n python2-%{module}
%doc LICENSE CHANGES README.rst INSTALL
%{python2_sitelib}/*
