Name:		texlive-mattens
Version:	62326
Release:	2
Summary:	Matrices/tensor typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mattens
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/mattens
%doc %{_texmfdistdir}/doc/latex/mattens
#- source
%doc %{_texmfdistdir}/source/latex/mattens

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
