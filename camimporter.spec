# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress
%define		temproot /tmp/temproot

Summary: CamImporter: useful tool to organize you multimedia files
Name: CamImporter
Version: 0.0.1
Release: 1
License: GPL+
Group: Development/Tools
SOURCE0 : %{name}-%{version}.tar.gz
URL: https://github.com/fmount/photo-exif.git

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
# Empty section.
python setup.py build

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

