%define module redis

Name:           python-%module
Version:        2.7.2
Release:        %mkrel 1
Summary:        Python client for Redis key-value store
License:        MIT
Group:          Development/Python
Url:            http://github.com/andymccurdy/redis-py/
Source0:        http://cloud.github.com/downloads/andymccurdy/redis-py/%module-%{version}.tar.gz
BuildRequires:  python-devel
BuildArch:      noarch

%description
Python client for Redis key-value store

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
%{__python} setup.py install --root %{buildroot} --install-purelib=%{python_sitelib}

%files
%doc LICENSE CHANGES README.md INSTALL
%{python_sitelib}/*
