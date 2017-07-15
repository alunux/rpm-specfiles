%global _hardened_build 1
%global _vpath_builddir build

%global commit0 01d46180b9574e67d1e22052312a1080308cf4d6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")

Name:       budgie-pixel-saver-applet
Version:    %{build_timestamp}.%{shortcommit0}
Release:    1%{?dist}
License:    GPL-2.0
Summary:    Budgie Pixel Saver
URL:        https://github.com/ilgarmehmetali/budgie-pixel-saver-applet

Source0: https://github.com/ilgarmehmetali/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  0001-meson-automatic-generate-LIB_INSTALL_DIR-value.patch
Patch1: 0002-meson-convert-post-install-shell-script-to-python.patch

BuildRequires: pkgconfig(budgie-1.0) >= 2
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(libpeas-1.0) >= 1.8.0
BuildRequires: pkgconfig(libwnck-3.0) >= 3.14.0
BuildRequires: vala >= 0.28
BuildRequires: meson <= 0.40.1

%description
This applet hides the title bar from maximized windows and creates a new one
inside the panel. Inspired from gnome extension pixel-saver.

- Added settings to choose action buttons and title bar visibility.
  This way its possible to create different layouts with multiple applets.
- Added settings to set title length.


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
%{_datadir}/glib-2.0/schemas/net.milgar.budgie-pixel-saver.gschema.xml

%changelog
* Sat Jul 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170715.01d4618-1
- Initial package
- build from git master branch - 01d46180b9574e67d1e22052312a1080308cf4d6
