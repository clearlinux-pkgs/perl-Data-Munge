#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Munge
Version  : 0.097
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Data-Munge-0.097.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Data-Munge-0.097.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-munge-perl/libdata-munge-perl_0.097-1.debian.tar.xz
Summary  : 'various utility functions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Munge-license = %{version}-%{release}
Requires: perl-Data-Munge-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Warnings)

%description
Data-Munge
Various utility functions.
INSTALLATION
To install this module, run the following commands:

%package dev
Summary: dev components for the perl-Data-Munge package.
Group: Development
Provides: perl-Data-Munge-devel = %{version}-%{release}
Requires: perl-Data-Munge = %{version}-%{release}

%description dev
dev components for the perl-Data-Munge package.


%package license
Summary: license components for the perl-Data-Munge package.
Group: Default

%description license
license components for the perl-Data-Munge package.


%package perl
Summary: perl components for the perl-Data-Munge package.
Group: Default
Requires: perl-Data-Munge = %{version}-%{release}

%description perl
perl components for the perl-Data-Munge package.


%prep
%setup -q -n Data-Munge-0.097
cd %{_builddir}
tar xf %{_sourcedir}/libdata-munge-perl_0.097-1.debian.tar.xz
cd %{_builddir}/Data-Munge-0.097
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Munge-0.097/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Munge
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Munge/5ec2f36a161275bf005607e23fbbec236aab67b1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Munge.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Munge/5ec2f36a161275bf005607e23fbbec236aab67b1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Data/Munge.pm
