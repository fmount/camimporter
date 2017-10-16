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
Requires: python2-pillow, python3-pillow, python2-prettytable, python3-prettytable, python2-six,
python3-six

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
rm -rf %{temproot}


%files
/usr/bin/camimporter
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/PKG-INFO
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/SOURCES.txt
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/dependency_links.txt
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/entry_points.txt
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/not-zip-safe
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/pbr.json
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/requires.txt
/usr/lib/python2.7/site-packages/camimporter-0.0.1.dev15-py2.7.egg-info/top_level.txt
/usr/lib/python2.7/site-packages/camimporter/CamImporter.py
/usr/lib/python2.7/site-packages/camimporter/CamImporter.pyc
/usr/lib/python2.7/site-packages/camimporter/CamImporter.pyo
/usr/lib/python2.7/site-packages/camimporter/FileHandler.py
/usr/lib/python2.7/site-packages/camimporter/FileHandler.pyc
/usr/lib/python2.7/site-packages/camimporter/FileHandler.pyo
/usr/lib/python2.7/site-packages/camimporter/ImageHandler.py
/usr/lib/python2.7/site-packages/camimporter/ImageHandler.pyc
/usr/lib/python2.7/site-packages/camimporter/ImageHandler.pyo
/usr/lib/python2.7/site-packages/camimporter/__init__.py
/usr/lib/python2.7/site-packages/camimporter/__init__.pyc
/usr/lib/python2.7/site-packages/camimporter/__init__.pyo
/usr/lib/python2.7/site-packages/camimporter/cli.py
/usr/lib/python2.7/site-packages/camimporter/cli.pyc
/usr/lib/python2.7/site-packages/camimporter/cli.pyo
/usr/lib/python2.7/site-packages/camimporter/config.py
/usr/lib/python2.7/site-packages/camimporter/config.pyc
/usr/lib/python2.7/site-packages/camimporter/config.pyo
/usr/lib/python2.7/site-packages/camimporter/config/parameters.json
/usr/lib/python2.7/site-packages/camimporter/utils/ConsoleUtils.py
/usr/lib/python2.7/site-packages/camimporter/utils/ConsoleUtils.pyc
/usr/lib/python2.7/site-packages/camimporter/utils/ConsoleUtils.pyo
/usr/lib/python2.7/site-packages/camimporter/utils/Stats.py
/usr/lib/python2.7/site-packages/camimporter/utils/Stats.pyc
/usr/lib/python2.7/site-packages/camimporter/utils/Stats.pyo
/usr/lib/python2.7/site-packages/camimporter/utils/__init__.py
/usr/lib/python2.7/site-packages/camimporter/utils/__init__.pyc
/usr/lib/python2.7/site-packages/camimporter/utils/__init__.pyo
/usr/lib/python2.7/site-packages/camimporter/utils/parser.py
/usr/lib/python2.7/site-packages/camimporter/utils/parser.pyc
/usr/lib/python2.7/site-packages/camimporter/utils/parser.pyo

%changelog
* Mon Oct 16 2017 Francesco Pantano <fmount9@autistici.org> 0.1-1
- First Build
