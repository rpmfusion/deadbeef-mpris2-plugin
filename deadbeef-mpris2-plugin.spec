Name:           deadbeef-mpris2-plugin
Version:        1.12
Release:        2%{?dist}
Summary:        MPRISv2 plugin for the DeaDBeeF music player

License:        GPLv2+
URL:            https://github.com/Serranya/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

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
%autosetup -n deadbeef-%{version}


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
