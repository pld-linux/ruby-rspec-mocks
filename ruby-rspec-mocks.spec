#
# Conditional build:
%bcond_without	tests		# build without tests
# test needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core

%define	pkgname	rspec-mocks
Summary:	Rspec-2 doubles (mocks and stubs)
Summary(pl.UTF-8):	Pary Rspec-2 (atrapy i zaślepki)
Name:		ruby-%{pkgname}
Version:	2.13.1
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	06ca349a77b5f95170c12005f26a0571
URL:		http://github.com/rspec/rspec-mocks
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rspec
%endif
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
%doc README.md Changelog.md License.txt
%{ruby_vendorlibdir}/rspec/mocks.rb
%{ruby_vendorlibdir}/rspec/mocks
%dir %{ruby_vendorlibdir}/spec
%{ruby_vendorlibdir}/spec/mocks.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
