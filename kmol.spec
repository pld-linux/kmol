Summary:	KMol - a molecular weight and elemental composition calculator
Summary(pl):	KMol - kalkulator do liczenia wagi cz±stek i zwi±zków
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

%description -l pl
KMol to prosty kalkulator chemiczny, licz±cy wagi cz±steczek oraz
zwi±zków chemicznych na podstawie ich wzorów chemicznych.

KMol zosta³ tak napisany, by byæ w stanie odczytaæ ka¿dy wzór
chemiczny, który mo¿e byæ jednoznacznie zinterpretowany je¶li jest
napisany przy u¿yciu ci±gu zwyk³ych znaków (bez indeksów dolnych i
górnych). Je¶li jeste¶ w stanie zrozumieæ jaki¶ wzór, s± szanse, ¿e
KMol zrozumie go tak samo. Je¶li nie mo¿esz, czy to wina KMola?
Program radzi sobie z:
 - nieograniczon± liczb± zagnie¿d¿onych podgrup:
   (CH3(C6H3)N(SiMe(CMe3)2))2Y(thf)2(CH(SiMe3)2)
 - zwi±zkami wielosk³adnikowymi: K2SO4+Al2(SO4)3+24H2O
 - wspó³czynnikami u³amkowymi: Cu3.14O2.72
 - symbolami zdefiniowanymi przez u¿ytkownika, przykrywaj±cymi
   domy¶lne ich znaczenie.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README TODO
#%attr(755,root,root) %{_bindir}/*
#%{_applnkdir}/Network/Communications/*.desktop
#%{_pixmapsdir}/hicolor/*/*/*.png
