%define module redis

Name:           python-%module
Version:	8.1.0
Release:	2
Summary:        Python client for Redis key-value store
License:        MIT
Group:          Development/Python
Url:            https://github.com/andymccurdy/redis-py/
Source0:	https://github.com/redis/redis-py/archive/refs/tags/v%{version}.tar.gz
BuildSystem:	python
BuildRequires:  python
BuildRequires:  python%{pyver}dist(hatchling)
BuildArch:      noarch

%description
Python client for Redis key-value store

%files
%doc LICENSE CHANGES
%{python_sitelib}/*
