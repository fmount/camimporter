%define version 0.1
%define release 1
%define architrecture noarch
%define summary "A new useful tool to organize your multimedia files importing them from a generic %CAMERA"
%define	temproot /tmp/temproot

Summary: camimporter: useful tool to organize your multimedia files
Name: camimporter
Version: 0.1
Release: 1
License: GPL+
Group: Development/Tools
SOURCE : %{name}-%{version}.tar.gz
URL: https://github.com/fmount/photo-exif.git

Packager: Francesco Pantano <fmount9@autistici.org>
Provides: camimporter
#Requires: package

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
# Empty section.
#python setup.py build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
mkdir -p %{temproot}
python setup.py install --root=%{temproot}

# in builddir
cp -a %{temproot}/* %{buildroot}


%clean
rm -rf %{buildroot}


%files

%changelog
* Mon Oct 16 2017 Francesco Pantano <fmount9@autistici.org> 0.1-1
- First Build
