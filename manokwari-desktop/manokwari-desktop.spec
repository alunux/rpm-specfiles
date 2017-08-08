%global _hardened_build 1
%global _vpath_builddir build

Name:       manokwari
Version:    1.0.13
Release:    1%{?dist}
License:    GPL-2.0
Summary:    Desktop shell for GNOME 3 with Gtk+ and HTML5 frontend
URL:        http://manokwari.blankonlinux.or.id

Source0: https://github.com/BlankOn/manokwari/archive/%{version}.tar.gz
Patch0: 0001-Add-Meson-as-optional-build-system.patch
Patch1: 0002-meson-remove-unused-variable.patch

BuildRequires: pkgconfig(glib-2.0) >= 2.12.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.8
BuildRequires: pkgconfig(atk) >= 2.0.0
BuildRequires: pkgconfig(gee-1.0) >= 0.6.1
BuildRequires: pkgconfig(cairo) >= 1.10.2
BuildRequires: pkgconfig(libgnome-menu-3.0) >= 2.30.5
BuildRequires: pkgconfig(libwnck-3.0) >= 3.0.0
BuildRequires: pkgconfig(unique-3.0) >= 3.0.0
BuildRequires: pkgconfig(webkitgtk-3.0) >= 1.3.0
BuildRequires: pkgconfig(x11) >= 1.6.0
BuildRequires: pkgconfig(libnotify) >= 0.7.6

BuildRequires: vala >= 0.28
BuildRequires: meson
BuildRequires: intltool

Requires: hicolor-icon-theme
Requires: gnome-session
Requires: gnome-settings-daemon
Requires: control-center
Requires: gnome-screensaver
Requires: network-manager-applet
Requires: webkitgtk3
Requires: libnotify

%description
Manokwari is a desktop shell for GNOME 3 with Gtk+ and HTML5 frontend

%prep
%autosetup -p1

%build
export LC_ALL=en_US.utf8
%meson
%meson_build

%install
export LC_ALL=en_US.utf8
%meson_install

%find_lang %{name}

%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null
    /usr/bin/update-desktop-database &> /dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/update-desktop-database &> /dev/null
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%doc DESIGN.md HACKING.md Styling.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/blankon-session
%config(noreplace) %{_sysconfdir}/xdg/menus/%{name}-applications.menu
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome-session/sessions/blankon.session
%{_datadir}/xsessions/blankon.desktop

%changelog
* Tue Aug 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.0.13-1
- initial package
