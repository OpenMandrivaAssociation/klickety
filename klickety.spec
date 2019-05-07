%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		klickety
Version:	 19.04.1
Release:	1
Epoch:		1
Summary:	An adaptation of the Clickomania game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksame/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DBusAddons)

Provides:	ksame = %{EVRD}
Obsoletes:	ksame < 1:4.5.74

%description
Klickety is an adaptation of the Clickomania game. The rules are similar
to those of the Same game: your goal is to clear the board by clicking on
groups to destroy them.

%files -f %{name}.lang
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
%{_datadir}/kxmlgui5/klickety/klicketyui.rc                          
%{_iconsdir}/*/*/apps/klickety.*                                                                       
%{_iconsdir}/*/*/apps/ksame.*

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
