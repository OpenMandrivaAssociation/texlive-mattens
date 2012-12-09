# revision 17582
# category Package
# catalog-ctan /macros/latex/contrib/mattens
# catalog-date 2009-11-09 23:10:10 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-mattens
Version:	1.3
Release:	2
Summary:	Matrices/tensor typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mattens
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mattens package contains the definitions to typeset
matrices, vectors and tensors as used in the engineering
community for the representation of common vectors and tensors
such as forces, velocities, moments of inertia, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mattens/mattens.sty
%doc %{_texmfdistdir}/doc/latex/mattens/README
%doc %{_texmfdistdir}/doc/latex/mattens/mattens.pdf
%doc %{_texmfdistdir}/doc/latex/mattens/mattens_sample.pdf
%doc %{_texmfdistdir}/doc/latex/mattens/mattens_sample_src.zip
#- source
%doc %{_texmfdistdir}/source/latex/mattens/mattens.dtx
%doc %{_texmfdistdir}/source/latex/mattens/mattens.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 753818
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718977
- texlive-mattens
- texlive-mattens
- texlive-mattens
- texlive-mattens

