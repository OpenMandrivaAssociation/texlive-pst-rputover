Name:		texlive-pst-rputover
Version:	44724
Release:	1
Summary:	Place text over objects without obscuring background colors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-rputover
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-rputover.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-rputover.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks package which allows to place text over
objects without obscuring background colors.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-rputover
%{_texmfdistdir}/tex/generic/pst-rputover
%doc %{_texmfdistdir}/doc/generic/pst-rputover

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
