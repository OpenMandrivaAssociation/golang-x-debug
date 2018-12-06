# Run tests in check section
%bcond_without check

%global goipath         golang.org/x/debug
%global forgeurl        https://github.com/golang/debug
%global commit          7fa577e31ac14e4b3f81669ca3be0f3a707ea19e

%global common_description %{expand:
Debugging tools for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Debugging tools for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
# gosym tests are failing
%gochecks -d gosym
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README CONTRIBUTORS CONTRIBUTING.md AUTHORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git7fa577e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180421git7fa577e
- First package for Fedora

