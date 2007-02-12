Summary:	Window Maker memory/swap/IO/uptime/ints monitor
Summary(pl.UTF-8):	Monitor systemu dla WindowMakera
Name:		asmon
Version:	0.60
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/files/%{name}-%{version}.tar.gz
# Source0-md5:	781d273283b307b5089afbfa6aa35f18
URL:		http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/sys.html#asmon
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system monitor for Linux that monitors CPU usage, memory usage, load
average, and uptime.

%description -l pl.UTF-8
Monitor systemu dla WindowMakera. Monitoruje użycie procesora,
pamięci, obciążenie systemu, oraz podaje uptime.

%prep
%setup -q

%build
%{__make} -C asmon \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install asmon/asmon $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/asmon
