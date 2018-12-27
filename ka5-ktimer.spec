%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		ktimer
Summary:	ktimer
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1e2b2a572e21c7ce663b20835586a2ab
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.46.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kio-devel >= 5.46.0
BuildRequires:	kf5-knotifications-devel >= 5.46.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.46.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTimer is a little tool to execute programs after some time. It allows
you to enter several tasks and to set a timer for each of them. The
timers for each task can be started, stopped, changed, or looped.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/org.kde.ktimer.desktop
%{_iconsdir}/hicolor/128x128/apps/ktimer.png
%{_iconsdir}/hicolor/16x16/apps/ktimer.png
%{_iconsdir}/hicolor/32x32/apps/ktimer.png
%{_iconsdir}/hicolor/48x48/apps/ktimer.png
%{_datadir}/metainfo/org.kde.ktimer.appdata.xml
