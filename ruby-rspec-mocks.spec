#
# Conditional build:
%bcond_with	tests		# unit tests [not present when repackaging .gem file]
# test needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core

%define	pkgname	rspec-mocks
Summary:	Rspec-2 doubles (mocks and stubs)
Summary(pl.UTF-8):	Pary Rspec-2 (atrapy i zaślepki)
Name:		ruby-%{pkgname}
Version:	3.7.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	b4b2393b550a520f6fa2c713b74a6f43
URL:		http://github.com/rspec/rspec-mocks
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby >= 1:1.8.7
%if %{with tests}
BuildRequires:	ruby-minitest >= 5.2
BuildRequires:	ruby-rspec-support >= 3.7.0
%endif
# .gemspec contains: s.add_dependency(%q<diff-lcs>.freeze, ["< 2.0", ">= 1.2.0"])
# but only "rubygems(diff-lcs) < 2.0" is detected, "rubygems(diff-lcs) >= 1.2.0" not...
Requires:	ruby-diff-lcs >= 1.2.0
Requires:	ruby-diff-lcs < 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rspec-mocks provides a test-double framework for rspec including
support for method stubs, fakes, and message expectations.

%description -l pl.UTF-8
rspec-mocks dostarcza szkielet pary testowej dla szkieletu rspec,
obejmujący obsługę zaślepek metod, atrapy oraz oczekiwania
komunikatów.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
ruby -rubygems -Ilib/ -S rspec spec/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changelog.md LICENSE.md
%{ruby_vendorlibdir}/rspec/mocks.rb
%{ruby_vendorlibdir}/rspec/mocks
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
