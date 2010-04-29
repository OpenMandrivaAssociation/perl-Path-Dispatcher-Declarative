%define upstream_name    Path-Dispatcher-Declarative
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Sugary dispatcher
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Path/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Path::Dispatcher)
BuildRequires: perl(Sub::Exporter)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
the Jifty::Dispatcher manpage rocks!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/Path/


