%define major 5
%define libname %mklibname KF5Archive %{major}
%define devname %mklibname KF5Archive -d
%define debug_package %{nil}

Name: karchive
Version: 4.95.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 archiving library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qmake5
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(zlib)

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

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_prefix}/mkspecs
%{_libdir}/cmake/KF5Archive
