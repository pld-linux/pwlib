Summary:	Portable Windows Libary
Summary(pl):	Przeno∂na biblioteka okienkowa
Name:		pwlib
Version:	1.2.11
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
Patch1:		%{name}-libname.patch
Patch2:		%{name}-asnparser.patch
Patch3:		%{name}-116.patch
URL:		http://www.openh323.org/
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
PWLib is a moderately large class library that has its genesis many
years ago as a method to product applications to run on both Microsoft
Windows and Unix X Window systems. It also was to have a Macintosh
port as well but this never eventuated. Unfortunately this package
contains no GUI code.

%description -l pl
PWLib to dosyÊ duøa biblioteka klas, ktÛra wywodzi siÍ ze sposobu na
tworzenie aplikacji dzia≥aj±cych zarÛwno pod Microsoft Windows jak i
uniksowych X Window. Mia≥a teø mieÊ port na Macintosha. Ten pakiet nie
zawiera kodu GUI.

%package devel
Summary:	Portable Windows Libary development files
Summary(pl):	Pliki dla developerÛw pwlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	openssl-devel
Requires:	expat-devel

%description devel
Header files and libraries for developing applications that use pwlib.

%description devel -l pl
Pliki nag≥Ûwkowe i biblioteki konieczne do rozwoju aplikacji
uøywaj±cych pwlib.

%package static
Summary:	Portable Windows Libary static libraries
Summary(pl):	Biblioteki statyczne pwlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

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

%build
# it still ignores CC and CXX
CC="%{__cc}"; export CC
%{?__cxx:CXX="%{__cc}"; export CXX}

PWLIBDIR=`pwd`; export PWLIBDIR
PWLIB_BUILD="yes"; export PWLIB_BUILD
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS} -fno-rtti -fno-exceptions" \
	EXTLIBS="-lstdc++ -lexpat"

%{__make} %{?debug:debugnoshared}%{!?debug:optnoshared} \
	OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS} -fno-rtti -fno-exceptions"

%{__make} -C tools/asnparser \
	%{?debug:debugshared}%{!?debug:optshared} \
	OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/{ptclib,ptlib/unix/ptlib},%{_bindir},%{_datadir}/%{name}}

#using cp as install won't preserve links
cp -d lib/lib* $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}
install include/ptclib/*.h $RPM_BUILD_ROOT%{_includedir}/ptclib
install include/ptlib/*.h $RPM_BUILD_ROOT%{_includedir}/ptlib
install include/ptlib/*.inl $RPM_BUILD_ROOT%{_includedir}/ptlib
install include/ptlib/unix/ptlib/*.h $RPM_BUILD_ROOT%{_includedir}/ptlib/unix/ptlib
install include/ptlib/unix/ptlib/*.inl $RPM_BUILD_ROOT%{_includedir}/ptlib/unix/ptlib
install tools/asnparser/obj_linux_*/asnparser $RPM_BUILD_ROOT%{_bindir}

cd make
for l in *.mak ; do
	sed -e 's#@prefix@#%{_prefix}#' \
	    -e 's#@makdir@#%{_datadir}/pwlib#' \
		< $l > $RPM_BUILD_ROOT%{_datadir}/%{name}/$l
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
