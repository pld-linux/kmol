Summary:	KMol - a molecular weight and elemental composition calculator.
#Summary(pl):
Name:		kmol
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://www.idiom.com/~tomi/%{name}-%{version}.tar.bz2
URL:		http://www.idiom.com/~tomi/kmol.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	qt-devel >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
KMol is a simple chemical calculator, which calculates molecular
weights and elemental composition of compounds given their chemical
formula.

KMol is designed to be able to parse any chemical formula that can be
unambiguously interpreted if written as a simple character sequence
(i.e., without subscript and superscript formating). If you can
understand a chemical formula, chances are KMol will understand it in
exactly the same way. If you can't, do you think it is KMol's fault?
KMol can deal with:

 - Unlimited number of nested subgroups:
   (CH3(C6H3)N(SiMe(CMe3)2))2Y(thf)2(CH(SiMe3)2).
 - Multicomponent compounds: K2SO4+Al2(SO4)3+24H2O.
 - Fractional coefficients: Cu3.14O2.72.
 - User-defined symbols, which override the global defaults.

# I don't know how to translate it human-readable 
#%description -l pl

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog INSTALL README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
#%attr(755,root,root) %{_bindir}/*
#%{_applnkdir}/Network/Communications/*.desktop
#%{_datadir}/icons/hicolor/*/*/*.png
