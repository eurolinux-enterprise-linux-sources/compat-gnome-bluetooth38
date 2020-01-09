Name:		compat-gnome-bluetooth38
Epoch:		1
Version:	3.8.2.1
Release:	2%{?dist}
Summary:	Compat package with gnome-bluetooth 3.8 libraries

Group:		Applications/Communications
License:	GPLv2+
URL:		http://live.gnome.org/GnomeBluetooth
Source0:	http://download.gnome.org/sources/gnome-bluetooth/3.8/gnome-bluetooth-%{version}.tar.xz
Source1:	61-gnome-bluetooth-rfkill.rules

Patch0:		0001-lib-Fix-a-few-memory-leaks.patch
Patch1:		0002-lib-Fix-cancellation-handling.patch
Patch2:		0003-lib-Fix-extraneous-reference-that-could-lead-to-cras.patch

%if 0%{?rhel}
ExcludeArch:	s390 s390x
%endif

BuildRequires:	gtk3-devel >= 3.0
BuildRequires:	dbus-glib-devel

BuildRequires:	intltool desktop-file-utils gettext gtk-doc
BuildRequires:	itstool

BuildRequires:	gobject-introspection-devel

%description
Compatibility package with gnome-bluetooth 3.8 librarires.

%package -n compat-libgnome-bluetooth11
Summary:	Compat package with gnome-bluetooth 3.8 libraries
Group:		System Environment/Libraries
License:	LGPLv2+

%description -n compat-libgnome-bluetooth11
Compatibility package with gnome-bluetooth 3.8 librarires.

%prep
%setup -q -n gnome-bluetooth-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure --disable-desktop-update --disable-icon-update --disable-schemas-compile --disable-compile-warnings
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/
rm -rf $RPM_BUILD_ROOT%{_libdir}/libgnome-bluetooth.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/libgnome-bluetooth.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_datadir}

%post -n compat-libgnome-bluetooth11 -p /sbin/ldconfig

%postun -n compat-libgnome-bluetooth11 -p /sbin/ldconfig

%files -n compat-libgnome-bluetooth11
%doc COPYING.LIB
%{_libdir}/libgnome-bluetooth.so.*

%changelog
* Wed Apr 22 2015 Bastien Nocera <bnocera@redhat.com> 3.8.2.1-2
- Update for RHEL
Resolves: #1184211

* Fri Nov 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.8.2.1-1
- gnome-bluetooth compat package for el7-gnome-3-14 copr
