#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Simple DirectMedia Layer Perl
Summary(pl):	Interfejs Simple DirectMedia Layer dla Perla
Name:		perl-SDL
Version:	2.1.0
Release:	0.1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DG/DGOEHRIG/SDL_Perl-%{version}.tar.gz
# Source0-md5:	7dc4ab6620003f37ff4093d052ed46fa
Patch0:		%{name}-detection.patch
URL:		http://search.cpan.org/dist/SDL_Perl/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel >= 2.0.10
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	smpeg-devel
Provides:	perl(SDL::OpenGL)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL_perl is a package of perl modules that provides both functional
and object orient interfaces to the Simple DirectMedia Layer for Perl
5. This package does take some liberties with the SDL API, and
attempts to adhere to the spirit of both the SDL and Perl.

%description -l pl
SDL_perl to pakiet z modu³ami perla udostêpniaj±cy z poziomu Perla
interfejsy zarówno funkcjonalne, jak i zorientowane obiektowo do
biblioteki SDL (Simple DirectMedia Layer). Pakiet przejmuje trochê
swobody z API SDL i próbuje siê dopasowaæ do idei SDL oraz Perla.

%prep
%setup -q -n SDL_Perl-%{version}
%patch0 -p1

%build
%{__perl} Build.PL
./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG TODO README
%{_mandir}/man3/*
%{perl_vendorarch}/SDL*.pm
%{perl_vendorarch}/SDL
%dir %{perl_vendorarch}/auto/SDL
%{perl_vendorarch}/auto/SDL/autosplit.ix
%dir %{perl_vendorarch}/auto/SDL_perl
%{perl_vendorarch}/auto/SDL_perl/SDL_perl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SDL_perl/SDL_perl.so
