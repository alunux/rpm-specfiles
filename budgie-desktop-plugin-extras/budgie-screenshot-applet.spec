%global _hardened_build 1
%global _vpath_builddir build

%global commit0 0eefbe239219912d138f06d98a4f865bb31196b9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")

Name:       budgie-screenshot-applet
Version:    %{build_timestamp}.%{shortcommit0}
Release:    2%{?dist}
License:    GPL-2.0
Summary:    Budgie Screenshot Applet
URL:        https://github.com/cybre/budgie-screenshot-applet

Source0: https://github.com/cybre/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(budgie-1.0) >= 2
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18
BuildRequires: pkgconfig(libsoup-2.4) >= 0.6
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: vala >= 0.28
BuildRequires: meson
BuildRequires: intltool
BuildRequires: pkgconfig(libcurl)

Requires: libcurl

%description
Take a screenshot of your desktop, a window or region; save to disk and upload.
Made with ❤ for Budgie Desktop.


%prep
%autosetup -n %{name}-%{commit0}

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
%license LICENSE
%{_libdir}/budgie-desktop/plugins/%{name}/
%{_datadir}/appdata/com.github.cybre.%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.cybre.%{name}.gschema.xml
%{_datadir}/glib-2.0/schemas/com.github.cybre.%{name}.provider.ftp.gschema.xml


%changelog
* Sun Apr 22 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20180422.0eefbe2-2
- rebuild

* Wed Nov 22 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20171122.0eefbe2-1
- build from 0eefbe239219912d138f06d98a4f865bb31196b9

* Tue Aug 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170815.180aa7f-2
- rebuild
- fix wrong url in description

* Sat Jul 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170715.180aa7f-1
- Initial package
- build from git master branch - 180aa7f03afb9ce9e6e936ffcdfd6b04ce804269
