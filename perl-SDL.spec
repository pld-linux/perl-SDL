%include	/usr/lib/rpm/macros.perl
Summary:	SDL perl module
Summary(pl):	Modu³ perla SDL
Name:		perl-SDL
Version:	1.18.5
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://sdlperl.org/downloads/SDL_perl-%{version}.tar.gz
Patch0:		%{name}-detection.patch
URL:		http://sdlperl.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG TODO README
%{_mandir}/man3/*
%{perl_sitearch}/SDL*
%{perl_sitearch}/auto/SDL*
