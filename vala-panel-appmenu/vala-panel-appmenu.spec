%global _hardened_build 1

Name:    vala-panel-appmenu
Version: 0.4.4
Release: 1%{?dist}
License: LGPL-3.0+
Summary: This package provides Application Menu plugin for vala-panel
URL:     https://github.com/rilian-la-te/vala-panel-appmenu

Source0: https://github.com/rilian-la-te/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:  0001-backport-from-master.patch

BuildRequires: cmake >= 2.8.0
BuildRequires: gettext
BuildRequires: vala >= 0.32.0
BuildRequires: pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires: pkgconfig(libpeas-1.0) >= 1.2.0
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: pkgconfig(libxfconf-0)
BuildRequires: pkgconfig(vala-panel)
BuildRequires: pkgconfig(libwnck-3.0) >= 3.4.0
BuildRequires: pkgconfig(x11)

Provides: vala-panel-appmenu-plugin

Requires: vala-panel-libs
Requires: bamf-daemon
Requires: libdbusmenu-gtk2
Requires: libdbusmenu-gtk3

%description
This is Application Menu (Global Menu) plugin.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.


%package -n mate-vala-panel-appmenu-plugin
Summary:  This package provides Application Menu plugin for mate-panel
Requires: vala-panel-libs
Requires: bamf-daemon
Requires: libdbusmenu-gtk2
Requires: libdbusmenu-gtk3
Provides: vala-panel-appmenu-plugin

%description -n mate-vala-panel-appmenu-plugin
This is Application Menu (Global Menu) plugin.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.


%package -n xfce4-vala-panel-appmenu-plugin
Summary:  This package provides Application Menu plugin for xfce4-panel
Requires: vala-panel-libs
Requires: bamf-daemon
Requires: libdbusmenu-gtk2
Requires: libdbusmenu-gtk3
Provides: vala-panel-appmenu-plugin

%description -n xfce4-vala-panel-appmenu-plugin
This is Application Menu (Global Menu) plugin.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.


%package -n libappmenu-gtk-parser-devel
Summary:	   Common development-files for libappmenu-gtk{2,3}-parser
BuildArch:     noarch
BuildRequires: gtk-doc
Requires:	   gtk-doc

%description -n libappmenu-gtk-parser-devel
This package contains common headers and documentation for
libappmenu-gtk{2,3}-parser.


%package -n libappmenu-gtk2-parser
Summary:	   Gtk2MenuShell to GMenuModel parser
BuildRequires: pkgconfig(gtk+-2.0)

%description -n libappmenu-gtk2-parser
This library converts Gtk2MenuShells into GMenuModels.


%package -n libappmenu-gtk2-parser-devel
Summary:  Development-files for libappmenu-gtk2-parser
Requires: pkgconfig(gtk+-2.0)%{?_isa}
Requires: libappmenu-gtk-parser-devel	== %{version}-%{release}
Requires: libappmenu-gtk2-parser%{?_isa} == %{version}-%{release}

%description -n libappmenu-gtk2-parser-devel
This package contains development-files for libappmenu-gtk2-parser.


%package -n libappmenu-gtk3-parser
Summary:       Gtk3MenuShell to GMenuModel parser
BuildRequires: pkgconfig(gtk+-3.0)

%description -n libappmenu-gtk3-parser
This library converts Gtk3MenuShells into GMenuModels.


%package -n libappmenu-gtk3-parser-devel
Summary:  Development-files for libappmenu-gtk3-parser
Requires: pkgconfig(gtk+-3.0)%{?_isa}
Requires: libappmenu-gtk-parser-devel == %{version}-%{release}
Requires: libappmenu-gtk3-parser%{?_isa} == %{version}-%{release}

%description -n libappmenu-gtk3-parser-devel
This package contains development-files for libappmenu-gtk3-parser.


%package -n appmenu-gtk-module-common
Summary:       Common files for appmenu-gtk{2,3}-module
BuildArch:	   noarch
BuildRequires: systemd
Requires:	   /bin/sh
Requires:	   dbus
Requires:	   gawk
Requires:	   glib2
Requires:	   sed
Requires:	   systemd

%description -n appmenu-gtk-module-common
This package contains common data-files for appmenu-gtk{2,3}-module.


%package -n appmenu-gtk2-module
Summary:  Gtk2MenuShell D-Bus exporter
Requires: libappmenu-gtk2-parser%{?_isa} == %{version}-%{release}
Requires: appmenu-gtk-module-common == %{version}-%{release}
Provides: appmenu-gtk == %{version}-%{release}
Provides: appmenu-gtk%{?_isa} == %{version}-%{release}

%description -n appmenu-gtk2-module
This GTK 2 module exports Gtk2MenuShells over D-Bus.


%package -n appmenu-gtk3-module
Summary:  Gtk3MenuShell D-Bus exporter
Requires: libappmenu-gtk3-parser%{?_isa} == %{version}-%{release}
Requires: appmenu-gtk-module-common == %{version}-%{release}
Provides: appmenu-gtk3 == %{version}-%{release}
Provides: appmenu-gtk3%{?_isa} == %{version}-%{release}

%description -n appmenu-gtk3-module
This GTK 3 module exports Gtk3MenuShells over D-Bus.


%prep
%autosetup -p1

%build
%cmake -DGSETTINGS_COMPILE=OFF -DENABLE_XFCE=ON -DENABLE_VALAPANEL=OFF \
       -DENABLE_BUDGIE=OFF -DENABLE_UNITY_GTK_MODULE=ON -DENABLE_MATE=ON
%make_build

%install
%make_install DESTDIR=%{buildroot}
%find_lang %{name}

%{__mkdir} -p %{buildroot}%{_userunitdir}/default.target.wants
%{_bindir}/ln -s %{_userunitdir}/%{name}.service \
                %{buildroot}%{_userunitdir}/default.target.wants/%{name}.service

%post -n libappmenu-gtk2-parser -p /sbin/ldconfig
%postun -n libappmenu-gtk2-parser -p /sbin/ldconfig

%post -n libappmenu-gtk3-parser -p /sbin/ldconfig
%postun -n libappmenu-gtk3-parser -p /sbin/ldconfig

%postun -n appmenu-gtk-module-common
if [ $1 -eq 0 ] ; then
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n appmenu-gtk-module-common
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun -n appmenu-gtk2-module
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} --update-cache &> /dev/null || :

%post -n appmenu-gtk2-module
if [ $1 -eq 1 ] ; then
    %{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} --update-cache &> /dev/null || :
fi

%postun -n appmenu-gtk3-module
%{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache &> /dev/null || :

%post -n appmenu-gtk3-module
if [ $1 -eq 1 ] ; then
    %{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache &> /dev/null || :
fi

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_userunitdir}/default.target.wants/%{name}.service

%files -n mate-vala-panel-appmenu-plugin
%{_datadir}/dbus-1/services/org.mate.panel.applet.AppmenuAppletFactory.service
%{_datadir}/mate-panel/applets/org.vala-panel.appmenu.mate-panel-applet
%{_libdir}/mate-panel/appmenu-mate

%files -n xfce4-vala-panel-appmenu-plugin
%{_libdir}/xfce4/panel/plugins/libappmenu-xfce.so
%{_datadir}/xfce4/panel/plugins/appmenu.desktop

%files -n libappmenu-gtk-parser-devel
%{_includedir}/appmenu-gtk-module

%files -n libappmenu-gtk2-parser
%license LICENSE*
%{_libdir}/libappmenu-gtk2-parser.so.0*

%files -n libappmenu-gtk2-parser-devel
%{_libdir}/libappmenu-gtk2-parser.so
%{_libdir}/pkgconfig/appmenu-gtk2-parser.pc

%files -n libappmenu-gtk3-parser
%license LICENSE
%{_libdir}/libappmenu-gtk3-parser.so.0*

%files -n libappmenu-gtk3-parser-devel
%{_libdir}/libappmenu-gtk3-parser.so
%{_libdir}/pkgconfig/appmenu-gtk3-parser.pc

%files -n appmenu-gtk-module-common
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
%{_userunitdir}/appmenu-gtk-module.service

%files -n appmenu-gtk2-module
%{_libdir}/gtk-2.0/modules/libappmenu-gtk-module.so

%files -n appmenu-gtk3-module
%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module.so


%changelog
* Sun Apr 16 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.4.4-1
- update spec file

* Mon Apr 27 2015 Konstantin <ria.freelander@gmail.com> - 0.4.4
- Generated by CMake UseRPMTools macros
