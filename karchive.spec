%define major 5
%define libname %mklibname KF5Archive %{major}
%define devname %mklibname KF5Archive -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		karchive
Version:	5.59.0
Release:	1
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary:	The KDE Frameworks 5 archiving library
URL:		http://kde.org/
License: 	LGPL
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(zlib)
# For QCH format docs
BuildRequires: qt5-assistant
BuildRequires: doxygen

%description
The KDE Frameworks 5 archiving library.

KArchive can read and decompress all common archive formats.

%package -n %{libname}
Summary: The KDE Frameworks 5 archiving library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 archiving library.

KArchive can read and decompress all common archive formats.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_sysconfdir}/xdg/karchive.categories

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs
%{_libdir}/cmake/KF5Archive

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
