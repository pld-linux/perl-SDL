#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	SDL Perl module
Summary(cs):	Modul SDL pro Perl
Summary(da):	Perlmodul SDL
Summary(de):	SDL Perl Modul
Summary(es):	Módulo de Perl SDL
Summary(fr):	Module Perl SDL
Summary(it):	Modulo di Perl SDL
Summary(ja):	SDL Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	SDL ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul SDL
Summary(pl):	Modu³ Perla SDL
Summary(pt):	Módulo de Perl SDL
Summary(pt_BR):	Módulo Perl SDL
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl SDL
Summary(sv):	SDL Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl SDL
Summary(zh_CN):	SDL Perl Ä£¿é
Name:		perl-SDL
Version:	1.20.0
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://sdlperl.org/SDL_perl/SDL_perl-%{version}.tar.gz
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
%{__make} OPTIMIZE="%{rpmcflags} -I/usr/X11R6/include"

%{!?_without_tests:%{__make} test}

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
%dir %{perl_sitearch}/auto/SDL_perl
%{perl_sitearch}/auto/SDL_perl/SDL_perl.bs
%{perl_sitearch}/auto/SDL/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/SDL_perl/SDL_perl.so
