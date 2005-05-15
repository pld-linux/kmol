Summary:	KMol - a molecular weight and elemental composition calculator
Summary(pl):	KMol - kalkulator do liczenia wagi cz±stek i zwi±zków
Name:		kmol
Version:	0.3.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	http://www.idiom.com/~tomi/%{name}-%{version}.tar.bz2
# Source0-md5:	7efb66b84e5424b959549703aa61cca0
Source1:        http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	81e0b2f79ef76218381270960ac0f55f
URL:		http://www.idiom.com/~tomi/kmol.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -a1

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}


mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Applications,%{_desktopdir}}/kmol.desktop
echo "Categories=Qt;KDE;Education;Science;Chemistry;" >> $RPM_BUILD_ROOT%{_desktopdir}/kmol.desktop
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kmol
%{_desktopdir}/kmol.desktop
%{_iconsdir}/*/*/apps/*.png
