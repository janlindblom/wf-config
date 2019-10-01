%global commit      e8d57d19183e0d358671e3aa7335cc2d3722321d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190904

Name:           wf-config
Version:        0.1
Release:        4.%{date}git%{shortcommit}%{?dist}
Summary:        Library for managing configuration files, written for wayfire

License:        MIT
URL:            https://github.com/WayfireWM/wf-config
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
# https://github.com/WayfireWM/wf-config/issues/12
Patch0:         %{url}/pull/13.diff#/%{name}-add-soname-version-to-library.diff

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(wlroots) >= 0.3

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/wayfire
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Oct 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-4.20190904gite8d57d1
- Fix soname version

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-3.20190904gite8d57d1
- Cosmetic fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package
