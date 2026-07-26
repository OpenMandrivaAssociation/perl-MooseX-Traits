%define upstream_name    MooseX-Traits
Name:		perl-%{upstream_name}
Version:	0.13
Release:	2

Summary:	Automatically apply roles at object creation time
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/moose/MooseX-Traits
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Traits-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Test::Fatal)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::autoclean)
Requires:	perl(namespace::autoclean)

BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 658863
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 552423
- update to 0.11

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 532714
- update to 0.09

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 505680
- update to 0.08

* Fri Aug 28 2009 Michael Scherer <misc@mandriva.org> 0.70.0-2mdv2010.0
+ Revision: 422011
- add missing requires, not found by autoreq as there the module is lowercase

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 420470
- adding missing buildrequires:
- update to 0.07

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 404042
- rebuild using %0.13 Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2010.0
+ Revision: 390838
- update to new version 0.06

* Tue Jun 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2010.0
+ Revision: 382297
- update to new version 0.05

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.1
+ Revision: 343969
- import perl-MooseX-Traits


* Sun Feb 22 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


