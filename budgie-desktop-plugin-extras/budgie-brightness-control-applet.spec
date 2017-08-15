%global _hardened_build 1
%global _vpath_builddir build

%global commit0 498f7f0ef4e80fd0ce9a7169ce5ff11632c9dffb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")

Name:       budgie-brightness-control-applet
Version:    %{build_timestamp}.%{shortcommit0}
Release:    1%{?dist}
License:    GPL-2.0
Summary:    Budgie Brightness Control Applet
URL:        https://github.com/ilgarmehmetali/budgie-pixel-saver-applet

Source0: https://github.com/ilgarmehmetali/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  0001-rebase-on-Budgie.Popover.patch
Patch1:  0002-fix-gsd-backlight-helper-path-on-fedora.patch

BuildRequires: pkgconfig(budgie-1.0) >= 2
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(libpeas-1.0) >= 1.8.0
BuildRequires: pkgconfig(libwnck-3.0) >= 3.14.0
BuildRequires: vala >= 0.28
BuildRequires: meson

Requires: gnome-settings-daemon

%description
This applet allows you to controll screen brightness.


%prep
%autosetup -n %{name}-%{commit0} -p1

%build
export LC_ALL=en_US.utf8
%meson
%meson_build

%install
export LC_ALL=en_US.utf8
%meson_install
find %{buildroot} -name '*.la' -delete

%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null
    /usr/bin/update-desktop-database &> /dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2/schemas &> /dev/null || :
/usr/bin/update-desktop-database &> /dev/null
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files
%license LICENSE.txt
%{_libdir}/budgie-desktop/plugins/%{name}/

%changelog
* Tue Aug 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170815.498f7f0-1
- build from 498f7f0ef4e80fd0ce9a7169ce5ff11632c9dffb
- drop meson patch

* Sat Jul 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170715.420fa7c-1
- Initial package
- build from git master branch - 420fa7c0277a0edf7229b19bf4f214590df2444e
