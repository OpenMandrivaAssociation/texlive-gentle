# revision 15878
# category Package
# catalog-ctan /info/gentle
# catalog-date 2009-01-04 11:16:40 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-gentle
Version:	20090104
Release:	2
Summary:	A Gentle Introduction to TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/gentle
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The "Gentle Introduction" is the longest-established
comprehensive free tutorial on the use of plain TeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/gentle/gentle.pdf
%doc %{_texmfdistdir}/doc/plain/gentle/gentle.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
