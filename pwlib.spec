Summary:	Portable Windows Libary
Name:		pwlib
Version:	1.1pl19
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.openh323.org/bin/%{name}_min_%{version}.tar.gz
URL:		http://www.openh323.org/
BuildRequires:	XFree86-devel
BuildRequires:	gcc-c++
BuildRequires:	libstdc++-devel
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
PWLib is a moderately large class library that has its genesis many years ago asa method to product applications to run on both Microsoft Windows and Unix
X-Windows systems. It also was to have a Macintosh port as well but this never
eventuated.

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

%build
PWLIBDIR=`pwd`; export PWLIBDIR
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}{/ptclib,/ptlib},%{_bindir}}
install lib/lib* $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}
install include/ptclib/*.h $RPM_BUILD_ROOT%{_includedir}/ptclib
install include/ptlib/*.h $RPM_BUILD_ROOT%{_includedir}/ptlib
install include/ptlib/*.inl $RPM_BUILD_ROOT%{_includedir}/ptlib
install tools/asnparser/obj_linux_x86_r/asnparser $RPM_BUILD_ROOT%{_bindir}

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
%attr(755,root,root) %{_includedir}/*
%{_libdir}/*.so
%attr(755,root,root) %{_bindir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
