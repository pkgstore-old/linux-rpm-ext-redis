%global app                     redis
%global user                    %{app}
%global group                   %{app}

%global d_home                  /home
%global d_storage               %{d_home}/storage.01
%global d_data                  %{d_storage}/data.02

%global release_prefix          100

Name:                           ext-redis
Version:                        1.0.2
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure Redis
License:                        MIT

Source10:                       %{app}.local.conf

Requires:                       redis ext-system

%description
META-package for install and configure Redis.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -dp -m 0755 %{buildroot}%{d_data}/%{app}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{_sysconfdir}/%{app}.local.conf


%files
%attr(0700,%{user},%{group}) %dir %{d_data}/%{app}
%config %{_sysconfdir}/%{app}.local.conf


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- UPD: Move to GitHub.
- UPD: License.

* Tue Nov 12 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: Directory names.

* Sun Jul 28 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-108
- UPD: SPEC-file.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-107
- UPD: SPEC-file.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-106
- UPD: SPEC-file.

* Fri Apr 19 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-105
- UPD: Directory structure.

* Sun Apr 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-104
- UPD: Directory structure.

* Sat Apr 13 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-103
- NEW: 1.0.0-103.

* Wed Apr 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-102
- NEW: 1.0.0-102.

* Sat Mar 30 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- NEW: 1.0.0-101.

* Wed Feb 13 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
