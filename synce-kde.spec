# TODO
# - split to subpackages
# - devel as -libs-devel as rest of synce-* packages do?
Summary:	KDE-Integration of SynCE. Kio-slave and Tray-Icon
Name:		synce-kde
Version:	0.9.1
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	213ea85f85414b9f05f4252028bce134
URL:		http://synce.sourceforge.net/
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
  konqueror.
- RAKI: Is a Linux-Incarnation of Activsync. It claims to be better
  than Activesync in future.

%package devel
Summary:	Header files for the KDE
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the Dynamite library.

%prep
%setup -q

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
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/raki
%attr(755,root,root) %{_bindir}/vdccm
%{_libdir}/kde3/kio_rapip.la
%{_libdir}/kde3/kio_rapip.so
%{_desktopdir}/raki.desktop
%{_datadir}/apps/konqueror/servicemenus/cab_install.desktop
%{_datadir}/apps/raki
%{_datadir}/mimelnk/application/x-raki.desktop
%{_datadir}/services/rapip.protocol
%{_datadir}/servicetypes/rakisynchronizer.desktop
%{_iconsdir}/*/*/apps/raki.png
%{_iconsdir}/*/*/apps/raki_bw.png
%{_iconsdir}/*/*/apps/rapip.png
%{_iconsdir}/*/*/apps/rapip_bw.png

# TODO: this seems wrong
%{_docdir}/kde/HTML/en/raki

%files devel
%defattr(644,root,root,755)
%{_includedir}/rakiapi.h
%{_includedir}/rakisyncfactory.h
%{_includedir}/rakisyncplugin.h
%{_includedir}/rapiwrapper.h
%{_includedir}/rra.h
