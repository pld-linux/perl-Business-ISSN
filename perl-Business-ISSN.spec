#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Business
%define		pnam	ISSN
Summary:	Business::ISSN - Perl extension for International Standard Serial Numbers
Summary(pl.UTF-8):	Business::ISSN - rozszerzenie Perla do obsługi numerów ISSN
Name:		perl-Business-ISSN
Version:	0.91
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1f609422d3a0ad5e301ae694d142fe4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business::ISSN - work with International Standard Serial Numbers.

%description -l pl.UTF-8
Business::ISSN to moduł Perla umożliwiający pracę z ISSN
(International Standard Serial Numbers).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Business/ISSN.pm
%{_mandir}/man3/*
