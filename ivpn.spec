%global         debug_package %{nil}

Name:           ivpn
Version:        3.14.17
Release:        1%{?dist}
Summary:        IVPN - Secure VPN for Privacy (CLI)

License:        GPL-3.0
URL:            https://www.ivpn.net
Source0:        https://github.com/ArchitektApx/ivpn-desktop-copr/releases/download/v%{version}/ivpn.tar.gz
Source1:        ivpn-service.service
Source2:        ivpn.install

Requires:       glibc
Requires:       lsof
Requires:       openvpn

Recommends:     bash-completion

%description
IVPN is a secure VPN for privacy, offering CLI tools for managing connections.

%prep
%autosetup -n ivpn

%pre
# pre upgrade
if [ $1 == 2 ]; then
  %{SOURCE2} pre_upgrade
fi

%preun
%{_sysconfdir}/opt/%{name}/%{name}.install pre_remove

%install
# Create directories
%__install -d %{buildroot}%{_datarootdir}/bash-completion/completions
%__install -d %{buildroot}/usr/lib/systemd/system
%__install -d %{buildroot}/opt/%{name}
%__install -d %{buildroot}/opt/%{name}/etc
%__install -d %{buildroot}/opt/%{name}/wireguard-tools
%__install -d %{buildroot}/opt/%{name}/obfsproxy
%__install -d %{buildroot}/opt/%{name}/dnscrypt-proxy
%__install -d %{buildroot}/opt/%{name}/kem
%__install -d %{buildroot}/opt/%{name}/v2ray
%__install -d %{buildroot}%{_sysconfdir}/opt/%{name}

# Install daemon
%__install -D -m 0755 ivpn-service %{buildroot}%{_bindir}/ivpn-service
# Install CLI
%__install -D -m 0755 ivpn %{buildroot}%{_bindir}/ivpn
%__install -D -m 0644 ivpn.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/ivpn
# Install configuration and support files
%__install -D -m 0700 etc/client.down %{buildroot}/opt/%{name}/etc/client.down
%__install -D -m 0700 etc/client.up %{buildroot}/opt/%{name}/etc/client.up
%__install -D -m 0700 etc/firewall.sh %{buildroot}/opt/%{name}/etc/firewall.sh
%__install -D -m 0700 etc/splittun.sh %{buildroot}/opt/%{name}/etc/splittun.sh
%__install -D -m 0600 etc/servers.json %{buildroot}/opt/%{name}/etc/servers.json
%__install -D -m 0400 etc/ca.crt %{buildroot}/opt/%{name}/etc/ca.crt
%__install -D -m 0400 etc/ta.key %{buildroot}/opt/%{name}/etc/ta.key
%__install -D -m 0400 etc/dnscrypt-proxy.toml %{buildroot}/opt/%{name}/etc/dnscrypt-proxy.toml

# Required tools
%__install -D -m 0755 wireguard-tools/wg-quick %{buildroot}/opt/%{name}/wireguard-tools/wg-quick
%__install -D -m 0755 wireguard-tools/wg %{buildroot}/opt/%{name}/wireguard-tools/wg
%__install -D -m 0755 obfsproxy/obfs4proxy %{buildroot}/opt/%{name}/obfsproxy/obfs4proxy
%__install -D -m 0755 dnscrypt-proxy/dnscrypt-proxy %{buildroot}/opt/%{name}/dnscrypt-proxy/dnscrypt-proxy
%__install -D -m 0755 kem/kem-helper %{buildroot}/opt/%{name}/kem/kem-helper
%__install -D -m 0755 v2ray/v2ray %{buildroot}/opt/%{name}/v2ray/v2ray

# Systemd service file
%__install -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ivpn-service.service

# install post/pre script
%__install -D -m 0755 %{SOURCE2} %{buildroot}/%{_sysconfdir}/opt/%{name}/%{name}.install

%post
# post install
if [ $1 -eq 1 ]; then
  %{_sysconfdir}/opt/%{name}/%{name}.install post_install
fi

if [ $1 -eq 2 ]; then
  %{_sysconfdir}/opt/%{name}/%{name}.install post_upgrade
fi

%postun
%{_sysconfdir}/opt/%{name}/%{name}.install post_remove

%files
%attr(-, root, root) %{_bindir}/ivpn
%attr(-, root, root) %{_bindir}/ivpn-service
%{_datarootdir}/bash-completion/completions/ivpn
/usr/lib/systemd/system/ivpn-service.service
%attr(-, root, root) /opt/%{name}/etc/client.down
%attr(-, root, root) /opt/%{name}/etc/client.up
%attr(-, root, root) /opt/%{name}/etc/firewall.sh
%attr(-, root, root) /opt/%{name}/etc/splittun.sh
%attr(-, root, root) /opt/%{name}/etc/servers.json
%attr(-, root, root) /opt/%{name}/etc/ca.crt
%attr(-, root, root) /opt/%{name}/etc/ta.key
%attr(-, root, root) /opt/%{name}/etc/dnscrypt-proxy.toml
%attr(-, root, root) /opt/%{name}/wireguard-tools/wg-quick
%attr(-, root, root) /opt/%{name}/wireguard-tools/wg
%attr(-, root, root) /opt/%{name}/obfsproxy/obfs4proxy
%attr(-, root, root) /opt/%{name}/dnscrypt-proxy/dnscrypt-proxy
%attr(-, root, root) /opt/%{name}/kem/kem-helper
%attr(-, root, root) /opt/%{name}/v2ray/v2ray
%attr(-, root, root) %{_sysconfdir}/opt/%{name}/%{name}.install

%changelog