%define version 0.1
%define release 1
%define architecture noarch
%define summary "A new useful tool to organize your multimedia files importing them from a generic %CAMERA"
%define	temproot /tmp/temproot

Summary: camimporter: useful tool to organize your multimedia files
Name: camimporter
Version: %{version}
Release: %{release}
License: MIT
Group: Development/Tools
BuildArch: %{architecture}
SOURCE : %{name}-%{version}.tar.gz
URL: https://github.com/fmount/camimporter.git

Packager: Francesco Pantano <fmount9@autistici.org>
Provides: camimporter
Requires: python2-pillow, python3-pillow, python-prettytable, python3-prettytable, python2-six, python3-six

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%global debug_package %{nil}
%prep
%setup -q

%global debug_package %{nil}
%build
# Empty section.
#python setup.py build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
mkdir -p %{temproot}
python3 setup.py install --root=%{temproot}

# in builddir
cp -a %{temproot}/* %{buildroot}


%clean
rm -rf %{buildroot}
rm -rf %{temproot}


%files

%changelog
* Mon Oct 16 2017 Francesco Pantano <fmount9@autistici.org> 0.1-1
- First Build
