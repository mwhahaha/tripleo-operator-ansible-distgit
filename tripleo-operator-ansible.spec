# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global srcname tripleo_operator_ansible
%global collectionname tripleo-operator-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{collectionname}
Version:        XXX
Release:        XXX
Summary:        Ansible Collection to perform TripleO related actions.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/tripleo-operator-ansible
Source0:        https://tarballs.openstack.org/%{collectionname}/%{collectionname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
Requires: ansible
%else
Requires: python3dist(ansible)
%endif

%description

Ansible Collection to perform TripleO related actions

%prep
%autosetup -n %{collectionname}-%{upstream_version} -S git


%build
%pyver_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%pyver_install


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/collections/tripleo/operator/


%changelog

