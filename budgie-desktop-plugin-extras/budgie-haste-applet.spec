%global _hardened_build 1
%global _vpath_builddir build

%global commit0 d5f7214f1dcb134471a96bb3f2d050cd7df2ff53
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")

Name:       budgie-haste-applet
Version:    %{build_timestamp}.%{shortcommit0}
Release:    1%{?dist}
License:    GPL-2.0
Summary:    Budgie Haste Applet
URL:        https://github.com/cybre/budgie-haste-applet

Source0: https://github.com/cybre/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(budgie-1.0) >= 2
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk+-3.0) > 3.18
BuildRequires: pkgconfig(libsoup-2.4) >= 0.6
BuildRequires: vala >= 0.28
BuildRequires: meson <= 0.40.1
BuildRequires: intltool

%description
Post any text, be it code or prose, to various services directly from your
desktop. Made with ❤ for Budgie Desktop..


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

%changelog
* Sat Jul 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 20170715.d5f7214-1
- Initial package
- build from git master branch - d5f7214f1dcb134471a96bb3f2d050cd7df2ff53
