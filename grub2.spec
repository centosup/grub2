%define install_prefix /opt/%name
Name: grub2
Version: 2.00
Release: 1%{?dist}
Summary: Bootloader with support for Linux, Multiboot and more

Group: System Environment/Base
License: GPLv3+
URL: http://www.gnu.org/software/grub/

Source: ftp://ftp.gnu.org/gnu/grub/grub-%{version}.tar.xz

BuildRequires: autoconf automake bison flex

%ifarch %{sparc} x86_64
BuildRequires: /usr/lib64/crt1.o glibc-static
%else
BuildRequires: /usr/lib/crt1.o glibc-static
%endif
Requires(pre): dracut
Requires(post): dracut

%description
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich variety of kernel formats,
file systems, computer architectures and hardware devices

%prep
%setup -q -n grub-2.00

%build
export LDFLAGS="$LDFLAGS -Wl,--build-id"
./configure --prefix=%{install_prefix}
make

%install
%make_install

%files
%defattr(-,root,root)
%{install_prefix}

%changelog
* Sun Nov 14 2016 CentOS Up repo <centosup@centosup.ispsystem.info> - 2.0.0-1
- First minimal release for CentOS 6.x
