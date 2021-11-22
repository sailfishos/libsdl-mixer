Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: SDL2_mixer
Version: 2.0.4
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://www.libsdl.org/projects/SDL_mixer/
License: zlib
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(flac)

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, libmpg123 and libmad MP3 libraries.

%package devel
Summary: Simple DirectMedia Layer - Sampler Mixer Library (Development)
Requires: %{name}

%description devel
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, libmpg123 and libmad MP3 libraries.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%configure
%make_build

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
