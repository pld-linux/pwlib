#
# Conditional build:
%bcond_with	dc	# with libdc1394 digital camera interface
#			  (instead of libavc1394)
#
Summary:	Portable Windows Libary
Summary(pl):	Biblioteka zapewniaj±ca przeno¶no¶æ miêdzy Windows i uniksami
Summary(pt_BR):	Biblioteca Windows Portavel
Name:		pwlib
Version:	1.5.2
Release:	2
License:	MPL 1.0
Group:		Libraries
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	0fa33ba1b32b254abe0b731a52c0f2f9
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-mak_files.patch
Patch2:		%{name}-libname.patch
Patch3:		%{name}-bison-pure.patch
Patch4:		%{name}-opt.patch
URL:		http://www.openh323.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875
BuildRequires:	expat-devel
BuildRequires:	flex
%{!?with_dc:BuildRequires:	libavc1394-devel}
%{?with_dc:BuildRequires:	libdc1394-devel}
%{!?with_dc:BuildRequires:	libdv-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PWLib is a moderately large class library that has its genesis many
years ago as a method to product applications to run on both Microsoft
Windows and Unix X Window systems. It also was to have a Macintosh
port as well but this never eventuated. Unfortunately this package
contains no GUI code.

%description -l pl
PWLib to dosyæ du¿a biblioteka klas, która wywodzi siê ze sposobu na
tworzenie aplikacji dzia³aj±cych zarówno pod Microsoft Windows jak i
uniksowych X Window. Mia³a te¿ mieæ port na Macintosha. Ten pakiet nie
zawiera kodu GUI.

%description -l pt_BR
PWLib e uma biblioteca de classes razoavelmente grande que teve seu
inicio ha alguns anos atras como um metodo para produzir aplicacoes
para serem executadas tanto em Windows quanto em sitemas Unix baseados
em X-Window. Tambem possui um porte para Macintosh mas nunca foi
terminado. Esta versao nao contem nenhum codigo para interface.

%package devel
Summary:	Portable Windows Libary development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych pwlib
Summary(pt_BR):	Pacote de desenvolvimento para a pwlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel
Requires:	expat-devel
%{!?with_dc:Requires:	libavc1394-devel}
%{?with_dc:Requires:	libdc1394-devel}
%{!?with_dc:Requires:	libdv-devel}
Requires:	libstdc++-devel
Requires:	openldap-devel
Requires:	openssl-devel >= 0.9.7c

%description devel
Header files and libraries for developing applications that use pwlib.

%description devel -l pl
Pliki nag³ówkowe i biblioteki konieczne do rozwoju aplikacji
u¿ywaj±cych pwlib.

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

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

ln -sf make bin

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	%{!?with_dc:--enable-firewireavc} \
	%{?with_dc:--enable-firewiredc}

%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	PWLIBDIR="`pwd`" \
	PWLIBMAKEDIR="`pwd`/make" \
	OPTCCFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PWLIBDIR="`pwd`" \
	PWLIBMAKEDIR="`pwd`/make"

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/ptclib
%{_includedir}/ptlib
%{_includedir}/*.h
%{_datadir}/%{name}
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
