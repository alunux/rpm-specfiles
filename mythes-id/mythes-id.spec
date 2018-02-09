Name: mythes-id
Summary: Indonesian thesaurus
Version: 1.0.1
Release: 1%{?dist}
Source: https://github.com/idnux/thes-id/archive/%{version}.tar.gz
URL: https://idnux.wordpress.com/proyek/mythes-id
License: LGPLv2+
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-id)

%if 0%{?fedora} >= 27
BuildRequires: perl-interpreter
%else
BuildRequires: perl
%endif

%description
Indonesian Thesaurus.

%prep
%autosetup -n thes-id-%{version}

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
install -m 644 th_id_ID_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_id_ID_v2.idx
install -m 644 th_id_ID_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_id_ID_v2.dat

%files
%doc README INSTALL LICENSE
%{_datadir}/mythes/*

%changelog
* Sat Feb 10 2018 La Ode Muh. Fadlun Akbar <releng@fedoraproject.org> - 1.0.1-1
- initial packaging for Fedora
