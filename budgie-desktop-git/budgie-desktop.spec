%global _hardened_build 1
%global _vpath_builddir build

%global commit0 d80b745bd25489751b0290050566b388598b4271
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")

Name:    budgie-desktop
Version: %{build_timestamp}.%{shortcommit0}
Release: 1%{?dist}
License: GPLv2 and LGPLv2.1
Summary: An elegant desktop with GNOME integration
URL:     https://github.com/solus-project/budgie-desktop

Source0: https://github.com/solus-project/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# [PATCH] Fix errors were caused by desktop-file-validate
Patch0:  https://github.com/alunux/budgie-desktop/commit/2762bebcde92902c08bb25ac4ea5eef022ecd502.patch

BuildRequires: pkgconfig(accountsservice) >= 0.6.40
BuildRequires: pkgconfig(gio-2.0) >= 2.46.0
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires: pkgconfig(gnome-bluetooth-1.0) >= 3.22.0
BuildRequires: pkgconfig(gnome-desktop-3.0) >= 3.22.0
BuildRequires: pkgconfig(gnome-settings-daemon) >= 3.22.0
BuildRequires: pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.44.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires: pkgconfig(ibus-1.0) >= 1.5.11
BuildRequires: pkgconfig(libgnome-menu-3.0) >= 3.10.3
BuildRequires: pkgconfig(libnotify) >= 0.7
BuildRequires: pkgconfig(libpeas-1.0) >= 1.8.0
BuildRequires: pkgconfig(libpeas-gtk-1.0) >= 1.8.0
BuildRequires: pkgconfig(libpulse) >= 2
BuildRequires: pkgconfig(libpulse-mainloop-glib) >= 2
BuildRequires: pkgconfig(libwnck-3.0) >= 3.14.0
%if 0%{?fedora} == 28
BuildRequires: pkgconfig(libmutter-2) >= 3.28.0
%endif
%if 0%{?fedora} == 29
BuildRequires: pkgconfig(libmutter-3) >= 3.30.0
%endif
%if 0%{?fedora} >= 30
BuildRequires: pkgconfig(libmutter-4) >= 3.32.0
%endif
BuildRequires: pkgconfig(polkit-agent-1) >= 0.110
BuildRequires: pkgconfig(polkit-gobject-1) >= 0.110
BuildRequires: pkgconfig(upower-glib) >= 0.99.0
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(alsa)

BuildRequires: vala >= 0.40.0
BuildRequires: git
BuildRequires: meson
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: sassc
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme
Requires: gnome-session
Requires: gnome-settings-daemon
Requires: control-center
Requires: gnome-screensaver
Requires: network-manager-applet

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Requires: %{name}-libs
Requires: %{name}-plugins-core
Requires: %{name}-schemas
Requires: %{name}-rundialog

Recommends: adapta-gtk-theme
Recommends: pop-icon-theme

%description
Budgie is the flagship desktop of the Solus, and is an Solus project.
The Budgie Desktop a modern desktop designed to keep out the way of
the user. It features heavy integration with the GNOME stack in order
for an enhanced experience.


%package        plugins-core
Summary:        Core plugins for the Budgie Desktop
Requires:       gtk3 >= 3.22.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-schemas%{?_isa} = %{version}-%{release}

%description    plugins-core
This package contains the core plugins of Budgie Desktop.


%package        rundialog
Summary:        Budgie Run Dialog for the Budgie Desktop
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-schemas%{?_isa} = %{version}-%{release}

%description    rundialog
Budgie Run Dialog for the Budgie Desktop


%package        libs
Summary:        Common libs for the Budgie Desktop
Requires:       gtk3 >= 3.22.0

%description    libs
This package contains the shared library of Budgie Desktop.


%package        schemas
Summary:        GLib schemas for the Budgie Desktop

%description    schemas
GLib schemas for the Budgie Desktop


%package        docs
Summary:        GTK3 Desktop Environment -- Documentation files
Group:          Documentation/HTML

%description    docs
GTK3 Desktop Environment -- Documentation files.
This package provides API Documentation for the Budgie Plugin API, in the
GTK-Doc HTML format.


%package        devel
Summary:        Development files for the Budgie Desktop
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the files required for developing for Budgie Desktop.


%prep
%setup -q -T -b 0 -n %{name}-%{commit0}
if [ ! -d .git ]; then
    git clone --bare --depth 1 https://github.com/solus-project/budgie-desktop.git .git
    git config --local --bool core.bare false
    git reset --hard
fi
%patch0 -p1

%build
export LC_ALL=en_US.utf8
%if 0%{?fedora} < 28
%meson
%else
%meson -Dwith-desktop-icons=none
%endif
%meson_build


%install
export LC_ALL=en_US.utf8
%meson_install
find %{buildroot} -name '*.la' -delete

%find_lang %{name}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/budgie-*.desktop


%ldconfig_scriptlets libs


%files -f %{name}.lang
%doc README.md
%license LICENSE LICENSE.LGPL2.1
%{_bindir}/budgie-*
%config(noreplace) %{_sysconfdir}/xdg/autostart/budgie-desktop-*.desktop
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/gnome-session/sessions/budgie-desktop.session
%{_datadir}/icons/hicolor/scalable/apps/budgie-desktop-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/notification-alert-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/pane-hide-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/pane-show-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-hibernate-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-log-out-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-restart-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/system-suspend-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/clock-applet-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/icon-task-list-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/notifications-applet-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/notification-disabled-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/separator-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/spacer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/system-tray-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/task-list-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/workspace-switcher-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/my-caffeine-on-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/budgie-caffeine-cup-empty.svg
%{_datadir}/icons/hicolor/scalable/status/budgie-caffeine-cup-full.svg
%{_datadir}/icons/hicolor/scalable/status/caps-lock-symbolic.svg
%{_datadir}/icons/hicolor/scalable/status/num-lock-symbolic.svg
%{_datadir}/xsessions/budgie-desktop.desktop

%files plugins-core
%{_libdir}/budgie-desktop/*

%files schemas
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%if 0%{?fedora} >= 29
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%endif

%files libs
%{_libdir}/budgie-desktop/
%{_libdir}/libbudgietheme.so.0
%{_libdir}/libbudgietheme.so.0.0.0
%{_libdir}/libbudgie-plugin.so.0
%{_libdir}/libbudgie-plugin.so.0.0.0
%{_libdir}/libbudgie-private.so.0
%{_libdir}/libbudgie-private.so.0.0.0
%{_libdir}/libraven.so.0
%{_libdir}/libraven.so.0.0.0
%{_libdir}/girepository-1.0/Budgie*.typelib

%files rundialog
%{_bindir}/budgie-run-dialog

%files docs
%{_datadir}/gtk-doc/html/budgie-desktop/

%files devel
%{_includedir}/budgie-desktop/
%{_libdir}/pkgconfig/budgie*.pc
%{_libdir}/libbudgietheme.so
%{_libdir}/libbudgie-plugin.so
%{_libdir}/libbudgie-private.so
%{_libdir}/libraven.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/vala/vapi/budgie-1.0.*


%changelog
* Wed Feb 13 2019 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20190213.5c97692-1
- build from commit 5c97692195a540bfd2973d185f01fb2e716da6e9

* Tue Jan 01 2019 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20190101.3dda224-1
- build from commit 3dda224e130dd62b7c7d3d94bc83b320991204c5

* Tue Dec 18 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20181218.16b501a-1
- build from commit 16b501aa6329a8d4bfc814e75e703f470d7efc65

* Fri Nov 30 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20181130.8b6f241-1
- build from commit 8b6f2414a3b6c44f09ddd67fbe9e03f5b28e589e

* Thu Nov 22 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20181122.deb7707-1
- build from commit deb7707ff977d88750fd1e4e27d9c51375d062da

* Wed Oct 31 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20181031.6f75bbd-1
- build from commit 6f75bbd33b46015a13001f9ba379bf08d240f519

* Wed Oct 10 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20181010.125637b-1
- [PATCH] Revert "Implement screenshot functionality leveraging GNOME Screenshot."

* Tue Oct 09 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20181009.125637b-1
- [PATCH] GNOME 3.30 compatability patch
- drop GNOME 3.30 obselete patch

* Tue Sep 18 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180918.cb35f5b-5
- [PATCH] Fix errors were caused by desktop-file-validate
- [PATCH] Make sure vapi workspace def use real c header filenames
- [PATCH] Point vapi cheaders to their upstream equiv
- drop F25 and F26 support
- update build dependecies
- move all plugins to new package budgie-desktop-plugins-core
- handle installed files correctly (i guess)
- use ldconfig_scriptlets macro instead

* Thu Sep 13 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180913.cb35f5b-4
- [PATCH] Revert "Apply fossfreedom's 3.18 fixes, which in turn fixes #1047"

* Thu Sep 13 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180913.cb35f5b-4
- fix window button-layout issue

* Mon Sep 10 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180910.cb35f5b-3
- bring budgie-wm gschema patch
- rebuild for GNOME 3.30

* Fri Aug 31 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180826.cb35f5b-2
- bring libmutter-3 patch
- fix build issue with Vala >= 0.41

* Sat Aug 11 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180811.cb35f5b-1
- build from commit cb35f5b4f1c71d8dfa3aa8f78298b3825ce85cc2

* Thu Jul 26 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180726.5cd2ad6-1
- build from commit 5cd2ad6d211b9e1d02309ea0a531906e12969e5b

* Tue Jul 03 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180703.b85ed82-2
- substitute arc-theme with adapta-gtk-theme
- substitute arc-icon-theme and moka-icon-theme with pop-icon-theme

* Thu Jun 28 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180628.b85ed82-1
- build from commit b85ed82c6ed6a8d76d15377aac0a0c3959cb2f8e

* Fri Jun 22 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180622.6aa57a9-1
- build from commit 6aa57a9b2540b02dd1baf222ea689176cb167396

* Sun Jun 10 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180610.558455e-1
- build from commit 558455e9ade9d42175ed917d06994011c2418eb2
- update URL of Budgie project
- drop CSS patch

* Mon May 14 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180514.15c960c-2
- disable desktop icons on Fedora 28

* Sat May 05 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180505.15c960c-1
- build from commit 15c960ccd7cb58b9adad557115956a80e0508de7

* Thu May 03 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180503.f3ce3a6-1
- build from commit f3ce3a619b225447d733982af927b3968f9a28f0

* Tue May 01 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180501.7e7e7cc-1
- build from commit 7e7e7ccb8114d8709ce5d1c3ec98385feefb62f8

* Tue May 01 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180501.995e85e-1
- build from commit 995e85e59be5b653311b97fb115b50521030bb75

* Sun Apr 15 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180415.298b9ae-1
- build from commit 298b9ae48a6c6824e25fed8df65bcf1726900a56
- add gnome-settings-daemon-devel to build requirement
- dropped the libmutter-2 patch

* Tue Apr 03 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180403.e6fbc45-1
- build from commit e6fbc45256c9f5119a0d696255b95773659c9fb9
- bring patch for libmutter-2

* Thu Feb 08 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180208.d6f3519-1
- build from commit d6f3519f04d8c619f7d1797ad24a26357e578ba9

* Mon Jan 01 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180101.04c2e0a-1
- build from commit 04c2e0aac3c82e63a487de8aec7b74a4aadea8ab

* Sat Nov 04 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20171019.9f71bb8-1
- build from commit 9f71bb847ef73a14e2cd248b34aaa3866b7e795c

* Thu Oct 19 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20171019.ff09a51-2
- fix global menu css patch

* Tue Oct 17 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20171017.ff09a51-1
- build from commit ff09a5104075e9774d8f600b875e9871eccb04f8
- fix build that contains meson subprojects

* Sun Oct 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20171008.9e2cc0f-3
- recommends arc-theme, arc-icon-theme, and moka-icon-theme
- fix license short name based on https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Software_License_List

* Mon Sep 18 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170918.9e2cc0f-2
- rebuild

* Fri Sep 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170915.9e2cc0f-1
- build from commit 9e2cc0f2f6549b75ba6ba1d880ea68364ca6445c

* Mon Sep 11 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170911.69fd617-1
- build from commit 69fd617eed1da896d5a1bc5e82de901cd2a1a33d

* Thu Aug 31 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170831.c2d75cd-1
- build from commit c2d75cdcd7e2c426d5813daec8a91cbd05d5811d

* Sun Aug 20 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170820.e950d53-1
- build from commit e950d5350e910004502feb099393bf24af6f74aa

* Tue Aug 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170815.4fa0a6c-2
- revert some CSS stuff that affect global menu padding

* Tue Aug 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170815.4fa0a6c-1
- build from commit 4fa0a6cc5234648c0173f4421980d10215432b01
- this is Budgie 10.4 "Irish Summer" release

* Mon Aug 14 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170814.ad4a402-1
- build from commit ad4a40245e10f9e9c8e2ca85e7ebb9a24707f77b

* Wed Aug 09 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170809.952cf89-1
- build from commit 952cf891ddaa1572843d0e42df98ec340dccf918

* Tue Aug 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170808.ebbb960-1
- build from commit ebbb960798613fe3392ae030cf6d5053db60eec7

* Sat Jul 29 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170729.7561deb-1
- build from commit 7561deb17452b650b370e11fbe3a4f2ddfe9e74b

* Fri Jul 28 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170728.8765552-1
- build from commit 876555241ddc46fbdfa859ccce1258f80cc4eb69

* Fri Jul 21 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170721.f0c9c9f-1
- build from commit f0c9c9f1b2913e946f592680e6cfcd14713af2c0

* Mon Jul 17 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170717.929f4b8-1
- build from commit 929f4b87205bcc0a9f577e6c589b62be4a716269

* Sat Jul 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170715.73c9f8b-1
- build from commit 73c9f8b8ba9f52feb0c9542140697e66a10f7322

* Fri Jul 14 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170714.254d284-1
- build from commit 254d284cf6857e5ab3fed37cbaea4d8e09d9daad

* Mon Jul 10 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170710.d3f7271-1
- build from commit d3f7271cbe531025a149f06f8a7500735d4e85bf

* Fri Jul 07 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170707.b76cec0-1
- build from commit 917dc55dd018fdeb3d45b585b54476d8fd97c180

* Thu Jul 06 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170706.1529bed-1
- build from commit 1529bedc28ca81afe2c3417f37aba0dbcc27be30

* Thu Jul 06 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170706.9750901-1
- build from commit 97509012f5024909fd6f3612f6bcfd359ee1da5e

* Tue Jul 04 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170704.8e58415-1
- build from commit 8e58415586580f5558fd35346b313963554311ef

* Fri May 12 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170512.b07359f-1
- build from commit b07359f5c14185126ac6d780c44b25fe325c2cba

* Wed May 03 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170503.a98d794-1
- build from commit a98d7943af7270897b26d4b17bda6b525c2bf019

* Wed Apr 26 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170426.8454436-1
- build from commit 84544363a7e3c65ef4e138c7aebb5eaa3a2e794f

* Sun Apr 23 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170423.f4e1b94-1
- build from commit f4e1b949cbbf8886c0ae12a3b528aed5a2d48ae1

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
