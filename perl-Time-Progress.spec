#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Time
%define		pnam	Progress
%include	/usr/lib/rpm/macros.perl
Summary:	Time::Progress - Elapsed and estimated finish time reporting
Summary(pl.UTF-8):	Time::Progress - informowanie o minionym i oczekiwanym czasie zakończenia operacji
Name:		perl-Time-Progress
Version:	1.5
Release:	2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fd355af4abcdf2408a829810c797202e
URL:		http://search.cpan.org/dist/Time-Progress/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::Progress reports elapsed and estimated finish time. Shortest
time interval that can be measured is 1 second (This should be fixed
in the future perhaps).

%description -l pl.UTF-8
Time::Progress informuje o mimionym i oczekiwanym czasie zakończenia
operacji. Najkrótszy mierzony czas to 1 sekunda (być może zostanie to
poprawione w przyszłości).

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
%doc Changes README
%{_mandir}/man3/Time::Progress.3pm*
%{perl_vendorlib}/Time/Progress.pm
