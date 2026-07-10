%global tl_name gentle
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Gentle Introduction to TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/gentle
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gentle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gentle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The "Gentle Introduction" is the longest-established comprehensive free
tutorial on the use of plain TeX.

