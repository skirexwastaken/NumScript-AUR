pkgname=numscript
pkgver=1.0.0
pkgrel=1
pkgdesc="NumScript: a lightweight, esoteric, interpreted scripting language designed for numeric programming."
arch=('any')
url="https://github.com/skirexwastaken/numscript-aur"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')

# Git source for the repo
source=("git+https://github.com/skirexwastaken/numscript-aur.git")
sha256sums=('SKIP')  # Git sources are not hashed

build() {
    cd "$srcdir/numscript-aur"  # git sources clone into this folder
    rm -f pyproject.toml
    python setup.py build
}

package() {
    cd "$srcdir/numscript-aur"
    python setup.py install --root="$pkgdir" --optimize=1
}
