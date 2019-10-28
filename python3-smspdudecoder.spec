# Conditional build:
%bcond_with	tests	# unit tests

%define		module		smspdu
%define		egg_name	smspdudecoder
%define		pypi_name	smspdudecoder
Summary:	SMS-PDU Decoder
Name:		python3-%{pypi_name}
Version:	1.1.0
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/Qotto/smspdudecoder/archive/%{version}.tar.gz
# Source0-md5:	d76e2a506ee62364399cc3e46de41aaf
URL:		https://github.com/Qotto/smspdudecoder/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	python3-bitstring
%endif
BuildRequires:	python3-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library will help you to decode raw SMS data you can get from a
GSM modem.

It has some encoding functionality as well.

It is recommended to read GSM 03.40 to facilitate understanding.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
