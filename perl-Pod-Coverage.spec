#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	Coverage
Summary:	Pod::Coverage - Checks if the documentation of a module is comprehensive
Summary(pl):	Pod::Coverage - sprawdzanie kompletno�ci dokumentacji modu�u
Name:		perl-Pod-Coverage
Version:	0.11
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Devel-Symdump >= 2.01
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a mechanism for determining if the pod for a
given module is comprehensive. It expects to find either a =head(n>1)
or an =item block documenting a subroutine.

%description -l pl
Ten modu� udost�pnia mechamizm do okre�lania, czy dokumentacja pod dla
danego modu�u jest kompletna. Oczekuje bloku =head(n>1) lub =item
opisuj�cego funkcj�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/Pod
%{perl_vendorarch}/Pod/*.pm
%{perl_vendorarch}/Pod/Coverage
%dir %{perl_vendorarch}/auto/Pod
%dir %{perl_vendorarch}/auto/Pod/Coverage
%{perl_vendorarch}/auto/Pod/Coverage/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Pod/Coverage/*.so
%{_mandir}/man3/*
