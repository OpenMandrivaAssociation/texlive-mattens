%global tl_name mattens
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3b
Release:	%{tl_revision}.1
Summary:	Matrices/tensor typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mattens
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mattens.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mattens package contains the definitions to typeset matrices,
vectors and tensors as used in the engineering community for the
representation of common vectors and tensors such as forces, velocities,
moments of inertia, etc.

