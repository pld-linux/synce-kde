# TODO
# - split to subpackages
# - devel as -libs-devel as rest of synce-* packages do?
Summary:	KDE-Integration of SynCE. Kio-slave and Tray-Icon
Summary(pl.UTF-8):	Integracja SynCE z KDE - moduł kio-slave i ikona zasobnika systemowego
Name:		synce-kde
Version:	0.9.1
Release:	3
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	213ea85f85414b9f05f4252028bce134
Patch0:		kde-common-PLD.patch
Patch1:		kde-am.patch
Patch2:		kde-ac260.patch
Patch3:		kde-ac260-lt.patch
Patch4:		synce-kde-desktop.patch
URL:		http://www.synce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-dynamite-libs-devel
BuildRequires:	synce-orange-libs-devel
BuildRequires:	synce-rra-devel >= 0.9.1
BuildRequires:	synce-unshield-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Package is a KDE-Integration of SynCE. It consists of a kio_slave
(RAPIP), a KDE System-Tray Application (RAKI) and an enhanced direct
cable connection manager (VDCCM).

- RAPIP: Lets you transparently interact with your PockePC via
  Konqueror.
- RAKI: Is a Linux-Incarnation of Activesync. It claims to be better
  than Activesync in future.

%description -l pl.UTF-8
Ten pakiet integruje SynCE z KDE. Składa się z modułu kio_slave
(RAPIP), aplikacji zasobnika systemowego KDE (RAKI) i rozszerzonego
zarządcy bezpośredniego połączenia kabelkiem (VDCCM).

- RAPIP pozwala w sposób przezroczysty pracować z PocketPC poprzez
  Konquerora.
- RAKI to linuksowa wersja Activesynca; w przyszłości ma być lepsza
  niż Activesync.

%package devel
Summary:	Header files for the Dynamite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Dynamite
Group:		Development/Libraries
# doesn't require base

%description devel
Header files for the Dynamite library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Dynamite.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}/kde \

%find_lang %{name} --with-kde
# note: separate on package split
%find_lang raki --with-kde
cat raki.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/raki
%attr(755,root,root) %{_bindir}/vdccm
%{_libdir}/kde3/kio_rapip.la
%attr(755,root,root) %{_libdir}/kde3/kio_rapip.so
%{_desktopdir}/kde/raki.desktop
%{_datadir}/apps/konqueror/servicemenus/cab_install.desktop
%{_datadir}/mimelnk/application/x-raki.desktop
%{_datadir}/services/rapip.protocol
%{_datadir}/servicetypes/rakisynchronizer.desktop
%{_iconsdir}/*/*/apps/raki.png
%{_iconsdir}/*/*/apps/raki_bw.png
%{_iconsdir}/*/*/apps/rapip.png
%{_iconsdir}/*/*/apps/rapip_bw.png

%dir %{_datadir}/apps/raki
%{_datadir}/apps/raki/tips
%{_datadir}/apps/raki/Infbeg.wav
%{_datadir}/apps/raki/Infend.wav
%dir %{_datadir}/apps/raki/scripts
%attr(755,root,root) %{_datadir}/apps/raki/scripts/vdccm.sh
%attr(755,root,root) %{_datadir}/apps/raki/scripts/dccm.sh

%files devel
%defattr(644,root,root,755)
%{_includedir}/rakiapi.h
%{_includedir}/rakisyncfactory.h
%{_includedir}/rakisyncplugin.h
%{_includedir}/rapiwrapper.h
%{_includedir}/rra.h
