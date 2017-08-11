%global _hardened_build 1

Name:    budgie-vala-panel-appmenu-plugin
Version: 0.5.3
Release: 1%{?dist}
License: LGPL-3.0+
Summary: This package provides Application Menu plugin for Budgie Desktop
URL:     https://github.com/rilian-la-te/vala-panel-appmenu

Source0: https://github.com/rilian-la-te/vala-panel-appmenu/releases/download/%{version}/vala-panel-appmenu-%{version}.tar.gz

BuildRequires: cmake >= 2.8.0
BuildRequires: gettext
BuildRequires: vala >= 0.32.0
BuildRequires: pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires: pkgconfig(libpeas-1.0) >= 1.2.0
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libxfconf-0)
BuildRequires: pkgconfig(libwnck-3.0) >= 3.4.0
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(budgie-1.0)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)

Requires: bamf-daemon
Requires: libdbusmenu
Requires: libdbusmenu-gtk2
Requires: libdbusmenu-gtk3
Requires: libappmenu-gtk2-parser
Requires: libappmenu-gtk3-parser
Requires: appmenu-gtk-module-common
Requires: appmenu-gtk2-module
Requires: appmenu-gtk3-module
Requires: appmenu-qt
Requires: appmenu-qt5
Requires: appmenu-qt5-profile.d

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


%description
This is Application Menu (Global Menu) plugin for Budgie Desktop.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.


%prep
%autosetup -n vala-panel-appmenu-%{version} -p1

cat > appmenu-gtk-module.sh << EOF
if [ -z "\$%{nil}GTK_MODULES" ]; then
    export GTK_MODULES="appmenu-gtk-module"
else
    export GTK_MODULES="\$%{nil}GTK_MODULES:appmenu-gtk-module"
fi
if [ -z "\$%{nil}UBUNTU_MENUPROXY" ]; then
    export UBUNTU_MENUPROXY=1
fi
EOF


%build
%cmake -DGSETTINGS_COMPILE=OFF -DENABLE_XFCE=OFF -DENABLE_VALAPANEL=OFF \
       -DENABLE_BUDGIE=ON -DENABLE_MATE=OFF -DENABLE_UNITY_GTK_MODULE=ON
%make_build

%install
%make_install DESTDIR=%{buildroot}
install -Dm 0644 appmenu-gtk-module.sh %{buildroot}%{_sysconfdir}/profile.d/appmenu-gtk-module.sh
rm -rf %{buildroot}/%{_datadir}/locale/


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

%files
%doc README.md
%license LICENSE
%{_libdir}/budgie-desktop/plugins/%{name}/

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
%config %{_sysconfdir}/profile.d/appmenu-gtk-module.*
%{_datadir}/glib-2.0/schemas/*
%{_userunitdir}/appmenu-gtk-module.service

%files -n appmenu-gtk2-module
%{_libdir}/gtk-2.0/modules/libappmenu-gtk-module.so

%files -n appmenu-gtk3-module
%{_libdir}/gtk-3.0/modules/libappmenu-gtk-module.so

%changelog
* Fri Aug 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.3-1
- update to 0.5.3

* Mon Aug 07 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-3
- add appmenu-gtk-module profile

* Mon Aug 07 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-2
- update spec file
- use appmenu-gtk-module instead unity-gtk-module

* Sat Jul 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-1
- Initial package
