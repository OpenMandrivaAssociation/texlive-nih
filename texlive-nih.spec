%global tl_name nih
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A class for NIH grant applications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nih
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nih.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nih.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The nih class offers support for grant applications to NIH, the National
Institutes of Health, a US government agency. The example-* files
provide a template for using nih.cls and submitting the biographical
sketches the NIH wants. They (potentially) use denselists package, which
just reduces list spacing; the package is distributed with the class,
but is not part of the class proper. (The examples may be distributed
without even the restrictions of the LaTeX licence.)

