%define upstream_name    Path-Dispatcher-Declarative
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Sugary dispatcher
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Path/%{upstream_name}-%{upstream_version}.tar.gz

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
