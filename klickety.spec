Name:		klickety
Version:	15.08.2
Release:	1
Epoch:		1
Summary:	An adaptation of the Clickomania game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksame/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)
Provides:	ksame = %{EVRD}
Obsoletes:	ksame < 1:4.5.74

%description
Klickety is an adaptation of the Clickomania game. The rules are similar
to those of the Same game: your goal is to clear the board by clicking on
groups to destroy them.

%files
%{_bindir}/klickety                                                                                    
%{_datadir}/applications/kde4/klickety.desktop                                                         
%{_datadir}/applications/kde4/ksame.desktop                                                            
%{_datadir}/apps/klickety                                                                              
%{_datadir}/apps/kconf_update/klickety.upd                                                             
%{_datadir}/apps/kconf_update/klickety-2.0-inherit-ksame-highscore.pl                                  
%doc %{_docdir}/HTML/en/klickety                                                                       
%{_iconsdir}/*/*/apps/klickety.*                                                                       
%{_iconsdir}/*/*/apps/ksame.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

