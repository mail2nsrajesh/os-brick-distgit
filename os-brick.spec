# Created by pyp2rpm-1.1.2
%global pypi_name os-brick

Name:           os-brick
Version:        XXX
Release:        XXX
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python-babel >= 1.3
Requires:       python-oslo-serialization
Requires:       python-oslo-concurrency
Requires:       python-oslo-i18n
Requires:       python-oslo-log
Requires:       python-oslo-service
Requires:       python-oslo-utils
Requires:       python-retrying
Requires:       python-six >= 1.9.0

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description
OpenStack Cinder brick library for managing local volume attaches
Features
--------
* Discovery of volumes being attached to a host for many transport
protocols.
* Removal of volumes from a host.

For any other imformation, refer to the parent project, Cinder:
  https://github.com/openstack/cinder


%prep
%setup -q -n %{name}-%{upstream_version}


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# Move config files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/%{name}/rootwrap
mv %{buildroot}/usr/etc/os-brick/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/%{name}/rootwrap

%files
%license LICENSE
%doc html README.rst
%{python2_sitelib}/os_brick*
%{_datarootdir}/%{name}/rootwrap/os-brick.filters

%changelog
