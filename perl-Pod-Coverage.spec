#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	Coverage
Summary:	Pod::Coverage - checks if the documentation of a module is comprehensive
Summary(pl):	Pod::Coverage - sprawdzanie kompletno¶ci dokumentacji modu³u
Name:		perl-Pod-Coverage
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12e4f06fa8411a1f5011d3e6ce3628b3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Module-Build >= 0.21-2
%if %{with tests}
BuildRequires:	perl-Devel-Symdump >= 2.01
BuildRequires:	perl-Pod-Parser >= 1.16
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a mechanism for determining if the pod for a
given module is comprehensive. It expects to find either a =head(n>1)
or an =item block documenting a subroutine.

%description -l pl
Ten modu³ udostêpnia mechamizm do okre¶lania, czy dokumentacja pod dla
danego modu³u jest kompletna. Oczekuje bloku =head(n>1) lub =item
opisuj±cego funkcjê.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	perl="%{__perl}" \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Pod/*.pm
%{perl_vendorlib}/Pod/Coverage
%{_mandir}/man3/*
