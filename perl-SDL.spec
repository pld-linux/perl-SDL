#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Simple DirectMedia Layer Perl
Summary(pl.UTF-8):	Interfejs Simple DirectMedia Layer dla Perla
Name:		perl-SDL
Version:	2.1.3
Release:	8
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DG/DGOEHRIG/SDL_Perl-%{version}.tar.gz
# Source0-md5:	6ce26e1b710ce52def4ec22637cd5176
Patch0:		%{name}-gfxPie.patch
Patch1:		%{name}-no-mixertest.patch
URL:		http://search.cpan.org/dist/SDL_Perl/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel >= 2.0.10
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-YAML
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

%description -l pl.UTF-8
SDL_perl to pakiet z modułami Perla udostępniający z poziomu Perla
interfejsy zarówno funkcjonalne, jak i zorientowane obiektowo do
biblioteki SDL (Simple DirectMedia Layer). Pakiet przejmuje trochę
swobody z API SDL i próbuje się dopasować do idei SDL oraz Perla.

%prep
%setup -q -n SDL_Perl-%{version}
%patch0 -p0
%patch1 -p1

mv t/mixerpm.t{,.blah}	# requires audio device

%build
%{__perl} Build.PL \
	installdirs=vendor \
	perl=%{__perl} \
	destdir=$RPM_BUILD_ROOT \
	config='optimize=%{rpmcflags}' \
	config='lddlflags=-shared %{rpmldflags}'
./Build

# <sigh> I don't know why but for some reason these dirs get put under
# blib/arch/auto/src instead of blib/arch/auto causing them to be installed
# in the wrong location and "./Build test" to fail. We copy them because if
# we move them the next call to ./Build will recreate them in the wrong
# location anyways. Unfortunatly with the copy the wrong located originals
# will also end up getting installed so we must remove those in %%install
cp -r blib/arch/auto/src/SDL* blib/arch/auto

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install
rm -rf $RPM_BUILD_ROOT%{perl_vendorarch}/auto/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG TODO README
%{_mandir}/man3/*
%{perl_vendorarch}/SDL*.pm
%{perl_vendorarch}/SDL
%dir %{perl_vendorarch}/auto/SDL
%dir %{perl_vendorarch}/auto/SDL_perl
%{perl_vendorarch}/auto/SDL_perl/SDL_perl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SDL_perl/SDL_perl.so
%dir %{perl_vendorarch}/auto/SDL/OpenGL
%{perl_vendorarch}/auto/SDL/OpenGL/OpenGL.bs
%attr(755,root,root)%{perl_vendorarch}/auto/SDL/OpenGL/OpenGL.so
%dir %{perl_vendorarch}/auto/SDL/SFont
%{perl_vendorarch}/auto/SDL/SFont/SFont.bs
%attr(755,root,root)%{perl_vendorarch}/auto/SDL/SFont/SFont.so
