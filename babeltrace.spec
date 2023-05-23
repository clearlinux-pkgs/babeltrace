#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x5F1B2A0789F12B11 (jeremie.galarneau@gmail.com)
#
Name     : babeltrace
Version  : 2.0.5
Release  : 9
URL      : https://www.efficios.com/files/babeltrace/babeltrace2-2.0.5.tar.bz2
Source0  : https://www.efficios.com/files/babeltrace/babeltrace2-2.0.5.tar.bz2
Source1  : https://www.efficios.com/files/babeltrace/babeltrace2-2.0.5.tar.bz2.asc
Summary  : Babeltrace 2 library to support plugins and create trace processing graphs
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1 MIT
Requires: babeltrace-bin = %{version}-%{release}
Requires: babeltrace-lib = %{version}-%{release}
Requires: babeltrace-license = %{version}-%{release}
Requires: babeltrace-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : elfutils-dev
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
// Render with Asciidoctor
= Babeltrace
13 April 2020
:btversion: 2.0
:bt2: Babeltrace{nbsp}2

%package bin
Summary: bin components for the babeltrace package.
Group: Binaries
Requires: babeltrace-license = %{version}-%{release}

%description bin
bin components for the babeltrace package.


%package dev
Summary: dev components for the babeltrace package.
Group: Development
Requires: babeltrace-lib = %{version}-%{release}
Requires: babeltrace-bin = %{version}-%{release}
Provides: babeltrace-devel = %{version}-%{release}
Requires: babeltrace = %{version}-%{release}

%description dev
dev components for the babeltrace package.


%package doc
Summary: doc components for the babeltrace package.
Group: Documentation
Requires: babeltrace-man = %{version}-%{release}

%description doc
doc components for the babeltrace package.


%package lib
Summary: lib components for the babeltrace package.
Group: Libraries
Requires: babeltrace-license = %{version}-%{release}

%description lib
lib components for the babeltrace package.


%package license
Summary: license components for the babeltrace package.
Group: Default

%description license
license components for the babeltrace package.


%package man
Summary: man components for the babeltrace package.
Group: Default

%description man
man components for the babeltrace package.


%prep
%setup -q -n babeltrace2-2.0.5
cd %{_builddir}/babeltrace2-2.0.5
pushd ..
cp -a babeltrace2-2.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684879300
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1684879300
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/babeltrace
cp %{_builddir}/babeltrace2-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/babeltrace/abdc08b736a74c3b8b56d8207ff8485b9da43d99 || :
cp %{_builddir}/babeltrace2-%{version}/mit-license.txt %{buildroot}/usr/share/package-licenses/babeltrace/896db08d9336fddb884ddd3994bd28993200ea1a || :
cp %{_builddir}/babeltrace2-%{version}/tests/utils/python/tap/LICENSE %{buildroot}/usr/share/package-licenses/babeltrace/e661ed4d57c95a6a4c29762570e79eff50f12fd8 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/babeltrace2
/usr/bin/babeltrace2

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libbabeltrace2-ctf-writer.so
/V3/usr/lib64/libbabeltrace2.so
/usr/include/babeltrace2-ctf-writer/clock-class.h
/usr/include/babeltrace2-ctf-writer/clock.h
/usr/include/babeltrace2-ctf-writer/event-fields.h
/usr/include/babeltrace2-ctf-writer/event-types.h
/usr/include/babeltrace2-ctf-writer/event.h
/usr/include/babeltrace2-ctf-writer/field-types.h
/usr/include/babeltrace2-ctf-writer/fields.h
/usr/include/babeltrace2-ctf-writer/object.h
/usr/include/babeltrace2-ctf-writer/stream-class.h
/usr/include/babeltrace2-ctf-writer/stream.h
/usr/include/babeltrace2-ctf-writer/trace.h
/usr/include/babeltrace2-ctf-writer/types.h
/usr/include/babeltrace2-ctf-writer/utils.h
/usr/include/babeltrace2-ctf-writer/visitor.h
/usr/include/babeltrace2-ctf-writer/writer.h
/usr/include/babeltrace2/babeltrace.h
/usr/include/babeltrace2/error-reporting.h
/usr/include/babeltrace2/func-status.h
/usr/include/babeltrace2/graph/component-class-dev.h
/usr/include/babeltrace2/graph/component-class.h
/usr/include/babeltrace2/graph/component-descriptor-set.h
/usr/include/babeltrace2/graph/component.h
/usr/include/babeltrace2/graph/connection.h
/usr/include/babeltrace2/graph/graph.h
/usr/include/babeltrace2/graph/interrupter.h
/usr/include/babeltrace2/graph/message-iterator-class.h
/usr/include/babeltrace2/graph/message-iterator.h
/usr/include/babeltrace2/graph/message.h
/usr/include/babeltrace2/graph/port.h
/usr/include/babeltrace2/graph/private-query-executor.h
/usr/include/babeltrace2/graph/query-executor.h
/usr/include/babeltrace2/graph/self-component-class.h
/usr/include/babeltrace2/graph/self-component-port.h
/usr/include/babeltrace2/graph/self-component.h
/usr/include/babeltrace2/graph/self-message-iterator.h
/usr/include/babeltrace2/integer-range-set.h
/usr/include/babeltrace2/logging-defs.h
/usr/include/babeltrace2/logging.h
/usr/include/babeltrace2/plugin/plugin-dev.h
/usr/include/babeltrace2/plugin/plugin-loading.h
/usr/include/babeltrace2/trace-ir/clock-class.h
/usr/include/babeltrace2/trace-ir/clock-snapshot.h
/usr/include/babeltrace2/trace-ir/event-class.h
/usr/include/babeltrace2/trace-ir/event.h
/usr/include/babeltrace2/trace-ir/field-class.h
/usr/include/babeltrace2/trace-ir/field-path.h
/usr/include/babeltrace2/trace-ir/field.h
/usr/include/babeltrace2/trace-ir/packet.h
/usr/include/babeltrace2/trace-ir/stream-class.h
/usr/include/babeltrace2/trace-ir/stream.h
/usr/include/babeltrace2/trace-ir/trace-class.h
/usr/include/babeltrace2/trace-ir/trace.h
/usr/include/babeltrace2/types.h
/usr/include/babeltrace2/util.h
/usr/include/babeltrace2/value.h
/usr/include/babeltrace2/version.h
/usr/lib64/libbabeltrace2-ctf-writer.so
/usr/lib64/libbabeltrace2.so
/usr/lib64/pkgconfig/babeltrace2-ctf-writer.pc
/usr/lib64/pkgconfig/babeltrace2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/babeltrace2/CONTRIBUTING.adoc
/usr/share/doc/babeltrace2/ChangeLog
/usr/share/doc/babeltrace2/LICENSE
/usr/share/doc/babeltrace2/README.adoc
/usr/share/doc/babeltrace2/gpl-2.0.txt
/usr/share/doc/babeltrace2/lgpl-2.1.txt
/usr/share/doc/babeltrace2/mit-license.txt
/usr/share/doc/babeltrace2/std-ext-lib.txt

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/babeltrace2/plugins/babeltrace-plugin-ctf.so
/V3/usr/lib64/babeltrace2/plugins/babeltrace-plugin-lttng-utils.so
/V3/usr/lib64/babeltrace2/plugins/babeltrace-plugin-text.so
/V3/usr/lib64/babeltrace2/plugins/babeltrace-plugin-utils.so
/V3/usr/lib64/libbabeltrace2-ctf-writer.so.0
/V3/usr/lib64/libbabeltrace2-ctf-writer.so.0.0.0
/V3/usr/lib64/libbabeltrace2.so.0
/V3/usr/lib64/libbabeltrace2.so.0.0.0
/usr/lib64/babeltrace2/plugins/babeltrace-plugin-ctf.so
/usr/lib64/babeltrace2/plugins/babeltrace-plugin-lttng-utils.so
/usr/lib64/babeltrace2/plugins/babeltrace-plugin-text.so
/usr/lib64/babeltrace2/plugins/babeltrace-plugin-utils.so
/usr/lib64/libbabeltrace2-ctf-writer.so.0
/usr/lib64/libbabeltrace2-ctf-writer.so.0.0.0
/usr/lib64/libbabeltrace2.so.0
/usr/lib64/libbabeltrace2.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/babeltrace/896db08d9336fddb884ddd3994bd28993200ea1a
/usr/share/package-licenses/babeltrace/abdc08b736a74c3b8b56d8207ff8485b9da43d99
/usr/share/package-licenses/babeltrace/e661ed4d57c95a6a4c29762570e79eff50f12fd8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/babeltrace2-convert.1
/usr/share/man/man1/babeltrace2-help.1
/usr/share/man/man1/babeltrace2-list-plugins.1
/usr/share/man/man1/babeltrace2-query.1
/usr/share/man/man1/babeltrace2-run.1
/usr/share/man/man1/babeltrace2.1
/usr/share/man/man7/babeltrace2-filter.lttng-utils.debug-info.7
/usr/share/man/man7/babeltrace2-filter.utils.muxer.7
/usr/share/man/man7/babeltrace2-filter.utils.trimmer.7
/usr/share/man/man7/babeltrace2-intro.7
/usr/share/man/man7/babeltrace2-plugin-ctf.7
/usr/share/man/man7/babeltrace2-plugin-lttng-utils.7
/usr/share/man/man7/babeltrace2-plugin-text.7
/usr/share/man/man7/babeltrace2-plugin-utils.7
/usr/share/man/man7/babeltrace2-query-babeltrace.support-info.7
/usr/share/man/man7/babeltrace2-query-babeltrace.trace-infos.7
/usr/share/man/man7/babeltrace2-sink.ctf.fs.7
/usr/share/man/man7/babeltrace2-sink.text.details.7
/usr/share/man/man7/babeltrace2-sink.text.pretty.7
/usr/share/man/man7/babeltrace2-sink.utils.counter.7
/usr/share/man/man7/babeltrace2-sink.utils.dummy.7
/usr/share/man/man7/babeltrace2-source.ctf.fs.7
/usr/share/man/man7/babeltrace2-source.ctf.lttng-live.7
/usr/share/man/man7/babeltrace2-source.text.dmesg.7
