%define		pkg	read
Summary:	read(1) for node programs
Name:		nodejs-%{pkg}
Version:	1.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	9f7521de8702223073b412f69a81ff24
URL:		https://github.com/isaacs/read
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.8.0
Requires:	nodejs-mute-stream < 0.0.5
Requires:	nodejs-mute-stream >= 0.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
read(1) for node programs.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib rs.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
