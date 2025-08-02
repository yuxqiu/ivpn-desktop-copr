%global         debug_package %{nil}

Name:           ivpn-ui
Version:            3.14.34
Release:        1%{?dist}
Summary:        IVPN - Secure VPN for Privacy (CLI)

License:        GPL-3.0
URL:            https://www.ivpn.net
Source0:        https://github.com/ArchitektApx/ivpn-desktop-copr/releases/download/v%{version}/ivpn.tar.gz

Requires:       ivpn >= %{version}

%description
IVPN is a secure VPN focused on privacy. This package provides the desktop UI.

%prep
%autosetup -n ivpn

%install
%__install -d %{buildroot}/opt/ivpn/ui
%__install -d %{buildroot}%{_datadir}/applications
%__install -d %{buildroot}%{_sysconfdir}/opt/ivpn

# Install the compiled UI to the proper locations
mkdir -p %{buildroot}/opt/ivpn/ui/bin
%__cp -fr ui/bin/* %{buildroot}/opt/ivpn/ui/bin

%__install -D ui/IVPN.desktop %{buildroot}%{_datadir}/applications/IVPN.desktop
%__install -D ui/IVPN.desktop %{buildroot}/opt/ivpn/ui/IVPN.desktop
%__install -D ui/ivpnicon.svg %{buildroot}/opt/ivpn/ui/ivpnicon.svg

%files
/opt/ivpn/ui/bin/*
%{_datadir}/applications/IVPN.desktop
/opt/ivpn/ui/IVPN.desktop
/opt/ivpn/ui/ivpnicon.svg

%changelog
* Sat Aug 02 2025 ArchitektApx <architektapx@gehinors.ch> - 3.14.34
- Update to upstream release v3.14.34 from https://github.com/ivpn/desktop-app/releases/tag/v3.14.34

* Wed Nov 27 2024 ArchitektApx <architektapx@gehinors.ch> - 3.14.29
- Update to upstream release v3.14.29 from https://github.com/ivpn/desktop-app/releases/tag/v3.14.29
