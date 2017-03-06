%global        uname httmock
%global        sum A mocking library for requests

Name:          python-%{uname}
Version:       1.2.6
Release:       1%{?dist}
Summary:       %{sum}

URL:           https://pypi.python.org/pypi/%{uname}
Source:        https://pypi.io/packages/source/h/%{uname}/%{uname}-%{version}.tar.gz
License:       Apache 2.0

BuildArch:     noarch

Buildrequires: python-setuptools
Buildrequires: python2-devel

Requires:      python2-requests

%description
%{sum}.

%package -n python2-%{uname}
Summary:        %{sum}

%description -n python2-%{uname}
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{uname}
%{python2_sitelib}/*

%changelog
* Mon Mar 6 2017 Nicolas Hicher <nhicher@redhat.com> 1.2.6-1
- initial package
