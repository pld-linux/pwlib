#
# Conditional build:
%bcond_with	dc1394		# build DC 1394 video input plugin
%bcond_with	avc1394		# build AVC 1394 video input plugin
#
Summary:	Portable Windows Libary
Summary(pl.UTF-8):	Biblioteka zapewniająca przenośność między Windows i Uniksami
Summary(pt_BR.UTF-8):	Biblioteca Windows Portavel
Name:		pwlib
Version:	1.10.10
Release:	7
Epoch:		0
License:	MPL 1.0
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/pwlib/1.10/%{name}-%{version}.tar.bz2
# Source0-md5:	2c3bf7e8236a96659728ad139ce30b33
#Source0:	http://www.voxgratia.org/releases/pwlib-v1_10_3-src-tar.gz
Patch0:		%{name}-mak_files.patch
Patch1:		%{name}-libname.patch
Patch2:		%{name}-bison-pure.patch
Patch3:		%{name}-opt.patch
Patch4:		%{name}-lib64.patch
Patch5:		%{name}-API.patch
Patch6:		%{name}-sparc64.patch
URL:		http://www.voxgratia.org/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel >= 1.0.1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison >= 1.875
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	expat-devel
BuildRequires:	flex
%{?with_avc1394:BuildRequires:	libavc1394-devel}
%{?with_dc1394:BuildRequires:	libdc1394-devel < 2.0.0}
BuildRequires:	libdv-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PWLib is a moderately large class library that has its genesis many
years ago as a method to product applications to run on both Microsoft
Windows and Unix X Window systems. It also was to have a Macintosh
port as well but this never eventuated. Unfortunately this package
contains no GUI code.

%description -l pl.UTF-8
PWLib to dosyć duża biblioteka klas, która wywodzi się ze sposobu na
tworzenie aplikacji działających zarówno pod Microsoft Windows jak i
uniksowych X Window. Miała też mieć port na Macintosha. Ten pakiet nie
zawiera kodu GUI.

%description -l pt_BR.UTF-8
PWLib e uma biblioteca de classes razoavelmente grande que teve seu
inicio ha alguns anos atras como um metodo para produzir aplicacoes
para serem executadas tanto em Windows quanto em sitemas Unix baseados
em X-Window. Tambem possui um porte para Macintosh mas nunca foi
terminado. Esta versao nao contem nenhum codigo para interface.

%package devel
Summary:	Portable Windows Libary development files
Summary(pl.UTF-8):	Pliki dla programistów używających pwlib
Summary(pt_BR.UTF-8):	Pacote de desenvolvimento para a pwlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel
Requires:	cyrus-sasl-devel >= 2.0
Requires:	expat-devel
Requires:	libstdc++-devel
Requires:	openldap-devel >= 2.4.6
Requires:	openssl-devel >= 0.9.7c
Conflicts:	ptlib-devel

%description devel
Header files and libraries for developing applications that use pwlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki konieczne do rozwoju aplikacji
używających pwlib.

%description devel -l pt_BR.UTF-8
O pacote pwlib-devel inclui as bibliotecas e arquivos de header para a
biblioteca pwlib.

%package static
Summary:	Portable Windows Libary static libraries
Summary(pl.UTF-8):	Biblioteki statyczne pwlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	ptlib-static

%description static
pwlib static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne pwlib.

%package sound-alsa
Summary:	Alsa audio plugin
Summary(pl.UTF-8):	Wtyczka dźwiękowa Alsa
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0.1
Provides:	pwlib-sound

%description sound-alsa
Alsa audio plugin.

%description sound-alsa -l pl.UTF-8
Wtyczka dźwiękowa Alsa.

%package sound-oss
Summary:	OSS audio plugin
Summary(pl.UTF-8):	Wtyczka dźwiękowa OSS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	pwlib-sound

%description sound-oss
OSS audio plugin.

%description sound-oss -l pl.UTF-8
Wtyczka dźwiękowa OSS.

%package video-avc
Summary:	AVC 1394 video input plugin
Summary(pl.UTF-8):	Wtyczka wejścia obrazu AVC 1394
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-avc
AVC 1394 video input plugin.

%description video-avc -l pl.UTF-8
Wtyczka wejścia obrazu AVC 1394.

%package video-dc
Summary:	DC 1394 video input plugin
Summary(pl.UTF-8):	Wtyczka wejścia obrazu DC 1394
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-dc
DC 1394 video input plugin.

%description video-dc -l pl.UTF-8
Wtyczka wejścia obrazu DC 1394.

%package video-v4l
Summary:	v4l video input plugin
Summary(pl.UTF-8):	Wtyczka wejścia obrazu v4l
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-v4l
v4l video input plugin.

%description video-v4l -l pl.UTF-8
Wtyczka wejścia obrazu v4l.

%package video-v4l2
Summary:	v4l2 video input plugin
Summary(pl.UTF-8):	Wtyczka wejścia obrazu v4l2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-v4l2
v4l2 video input plugin.

%description video-v4l2 -l pl.UTF-8
Wtyczka wejścia obrazu v4l2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if "%{_lib}" == "lib64"
%patch4 -p1
%endif
%patch5 -p1
%ifarch sparc64
%patch6 -p1
%endif

ln -sf make bin

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-plugins \
	--enable-v4l2 \
	%{!?with_avc1394:--disable-avc} \
	%{!?with_dc1394:--disable-dc}

dir=$(pwd)
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	PWLIBDIR="$dir" \
	PWLIBMAKEDIR="$dir/make" \
	PW_LIBDIR="$dir/lib" \
	OPTCCFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/%{name}}

dir=$(pwd)
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PWLIBDIR="$dir" \
	PWLIBMAKEDIR="$dir/make" \
	PW_LIBDIR="$dir/lib" \

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
%{_includedir}/ptclib
%{_includedir}/ptlib
%{_includedir}/pwlib
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

%if %{with avc1394}
%files video-avc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/avc_pwplugin.so
%endif

%if %{with dc1394}
%files video-dc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/dc_pwplugin.so
%endif

%files video-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/v4l_pwplugin.so

%files video-v4l2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pwlib/devices/videoinput/v4l2_pwplugin.so
