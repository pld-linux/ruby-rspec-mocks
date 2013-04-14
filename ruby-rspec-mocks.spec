#
# Conditional build:
%bcond_with	tests		# build without tests
# test needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core

%define	gem_name	rspec-mocks
Summary:	Rspec-2 doubles (mocks and stubs)
Name:		ruby-%{gem_name}
Version:	2.13.1
Release:	0.1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
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

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
ruby -rubygems -Ilib/ -S rspec spec/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

# cleanups
rm -f $RPM_BUILD_ROOT%{gem_instdir}/{.document,.gitignore,.travis.yml,.yardopts}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changelog.md License.txt
%{ruby_vendorlibdir}/rspec/mocks.rb
%{ruby_vendorlibdir}/rspec/mocks
%dir %{ruby_vendorlibdir}/spec
%{ruby_vendorlibdir}/spec/mocks.rb

%if 0
%files	doc
%defattr(644,root,root,755)
%endif
