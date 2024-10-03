Summary:	XOAUTH2 plugin for Cyrus SASL
Name:		cyrus-sasl-xoauth2
Version:	0.2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/moriyoshi/cyrus-sasl-xoauth2/archive/refs/heads/master.zip
# Source0-md5:	7ffb5803e81384ba394288e633f17cc0
URL:		https://github.com/moriyoshi/cyrus-sasl-xoauth2
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libtool >= 1.4
BuildRequires:	sqlite3-devel
BuildRequires:	unzip
Requires:	cyrus-sasl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin implementation of XOAUTH2 for Cyrus SASL.

%prep
%setup -q -n %{name}-master

sed -i -e 's#^pkglibdir = ${CYRUS_SASL_PREFIX}/lib/sasl2#pkglibdir = %{_libdir}/sasl2#g' Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/libxoauth2.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/sasl2/libxoauth2.so*
