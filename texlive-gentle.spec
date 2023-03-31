Name:		texlive-gentle
Version:	15878
Release:	2
Summary:	A Gentle Introduction to TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/gentle
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentle.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
