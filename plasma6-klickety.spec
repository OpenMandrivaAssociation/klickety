%define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-klickety
Version:	24.01.96
Release:	%{?git:0.%{git}.}1
Summary:	An adaptation of the Clickomania game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksame/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/klickety/-/archive/%{gitbranch}/klickety-%{gitbranchd}.tar.bz2#/klickety-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/klickety-%{version}.tar.xz
%endif
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DBusAddons)

Provides:	ksame = %{EVRD}
Obsoletes:	ksame < 1:4.6.74

%description
Klickety is an adaptation of the Clickomania game. The rules are similar
to those of the Same game: your goal is to clear the board by clicking on
groups to destroy them.

%files -f klickety.lang
%{_bindir}/klickety                                                                                    
%{_datadir}/applications/org.kde.klickety.desktop                                                         
%{_datadir}/applications/org.kde.ksame.desktop                                                            
%{_datadir}/klickety/klickety.kcfg
%{_datadir}/kconf_update/klickety.upd                                                             
%{_datadir}/kconf_update/klickety-2.0-inherit-ksame-highscore.pl        
%{_datadir}/klickety/themes/classic.svg
%{_datadir}/klickety/themes/classic_preview.png
%{_datadir}/klickety/themes/default.desktop
%{_datadir}/klickety/themes/ksame.desktop
%{_datadir}/klickety/themes/ksame.svg
%{_datadir}/klickety/themes/ksame_old.desktop
%{_datadir}/klickety/themes/ksame_old.svg
%{_datadir}/klickety/themes/ksame_old_preview.png
%{_datadir}/klickety/themes/ksame_preview.png
%{_datadir}/metainfo/*.xml
%{_datadir}/sounds/klickety
%{_iconsdir}/*/*/apps/klickety.*                                                                       
%{_iconsdir}/*/*/apps/ksame.*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n klickety-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang klickety --with-html
