# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/nih
# catalog-date 2007-03-10 12:31:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-nih
Version:	20070310
Release:	1
Summary:	A class for NIH grant applications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nih
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nih.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nih.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The nih class offers support for grant applications to NIH, the
National Institutes of Health, a US government agency. The
example-* files provide a template for using nih.cls and
submitting the biographical sketches the NIH wants. They
(potentially) use denselists package, which just reduces list
spacing; the package is distributed with the class, but is not
part of the class proper. (The examples may be distributed
without even the restrictions of the LaTeX licence.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nih/denselists.sty
%{_texmfdistdir}/tex/latex/nih/nih.cls
%doc %{_texmfdistdir}/doc/latex/nih/README
%doc %{_texmfdistdir}/doc/latex/nih/example-biosketch.pdf
%doc %{_texmfdistdir}/doc/latex/nih/example-biosketch.tex
%doc %{_texmfdistdir}/doc/latex/nih/example-nih-cls.pdf
%doc %{_texmfdistdir}/doc/latex/nih/example-nih-cls.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
