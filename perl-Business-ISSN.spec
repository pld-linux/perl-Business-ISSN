%include	/usr/lib/rpm/macros.perl
%define	pdir	Business
%define	pnam	ISSN
Summary:	Business::ISSN perl module
Summary(pl):	Modu� perla Business::ISSN
Name:		perl-Business-ISSN
Version:	0.90
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business::ISSN - work with International Standard Serial Numbers.

%description -l pl
Business::ISSN - modu� umo�liwiaj�cy prac� z ISSN (International
Standard Serial Numbers).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme Changes
%{perl_sitelib}/Business/ISSN.pm
%{_mandir}/man3/*
