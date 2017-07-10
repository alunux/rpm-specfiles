%global _hardened_build 1
%global _vpath_builddir build

Name:       budgie-desktop
Version:    10.3.1
Release:    1%{?dist}
License:    GPL-2.0 and LGPL-2.1
Summary:    An elegant desktop with GNOME integration
URL:        https://github.com/budgie-desktop/budgie-desktop

Source0: https://github.com/budgie-desktop/budgie-desktop/releases/download/v%{version}/budgie-desktop-%{version}.tar.xz
Patch0: 0001-wm-Default-to-an-empty-rpath.patch

BuildRequires: pkgconfig(accountsservice) >= 0.6
BuildRequires: pkgconfig(gio-2.0) >= 2.46.0
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires: pkgconfig(gnome-bluetooth-1.0) >= 3.18.0
BuildRequires: pkgconfig(gnome-desktop-3.0) >= 3.18.0
BuildRequires: pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.44.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires: pkgconfig(ibus-1.0) >= 1.5.11
BuildRequires: pkgconfig(libgnome-menu-3.0) >= 3.10.1
BuildRequires: pkgconfig(libpeas-1.0) >= 1.8.0
BuildRequires: pkgconfig(libpeas-gtk-1.0) >= 1.8.0
BuildRequires: pkgconfig(libpulse) >= 2
BuildRequires: pkgconfig(libpulse-mainloop-glib) >= 2
BuildRequires: pkgconfig(libwnck-3.0) >= 3.14.0
%if 0%{?fedora} >= 26
BuildRequires: pkgconfig(libmutter-0) >= 3.18.0
%else
BuildRequires: pkgconfig(libmutter) >= 3.18.0
%endif
BuildRequires: pkgconfig(polkit-agent-1) >= 0.110
BuildRequires: pkgconfig(polkit-gobject-1) >= 0.110
BuildRequires: pkgconfig(upower-glib) >= 0.9.20
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(xtst)

BuildRequires: vala >= 0.28
BuildRequires: git
BuildRequires: meson
BuildRequires: intltool
BuildRequires: gtk-doc

Requires: hicolor-icon-theme
Requires: gnome-session
Requires: gnome-settings-daemon
Requires: control-center
Requires: gnome-screensaver
Requires: network-manager-applet

Requires: %{name}-libs
Requires: %{name}-schemas
Requires: %{name}-rundialog

%description
Budgie is the flagship desktop of the Solus, and is an Solus project.
The Budgie Desktop a modern desktop designed to keep out the way of
the user. It features heavy integration with the GNOME stack in order
for an enhanced experience.


%package    rundialog
Summary:    Budgie Run Dialog for the Budgie Desktop
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Requires:   %{name}-schemas%{?_isa} = %{version}-%{release}

%description    rundialog
Budgie Run Dialog for the Budgie Desktop


%package    libs
Summary:    Common libs for the Budgie Desktop
Requires:   gtk3 >= 3.18.0

%description    libs
Common libs for the BUdgie Desktop


%package    schemas
Summary:    GLib schemas for the Budgie Desktop

%description    schemas
GLib schemas for the Budgie Desktop


%package    docs
Summary:    GTK3 Desktop Environment -- Documentation files
Group:      Documentation/HTML

%description    docs
GTK3 Desktop Environment -- Documentation files.
This package provides API Documentation for the Budgie Plugin API, in the
GTK-Doc HTML format.


%package    devel
Summary:    Development files for the Budgoe Desktop
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for the Budgie Desktop


%prep
%autosetup -p1

%build
export LC_ALL=en_US.utf8
%meson
%meson_build

%install
export LC_ALL=en_US.utf8
%meson_install
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

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

%files -f %{name}.lang
%doc README.md
%license LICENSE LICENSE.LGPL2.1
%{_bindir}/budgie-{daemon,desktop,panel,polkit-dialog,wm}
%config(noreplace) %{_sysconfdir}/xdg/autostart/budgie-desktop-*.desktop
%{_libdir}/budgie-desktop/
%{_libdir}/girepository-1.0/Budgie*.typelib
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/gnome-session/sessions/budgie-desktop.session
%{_datadir}/icons/hicolor/scalable/actions/notification-alert-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/pane-hide-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/pane-show-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/clock-applet-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/icon-task-list-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/notifications-applet-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/separator-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/spacer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/system-tray-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/task-list-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/workspace-switcher-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/caps-lock-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/num-lock-symbolic.svg
%{_datadir}/xsessions/budgie-desktop.desktop

%files schemas
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml

%files libs
%{_libdir}/libbudgie*.so.*
%{_libdir}/libraven*.so.*

%files rundialog
%{_bindir}/budgie-run-dialog

%files docs
%{_datadir}/gtk-doc/html/budgie-desktop/

%files devel
%{_includedir}/budgie-desktop/
%{_libdir}/pkgconfig/budgie*.pc
%{_libdir}/lib*.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/vala/vapi/budgie-1.0.*

%changelog
* Tue Apr 18 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 10.3.1-1
- update spec file to build from stable branch

* Tue Apr 18 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170418.932cd0c-1
- build from commit 932cd0c656bb8134a290316274f5d698e47d1a27

* Tue Apr 18 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170418.83d57d4-1
- build from commit 83d57d4b9be3b75b3ac62bdf6ec18e851aa8080a

* Mon Apr 17 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170417.27637cb-1
- build from commit 27637cb5833a1765dbc2191cfe3c87a0911a3199

* Sun Apr 16 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170416.0087b0b-1
- build from commit 0087b0b31fac03d65526a35b47a0493d936c9a2b

* Sun Apr 16 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170416.aad18b3-1
- build from commit aad18b3e81a599662624b3967d023e7647ad8580

* Mon Apr 10 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170410.cfd4f19-1
- build from commit cfd4f1939c2862f945b98f4f550d41257e2dbac7

* Mon Apr 03 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170403.97d78d1-1
- build from commit 97d78d14941c4538389d18492fd44fdd92cdb5b9

* Tue Mar 14 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170314.17c7b07-1
- build from commit 17c7b0750866116b6accf0fd9ea9f55f923967b7

* Mon Feb 27 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170227.5991c79-1
- build from commit 5991c79
- edit spec file to adapt meson build system
- add budgie-devel as dependency
- enable debuginfo package again

* Sun Feb 12 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170212.647ad8d-1
- Split into some packages: libs, schemas, devel, and rundialog
- build from commit 647ad8d

* Thu Feb 02 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170202.8ad63dd-2
- add git to build dependency list

* Thu Feb 02 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170202.8ad63dd-1
- revert to manual build
- commit 8ad63dd

* Wed Nov 02 2016 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20161102
- automatic build

* Fri Jul 29 2016 Leigh Scott <leigh123linux@googlemail.com> - 10.2.6-2
- add requires gnome-screensaver

* Fri Jul 29 2016 Leigh Scott <leigh123linux@googlemail.com> - 10.2.6-1
- update to 10.2.6
- add requires for required startup components
- add suggests nautilus

* Sun Dec  7 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 8-2
- Propagate configuration parameters to budgie-1.0.pc.in
- Validate the Budgie desktop session file
- Verbose build output
- Fix directory ownerships

* Fri Dec  5 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 8-1
- Initial package
