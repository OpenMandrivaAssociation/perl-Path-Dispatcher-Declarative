%define upstream_name    Path-Dispatcher-Declarative
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	5

Summary:	Sugary dispatcher
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bestpractical/path-dispatcher-declarative
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SARTAK/Path-Dispatcher-Declarative-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Path::Dispatcher)
BuildRequires:	perl(Sub::Exporter)
BuildArch:	noarch

%description
the Jifty::Dispatcher manpage rocks!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/Path/

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 681744
- new version 0.03

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 541114
- import perl-Path-Dispatcher-Declarative


* Fri Apr 30 2010 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
