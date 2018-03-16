Summary:	xmessage application - display a message or query in a window
Summary(pl.UTF-8):	Aplikacja xmessage - wyświetlanie komunikatu lub zapytania w oknie
Name:		xorg-app-xmessage
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xmessage-%{version}.tar.bz2
# Source0-md5:	e50ffae17eeb3943079620cb78f5ce0b
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xmessage program displays a window containing a message from the
command line, a file, or standard input. Along the lower edge of the
message is row of buttons; clicking the left mouse button on any of
these buttons will cause xmessage to exit. Which button was pressed is
returned in the exit status and, optionally, by writing the label of
the button to standard output.

%description -l pl.UTF-8
Program xmessage wyświetla okienko zawierające komunikat z linii
poleceń, pliku lub standardowego wejścia. Wzdłuż dolnej krawędzi
komunikatu znajduje się wiersz przycisków; kliknięcie lewym klawiszem
myszy na dowolnym z przycisków powoduje zakończenie xmessage, To,
który przycisk został wciśnięty, jest zwracane w kodzie wyjścia oraz,
opcjonalnie, poprzez wypisanie etykiety przycisku na standardowym
wyjściu.

%prep
%setup -q -n xmessage-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xmessage
%{_datadir}/X11/app-defaults/Xmessage*
%{_mandir}/man1/xmessage.1*
