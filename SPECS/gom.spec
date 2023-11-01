Name:           gom
Version:        0.4
Release:        1%{?dist}
Summary:        GObject to SQLite object mapper library

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Gom
Source0:        https://download.gnome.org/sources/gom/0.4/gom-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pygobject3-devel
BuildRequires:  python3-devel

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%meson -Denable-gtk-doc=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/girepository-1.0/Gom-1.0.typelib
%{_libdir}/libgom-1.0.so.0*
%dir %{python3_sitearch}/gi
%dir %{python3_sitearch}/gi/overrides
%{python3_sitearch}/gi/overrides/*

%files devel
%{_includedir}/gom-1.0/
%{_libdir}/libgom-1.0.so
%{_libdir}/pkgconfig/gom-1.0.pc
%{_datadir}/gir-1.0/Gom-1.0.gir
%doc %{_datadir}/gtk-doc/

%changelog
* Thu Mar 19 2020 Bastien Nocera <bnocera@redhat.com> - 0.4-1
+ gom-0.4-1
- Update to 0.4
Related: rhbz#1804171

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-4
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 0.3.3-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Kalev Lember <klember@redhat.com> - 0.3.3-1
- Update to 0.3.3
- Switch to the meson build system

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Kalev Lember <klember@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.1-1
- Update to 0.3.1

* Thu Feb 19 2015 Richard Hughes <rhughes@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Mon Aug 25 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.1-1
- Initial Fedora packaging
