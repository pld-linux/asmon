Summary:	Window Maker  memory/swap/IO/uptime/ints monitor
Summary(pl):	Monitor systemu dla WindowMakera
Name:		asmon
Version:	0.60
Release:	1
License:	GPL
Source0:	http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/files/%{name}-%{version}.tar.gz
URL:		http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/sys.html#asmon
Group:		X11/Window Managers/Tools
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A system monitor for Linux that monitors CPU usage, memory usage, load
average, and uptime.

%description -l pl
Monitor systemu dla WindowMakera. Monitoruje u¿ycie procesora,
pamiêci, obci±¿enie systemu, oraz podaje uptime.

%prep
%setup -q

%build
%{__make} -C asmon CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install asmon/asmon       $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/asmon
