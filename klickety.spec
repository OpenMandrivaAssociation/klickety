Name:		klickety
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	An adaptation of the Clickomania game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksame/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Provides:	ksame = %{EVRD}
Obsoletes:	ksame < 1:4.5.74

%description
Klickety is an adaptation of the Clickomania game. The rules are similar
to those of the Same game: your goal is to clear the board by clicking on
groups to destroy them.

%files
%{_kde_bindir}/klickety
%{_kde_applicationsdir}/klickety.desktop
%{_kde_applicationsdir}/ksame.desktop
%{_kde_appsdir}/klickety
%{_kde_appsdir}/kconf_update/klickety.upd
%{_kde_appsdir}/kconf_update/klickety-2.0-inherit-ksame-highscore.pl
%{_kde_docdir}/HTML/en/klickety
%{_kde_iconsdir}/*/*/apps/klickety.*
%{_kde_iconsdir}/*/*/apps/ksame.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

