%include	/usr/lib/rpm/macros.perl
Summary:	Business-ISSN perl module
Summary(pl):	Modu³ perla Business-ISSN
Name:		perl-Business-ISSN
Version:	0.90
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Business/Business-ISSN-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business-ISSN - work with International Standard Serial Numbers.

%description -l pl
Business-ISSN - modu³ umo¿liwiaj±cy pracê z ISSN (International
Standard Serial Numbers).

%prep
%setup -q -n Business-ISSN-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf readme Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Business/ISSN.pm
%{_mandir}/man3/*
