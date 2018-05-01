%global _hardened_build 1
%global _vpath_builddir build

Summary: Linux Steam Integration (LSI)
Name:    linux-steam-integration
Version: 0.7.2
Release: 2%{?dist}
License: LGPLv2.1
URL:     https://github.com/solus-project/linux-steam-integration

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: meson
BuildRequires: gettext

Requires: steam
Requires: alsa-lib(x86-32)
Requires: alsa-plugins-arcamav(x86-32)
Requires: alsa-plugins-jack(x86-32)
Requires: alsa-plugins-oss(x86-32)
Requires: alsa-plugins-pulseaudio(x86-32)
Requires: alsa-plugins-samplerate(x86-32)
Requires: alsa-plugins-speex(x86-32)
Requires: alsa-plugins-upmix(x86-32)
Requires: alsa-plugins-usbstream(x86-32)
Requires: alsa-plugins-vdownmix(x86-32)
Requires: atk(x86-32)
Requires: avahi-libs(x86-32)
Requires: bzip2-libs(x86-32)
Requires: cairo(x86-32)
Requires: cups-libs(x86-32)
Requires: dbus-glib(x86-32)
Requires: dbus-libs(x86-32)
Requires: dconf(x86-32)
Requires: elfutils-libelf(x86-32)
Requires: elfutils-libs(x86-32)
Requires: expat(x86-32)
Requires: ffmpeg-libs(x86-32)
Requires: flac-libs(x86-32)
Requires: fontconfig(x86-32)
Requires: freeglut(x86-32)
Requires: freetype(x86-32)
Requires: GConf2(x86-32)
Requires: gdk-pixbuf2(x86-32)
Requires: glib2(x86-32)
Requires: glibc(x86-32)
Requires: gmp(x86-32)
Requires: gnutls(x86-32)
Requires: graphite2(x86-32)
Requires: gsm(x86-32)
Requires: gstreamer(x86-32)
Requires: gstreamer1(x86-32)
Requires: gstreamer-plugins-base(x86-32)
Requires: gtk2(x86-32)
Requires: gtk2-engines(x86-32)
Requires: gtk3(x86-32)
Requires: gtk-murrine-engine(x86-32)
Requires: harfbuzz(x86-32)
Requires: heimdal-libs(x86-32)
Requires: jack-audio-connection-kit(x86-32)
Requires: json-c(x86-32)
Requires: keyutils-libs(x86-32)
Requires: krb5-libs(x86-32)
Requires: lcms2(x86-32)
Requires: libacl(x86-32)
Requires: libappindicator(x86-32)
Requires: libasyncns(x86-32)
Requires: libattr(x86-32)
Requires: libcanberra(x86-32)
Requires: libcanberra-gtk2(x86-32)
Requires: libcap(x86-32)
Requires: libcom_err(x86-32)
Requires: libcurl(x86-32)
Requires: libdbusmenu(x86-32)
Requires: libdbusmenu-gtk2(x86-32)
Requires: libdrm(x86-32)
Requires: libexif(x86-32)
Requires: libffi(x86-32)
Requires: libgcc(x86-32)
Requires: libgcrypt(x86-32)
Requires: libGLEW(x86-32)
Requires: libgomp(x86-32)
Requires: libgpg-error(x86-32)
Requires: libICE(x86-32)
Requires: libidn(x86-32)
Requires: libindicator(x86-32)
Requires: libjpeg-turbo(x86-32)
Requires: libnotify(x86-32)
Requires: libogg(x86-32)
Requires: libpng(x86-32)
Requires: libpng12(x86-32)
Requires: libsamplerate(x86-32)
Requires: libselinux(x86-32)
Requires: libSM(x86-32)
Requires: libsndfile(x86-32)
Requires: libstdc++(x86-32)
Requires: libtasn1(x86-32)
Requires: libtdb(x86-32)
Requires: libtheora(x86-32)
Requires: libtool-ltdl(x86-32)
Requires: libusbx(x86-32)
Requires: libuuid(x86-32)
Requires: libva(x86-32)
Requires: libvdpau(x86-32)
Requires: libvorbis(x86-32)
Requires: libvpx(x86-32)
Requires: libwayland-client(x86-32)
Requires: libwayland-server(x86-32)
Requires: libX11(x86-32)
Requires: libXau(x86-32)
Requires: libXaw(x86-32)
Requires: libxcb(x86-32)
Requires: libXcomposite(x86-32)
Requires: libXcursor(x86-32)
Requires: libXdamage(x86-32)
Requires: libXdmcp(x86-32)
Requires: libXext(x86-32)
Requires: libXfixes(x86-32)
Requires: libXft(x86-32)
Requires: libXi(x86-32)
Requires: libXinerama(x86-32)
Requires: libxml2(x86-32)
Requires: libXmu(x86-32)
Requires: libXpm(x86-32)
Requires: libXrandr(x86-32)
Requires: libXrender(x86-32)
Requires: libXScrnSaver(x86-32)
Requires: libxshmfence(x86-32)
Requires: libXt(x86-32)
Requires: libXtst(x86-32)
Requires: libXxf86vm(x86-32)
Requires: mesa-libEGL(x86-32)
Requires: mesa-libgbm(x86-32)
Requires: mesa-libGL(x86-32)
Requires: mesa-libglapi(x86-32)
Requires: mesa-libGLU(x86-32)
Requires: ncurses-libs(x86-32)
Requires: nettle(x86-32)
Requires: NetworkManager-glib(x86-32)
Requires: nspr(x86-32)
Requires: nss(x86-32)
Requires: nss-softokn(x86-32)
Requires: nss-softokn-freebl(x86-32)
Requires: nss-util(x86-32)
Requires: openal-soft(x86-32)
Requires: openldap(x86-32)
Requires: openssl-libs(x86-32)
Requires: orc(x86-32)
Requires: p11-kit(x86-32)
Requires: pango(x86-32)
Requires: pangox-compat(x86-32)
Requires: pciutils-libs(x86-32)
Requires: pcre(x86-32)
Requires: pixman(x86-32)
Requires: pulseaudio-libs(x86-32)
Requires: SDL(x86-32)
Requires: SDL2(x86-32)
Requires: SDL2_image(x86-32)
Requires: SDL2_mixer(x86-32)
Requires: SDL2_net(x86-32)
Requires: SDL2_ttf(x86-32)
Requires: SDL_image(x86-32)
Requires: SDL_mixer(x86-32)
Requires: SDL_ttf(x86-32)
Requires: speex(x86-32)
Requires: speexdsp(x86-32)
Requires: sqlite(x86-32)
Requires: systemd-libs(x86-32)
Requires: tbb(x86-32)
Requires: tcp_wrappers-libs(x86-32)
Requires: xz-libs(x86-32)
Requires: zlib(x86-32)
Requires: libgudev(x86-32)
Requires: trousers-lib(x86-32)
Requires: %{name}-libs(x86-64)
Requires: %{name}-libs(x86-32)

Source0: https://github.com/solus-project/linux-steam-integration/releases/download/v%{version}/linux-steam-integration-%{version}.tar.xz

%description
A helper shim to enable better Steam* integration on Linux systems. This is part
of an effort by Solus to enhance Steam for everyone.


%package    libs
Obsoletes:  %{name} < 0.6-2%{?dist}
Requires:   %{name} = %{version}-%{release}
Summary:    Common libraries for Linux Steam Integration 

%description    libs
Common libraries for Linux Steam Integration


%prep
%autosetup -p1

%build
export LC_ALL=en_US.utf8
%if %{__isa_bits} == 64
    %meson -Dwith-shim=co-exist -Dwith-new-libcxx-abi=true -Dwith-frontend=true -Dwith-steam-binary=/usr/bin/steam
%endif
%if %{__isa_bits} == 32
    %meson -Dwith-shim=none -Dwith-new-libcxx-abi=true
%endif
%meson_build

%install
export LC_ALL=en_US.utf8
%meson_install
%find_lang %{name}
%if %{__isa_bits} == 32
    find %{buildroot} -name '*.mo' -delete
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{__isa_bits} == 64
%files -f %{name}.lang
%license LICENSE
%attr(644, root, root) %doc README.md TECHNICAL.md
%{_bindir}/lsi-steam
%{_bindir}/lsi-exec
%{_bindir}/lsi-settings
%{_datadir}/applications/lsi-settings.desktop
%{_datadir}/applications/lsi-steam.desktop
%endif

%files libs
%{_libdir}/liblsi-intercept.so
%{_libdir}/liblsi-redirect.so

%changelog
* Sun Apr 29 2018 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.7.2-2
- update to 0.7.2

* Wed Dec 20 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 0.7.2-1
- update to 0.7.2

* Tue Nov 14 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.6-3
- fix libbz2 and libudev issues
- currently, build from master branch

* Thu Nov 09 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.6-2
- drop libintercept config pacth, restore to default
- split libintercept and libredirect from main package

* Wed Nov 08 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.6-1
- update to v0.6

* Wed Oct 18 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.5-2
- don't use libintercept by default because performance issues

* Wed Oct 18 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.5-1
- update to v0.5
- backport some patches from master branch

* Wed Aug 16 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.3-5
- re-disable compat-libgcrypt from dependency again!

* Tue Aug 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.3-5
- re-enable compat-libgcrypt from dependency

* Sat Aug 12 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.3-4
- remove compat-libgcrypt from dependency

* Sat Apr 15 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.3-3
- re-enable debug package

* Wed Jan 04 2017 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - v0.3
- Build v0.3
