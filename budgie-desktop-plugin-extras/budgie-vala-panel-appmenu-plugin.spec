%global _hardened_build 1

Name:    budgie-vala-panel-appmenu-plugin
Version: 0.5.2
Release: 1%{?dist}
License: LGPL-3.0+
Summary: This package provides Application Menu plugin for Budgie Desktop
URL:     https://github.com/rilian-la-te/vala-panel-appmenu

Source0: https://github.com/rilian-la-te/vala-panel-appmenu/releases/download/%{version}/vala-panel-appmenu-%{version}.tar.gz
Patch0:  backporting-from-master.patch

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
Requires: unity-gtk2-module
Requires: unity-gtk-module
Requires: unity-gtk3-module
Requires: appmenu-qt
Requires: appmenu-qt5
Requires: appmenu-qt5-profile

%description
This is Application Menu (Global Menu) plugin for Budgie Desktop.
It built using Unity protocol and libraries,
and share all Unity limitations and advancements.


%prep
%autosetup -n vala-panel-appmenu-%{version} -p1

%build
%cmake -DGSETTINGS_COMPILE=OFF -DENABLE_XFCE=OFF -DENABLE_VALAPANEL=OFF \
       -DENABLE_BUDGIE=ON -DENABLE_MATE=OFF
%make_build

%install
%make_install DESTDIR=%{buildroot}
rm -rf %{buildroot}/%{_datadir}/locale/

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

%changelog
* Sat Jul 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.5.2-1
- Initial package
