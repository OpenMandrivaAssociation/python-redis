%define module redis

Name:           python-%{module}
Version:        2.9.1
Release:        1
Summary:        Python client for Redis key-value store
License:        MIT
Group:          Development/Python
Url:            http://github.com/andymccurdy/redis-py/
Source0:        http://cloud.github.com/downloads/andymccurdy/redis-py/redis-py-%{version}.tar.gz
BuildRequires:  python-devel
BuildArch:      noarch

%description
Python client for Redis key-value store

%prep
%setup -q -n %{module}-py-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root %{buildroot} --install-purelib=%{py_puresitedir}

%files
%doc LICENSE CHANGES INSTALL
%{py_puresitedir}/*


