# IVPN CLI & IVPN UI for aarch64

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![📦 Architecture: aarch64](https://img.shields.io/badge/📦_Architecture-aarch64-blue?style=flat-square)

Automatically updated spec files and aarch64/arm64 build workflows for the [IVPN Desktop App](https://github.com/ivpn/desktop-app) packaged for fedora.

## IVPN CLI
[![Latest Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Version&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Darchitektapx%26projectname%3Divpn%26packagename%3Divpn%26with_latest_build%3DTrue&style=flat-square&logoColor=blue)](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/package/ivpn/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/package/ivpn/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/package/ivpn/)

`ivpn` provides the baseline IVPN CLI Interface

## IVPN UI
[![Latest Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Version&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Darchitektapx%26projectname%3Divpn%26packagename%3Divpn-ui%26with_latest_build%3DTrue&style=flat-square&logoColor=blue)](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/package/ivpn-ui/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/package/ivpn-ui/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/package/ivpn-ui/)

`ivpn-ui` provides the IVPN Desktop App and TrayIcon

## Issue Contacts
Bugs related to IVPN should be reported directly to the IVPN GitHub repo:
<https://github.com/ivpn/desktop-app>

Bugs related to this package should be reported at this Github project:
<https://github.com/ArchitektApx/ivpn-desktop-copr>

## Installation Instructions
1. Enable `architektapx/ivpn` [Copr](https://copr.fedorainfracloud.org/coprs/architektapx/ivpn/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable architektapx/ivpn
# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable architektapx/ivpn
```

2. (Optional) Update your package list.
```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.
```Shell
# to only install the cli interface use the ivpn package
sudo dnf install ivpn
# to install the full Desktop app use the ivpn-ui package
sudo dnf install ivpn-ui
```

4. Launch the application from the Application Menu or execute following command in terminal.
```Shell
ivpn
```

## RPM/DEB Installers
[All releases](https://github.com/ArchitektApx/ivpn-desktop-copr/releases) include pre-made rpm/deb files for different distros to be used.