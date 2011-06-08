%define module redis
Name:           python-%module
Version:        2.2.2
Release:        %mkrel 1
Summary:        Python client for Redis key-value store
License:        MIT
Url:            http://github.com/andymccurdy/redis-py/
Group:          Development/Python
Source:         http://cloud.github.com/downloads/andymccurdy/redis-py/%module-%{version}.tar.bz2
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Python client for Redis key-value store


%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE CHANGES README.md INSTALL
%{python_sitelib}/*

