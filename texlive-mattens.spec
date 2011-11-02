Name:		texlive-mattens
Version:	1.3
Release:	1
Summary:	Matrices/tensor typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mattens
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The mattens package contains the definitions to typeset
matrices, vectors and tensors as used in the engineering
community for the representation of common vectors and tensors
such as forces, velocities, moments of inertia, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
