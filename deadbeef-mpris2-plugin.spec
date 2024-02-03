Name:           deadbeef-mpris2-plugin
Version:        1.16
Release:        3%{?dist}
Summary:        MPRISv2 plugin for the DeaDBeeF music player

License:        GPLv2+
URL:            https://github.com/DeaDBeeF-Player/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Build for armv7hl failed
# https://github.com/DeaDBeeF-Player/deadbeef/issues/2538
ExcludeArch:    armv7hl

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  deadbeef-devel

Requires:       deadbeef%{?_isa}

%description
This plugin aims to implement the MPRISv2 for DeaDBeeF.

The original MPRIS plugin for DeaDBeef does not work anymore and seems
to be orphaned. The original plugin supported MPRISv1 AND MPRISv2. This plugin
will only support version two.

%prep
%autosetup
autoreconf -fiv


%build
%configure \
 --disable-silent-rules \
 --disable-static
%{make_build}


%install
%{make_install}
rm %{buildroot}%{_libdir}/deadbeef/mpris.*a


%files
%doc README
%license LICENSE
%{_libdir}/deadbeef/mpris.*


%changelog
* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 11 2023 Leigh Scott <leigh123linux@gmail.com> - 1.16-1
- Update to 1.16

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> 1.14-1
- Update to 1.14

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.13-1
- Update to 1.13

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Feb 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.12-1
- Update to 1.12

* Thu Dec 27 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.11-1
- Update to 1.11

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.10-1
- Update to latest release

* Wed May 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.8-1
- Initial release for fedora
