#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Simple DirectMedia Layer Perl
Summary(pl):	Interfejs Simple DirectMedia Layer dla Perla
Name:		perl-SDL
Version:	1.20.0
Release:	4
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://sdlperl.org/SDL_perl/SDL_perl-%{version}.tar.gz
# Source0-md5:	041617aec124677083ecef04aa48f927
Patch0:		%{name}-detection.patch
URL:		http://sdlperl.org/
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
%setup -q -n SDL_perl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags} -I/usr/X11R6/include"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG TODO README
%{_mandir}/man3/*
%{perl_vendorarch}/SDL*
%dir %{perl_vendorarch}/auto/SDL_perl
%{perl_vendorarch}/auto/SDL_perl/SDL_perl.bs
%{perl_vendorarch}/auto/SDL/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/SDL_perl/SDL_perl.so
