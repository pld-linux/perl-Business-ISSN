#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Business
%define	pnam	ISSN
Summary:	Business::ISSN - Perl extension for International Standard Serial Numbers
Summary(pl):	Business::ISSN - rozszerzenie Perla do obs�ugi numer�w ISSN
Name:		perl-Business-ISSN
Version:	0.90
Release:	9
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e221b2042c93bd134b6590e54e8ad17d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business::ISSN - work with International Standard Serial Numbers.

%description -l pl
Business::ISSN to modu� Perla umo�liwiaj�cy prac� z ISSN
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
%doc readme Changes
%{perl_vendorlib}/Business/ISSN.pm
%{_mandir}/man3/*
