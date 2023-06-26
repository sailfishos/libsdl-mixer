Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: SDL2_mixer
Version: 2.6.3
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libsdl-org/SDL_mixer
License: zlib
BuildRequires: cmake
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(libmpg123)

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
mkdir -p build
pushd build
%cmake .. \
  -DSDL2MIXER_MIDI=OFF \
  -DSDL2MIXER_MOD=OFF \
  -DSDL2MIXER_OPUS=OFF
%make_build
popd

%install
pushd build
%make_install
rm -f %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/*
