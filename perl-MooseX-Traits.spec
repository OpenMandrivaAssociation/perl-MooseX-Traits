%define module   MooseX-Traits
%define version    0.06
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Automatically apply roles at object creation time
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::use::ok)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Often you want to create components that can be added to a class
arbitrarily. This module makes it easy for the end user to use these
components. Instead of requiring the user to create a named class with the
desired roles applied, or applying roles to the instance one-by-one, he can
just pass a 'traits' parameter to the class's 'new_with_traits'
constructor. This role will then apply the roles in one go, cache the
resulting class (for efficiency), and return a new instance. Arguments
meant to initialize the applied roles' attributes can also be passed to the
constructor.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


