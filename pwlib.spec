Summary:	Portable Windows Libary
Summary(pl):	Biblioteka zapewniaj�ca przeno�no�� mi�dzy Windows i Uniksami
Summary(pt_BR):	Biblioteca Windows Portavel
Name:		pwlib
Version:	1.9.0
%define	fver	%(echo %{version} | tr . _)
Release:	2
License:	MPL 1.0
Group:		Libraries
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src-tar.gz
# Source0-md5:	9163893f588f77fd8be355d10bc995b8
#Source0:	http://www.seconix.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
Patch1:		%{name}-libname.patch
Patch2:		%{name}-bison-pure.patch
Patch3:		%{name}-opt.patch
Patch4:		%{name}-lib64.patch
URL:		http://www.openh323.org/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel >= 1.0.1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison >= 1.875
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	libavc1394-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libdv-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PWLib is a moderately large class library that has its genesis many
years ago as a method to product applications to run on both Microsoft
Windows and Unix X Window systems. It also was to have a Macintosh
port as well but this never eventuated. Unfortunately this package
contains no GUI code.

%description -l pl
PWLib to dosy� du�a biblioteka klas, kt�ra wywodzi si� ze sposobu na
tworzenie aplikacji dzia�aj�cych zar�wno pod Microsoft Windows jak i
uniksowych X Window. Mia�a te� mie� port na Macintosha. Ten pakiet nie
zawiera kodu GUI.

%description -l pt_BR
PWLib e uma biblioteca de classes razoavelmente grande que teve seu
inicio ha alguns anos atras como um metodo para produzir aplicacoes
para serem executadas tanto em Windows quanto em sitemas Unix baseados
em X-Window. Tambem possui um porte para Macintosh mas nunca foi
terminado. Esta versao nao contem nenhum codigo para interface.

%package devel
Summary:	Portable Windows Libary development files
Summary(pl):	Pliki dla programist�w u�ywaj�cych pwlib
Summary(pt_BR):	Pacote de desenvolvimento para a pwlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel
Requires:	cyrus-sasl-devel >= 2.0
Requires:	expat-devel
Requires:	libstdc++-devel
Requires:	openldap-devel
Requires:	openssl-devel >= 0.9.7c

%description devel
Header files and libraries for developing applications that use pwlib.

%description devel -l pl
Pliki nag��wkowe i biblioteki konieczne do rozwoju aplikacji
u�ywaj�cych pwlib.

%description devel -l pt_BR
O pacote pwlib-devel inclui as bibliotecas e arquivos de header para a
biblioteca pwlib.

%package static
Summary:	Portable Windows Libary static libraries
Summary(pl):	Biblioteki statyczne pwlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
pwlib static libraries.

%description static -l pl
Biblioteki statyczne pwlib.

%package sound-alsa
Summary:	Alsa audio plugin
Summary(pl):	Wtyczka d�wi�kowa Alsa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0.1
Provides:	pwlib-sound

%description sound-alsa
Alsa audio plugin.

%description sound-alsa -l pl
Wtyczka d�wi�kowa Alsa.

%package sound-oss
Summary:	OSS audio plugin
Summary(pl):	Wtyczka d�wi�kowa OSS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	pwlib-sound

%description sound-oss
OSS audio plugin.

%description sound-oss -l pl
Wtyczka d�wi�kowa OSS.

%package video-avc
Summary:	AVC 1394 video input plugin
Summary(pl):	Wtyczka wej�cia obrazu AVC 1394
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-avc
AVC 1394 video input plugin.

%description video-avc -l pl
Wtyczka wej�cia obrazu AVC 1394.

%package video-dc
Summary:	DC 1394 video input plugin
Summary(pl):	Wtyczka wej�cia obrazu DC 1394
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-dc
DC 1394 video input plugin.

%description video-dc -l pl
Wtyczka wej�cia obrazu DC 1394.

%package video-v4l
Summary:	v4l video input plugin
Summary(pl):	Wtyczka wej�cia obrazu v4l
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-v4l
v4l video input plugin.

%description video-v4l -l pl
Wtyczka wej�cia obrazu v4l.

%prep
%setup -q -n %{name}_v%{fver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch sparc64 %{x8664}
%patch4 -p1
%endif

ln -sf make bin

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-plugins

%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	PWLIBDIR="`pwd`" \
	PWLIBMAKEDIR="`pwd`/make" \
	PW_LIBDIR="`pwd`/lib" \
	OPTCCFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PWLIBDIR="`pwd`" \
	PWLIBMAKEDIR="`pwd`/make" \
	PW_LIBDIR="`pwd`/lib"

cp -d lib/lib*.a $RPM_BUILD_ROOT%{_libdir}
cp version.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_libdir}/libpt*.so.*.*.*
%dir %{_libdir}/pwlib
%dir %{_libdir}/pwlib/devices
%dir %{_libdir}/pwlib/devices/sound
%dir %{_libdir}/pwlib/devices/videoinput

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpt*.so
%{_includedir}/%{name}/version.h
%{_includedir}/ptclib
%{_includedir}/ptlib
%{_includedir}/*.h
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/make
%{_datadir}/%{name}/make/*.mak

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files sound-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/sound/alsa_pwplugin.so

%files sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/sound/oss_pwplugin.so

%files video-avc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/avc_pwplugin.so

%files video-dc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/dc_pwplugin.so

%files video-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/v4l_pwplugin.so
