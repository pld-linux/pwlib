Summary:	Portable Windows Libary
Name:		pwlib
Version:	1.1pl19
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://www.openh323.org/bin/%{name}_min_%{version}.tar.gz
Patch0:		pwlib-mak_files.patch
Patch1:		pwlib-libname.patch
Patch2:		pwlib-asnparser.patch
URL:		http://www.openh323.org/
BuildRequires:	gcc-c++
BuildRequires:	libstdc++-devel
BuildRequires:	bison
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
PWLib is a moderately large class library that has its genesis many years ago asa method to product applications to run on both Microsoft Windows and Unix
X-Windows systems. It also was to have a Macintosh port as well but this never
eventuated.
Unfortunately this package contains no GUI code.

%package devel
Summary:	Portable Windows Libary development files
Summary(pl):	Pliki dla developerów pwlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and libraries for developing applications that use pwlib.

%description -l pl devel
Pliki nag³ówkowe i biblioteki konieczne do rozwoju aplikacji
u¿ywaj±cych pwlib.

%package static
Summary:	Portable Windows Libary static libraries
Summary(pl):	Biblioteki statyczne pwlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
pwlib static libraries.

%description -l pl static
Biblioteki statyczne pwlib.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
PWLIBDIR=`pwd`; export PWLIBDIR
PWLIB_BUILD="yes"; export PWLIB_BUILD
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
		OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS}"
%{__make} %{?debug:debugnoshared}%{!?debug:optnoshared} \
		OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS}"

cd tools/asnparser
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
		OPTCCFLAGS="%{!?debug:$RPM_OPT_FLAGS}"

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
install tools/asnparser/obj_linux_x86_?/asnparser $RPM_BUILD_ROOT%{_bindir}

cd make
for l in *.mak ; do
	sed -e's/@prefix@/%{_prefix}/' \
	    -e's/@makdir@/%{_datadir}\/pwlib/' \
		< $l > $RPM_BUILD_ROOT%{_datadir}/%{name}/$l
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
