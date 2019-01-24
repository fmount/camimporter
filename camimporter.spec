%define version 1.0
%define release 1
%define architecture noarch
%define summary "A new useful tool to organize your multimedia files importing them from a generic %CAMERA"
%define	temproot /tmp/temproot

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
#rm -rf %{buildroot}
#mkdir -p  %{buildroot}
mkdir -p %{temproot}
cd %{name}-0.1.1.dev7
python3 setup.py install --root=%{temproot}

# in builddir
cp -a %{temproot}/* %{buildroot}


%clean
rm -rf %{buildroot}
rm -rf %{temproot}


%files
/usr/bin/camimporter
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/PKG-INFO
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/SOURCES.txt
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/dependency_links.txt
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/entry_points.txt
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/not-zip-safe
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/requires.txt
/usr/lib/python3.7/site-packages/camimporter-0.1.1.dev7-py3.7.egg-info/top_level.txt
/usr/lib/python3.7/site-packages/camimporter/CamImporter.py
/usr/lib/python3.7/site-packages/camimporter/FileHandler.py
/usr/lib/python3.7/site-packages/camimporter/ImageHandler.py
/usr/lib/python3.7/site-packages/camimporter/__init__.py
/usr/lib/python3.7/site-packages/camimporter/cli.py
/usr/lib/python3.7/site-packages/camimporter/config.py
/usr/lib/python3.7/site-packages/camimporter/config/parameters.json
/usr/lib/python3.7/site-packages/camimporter/utils/ConsoleUtils.py
/usr/lib/python3.7/site-packages/camimporter/utils/Stats.py
/usr/lib/python3.7/site-packages/camimporter/utils/__init__.py
/usr/lib/python3.7/site-packages/camimporter/utils/parser.py
/usr/lib/python3.7/site-packages/camimporter/__pycache__/CamImporter.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/CamImporter.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/FileHandler.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/FileHandler.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/ImageHandler.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/ImageHandler.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/__init__.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/__init__.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/cli.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/cli.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/config.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/config.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/ConsoleUtils.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/ConsoleUtils.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/Stats.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/Stats.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/__init__.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/__init__.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/parser.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/parser.cpython-37.pyc
/usr/lib/python3.7/site-packages/camimporter/__pycache__/CamImporter.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/CamImporter.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/FileHandler.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/FileHandler.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/ImageHandler.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/ImageHandler.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/__init__.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/__init__.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/cli.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/cli.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/config.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/__pycache__/config.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/ConsoleUtils.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/ConsoleUtils.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/Stats.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/Stats.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/__init__.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/__init__.cpython-37.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/parser.cpython-37.opt-1.pyc
   /usr/lib/python3.7/site-packages/camimporter/utils/__pycache__/parser.cpython-37.pyc

%changelog
* Thu Jan 24 2019 Francesco Pantano <fpantano@redhat.com> 0.1-1
- Fedora 29 copr repack
* Mon Oct 16 2017 Francesco Pantano <fmount9@autistici.org> 0.1-1
- First Build
