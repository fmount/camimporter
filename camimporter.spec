%define version 1.0
%define release 1
%define architecture noarch
%define summary "A new useful tool to organize your multimedia files importing them from a generic %CAMERA"
%define	temproot ~/tmp/temproot
%define dev dev8
%{?python_enable_dependency_generator}

Summary: camimporter: useful tool to organize your multimedia files
Name: {{{ git_dir_name }}}
Version: {{{ git_dir_version }}}
Release: 1%{?dist}
License: MIT
Group: Development/Tools
BuildArch: %{architecture}
VCS: {{{ git_dir_vcs }}}
URL: https://github.com/fmount/camimporter.git
Source: {{{ git_dir_pack }}}

Packager: Francesco Pantano <fpantano@redhat.com>
Provides: camimporter
Requires: python2-pillow, python3-pillow, python-prettytable, python3-prettytable, python2-six, python3-six
BuildRequires: python3-devel, python-unversioned-command, python-setuptools

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
%{summary}

%global debug_package %{nil}
%prep
%setup -q

%global debug_package %{nil}
%build
#python setup.py sdist --root=%{temproot}
#python setup.py build

%install
#rm -rf %{buildroot}
#mkdir -p  %{buildroot}
mkdir -p %{temproot}
cd %{name}-0.1.1.dev16
python3 setup.py install --root=%{temproot}

# in builddir
cp -a %{temproot}/* %{buildroot}


%clean
rm -rf %{buildroot}
rm -rf %{temproot}


%files
%{python3_sitelib}/*
/usr/bin/*

%changelog
* Thu Jan 24 2019 Francesco Pantano <fpantano@redhat.com> 0.1-1
- Fedora 29 copr repack
* Mon Oct 16 2017 Francesco Pantano <fmount9@autistici.org> 0.1-1
- First Build
