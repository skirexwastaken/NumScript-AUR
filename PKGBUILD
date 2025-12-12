pkgname=numscript
pkgver=1.0.0
pkgrel=1
pkgdesc="NumScript: a lightweight, esoteric, interpreted scripting language designed for numeric programming."
arch=('any')
url="https://github.com/skirexwastaken/numscript-aur"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')

source=("git+https://github.com/skirexwastaken/numscript-aur.git")
sha256sums=('SKIP')

build() {
    cd "$srcdir/numscript-aur-${pkgver}"
    rm -f pyproject.toml
    python setup.py build
}

package() {
    cd "$srcdir/numscript-aur-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize=1
    install -Dm755 -t "$pkgdir/usr/lib/python3.13/site-packages/source" source/*
}
