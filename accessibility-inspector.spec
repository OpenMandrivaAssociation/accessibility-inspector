%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Name:		accessibility-inspector
Version:	26.08.2
Release:	1
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Inspect your application accessibility tree
URL:		https://apps.kde.org/accessibilityinspector/
License:	LGPLv2+
Group:		Graphical desktop/KDE
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(QAccessibilityClient6)

%description
Accessibility Inspector lets you inspect the accessibility tree of
applications and check items exposed via AT-SPI.

%files -f %{name}.lang
%{_bindir}/accessibilityinspector
%{_libdir}/libaccessibilityinspector.so.*
%{_datadir}/applications/org.kde.accessibilityinspector.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.accessibilityinspector.svg
%{_datadir}/metainfo/org.kde.accessibilityinspector.metainfo.xml
%{_datadir}/qlogging-categories6/accessibilityinspector.*
