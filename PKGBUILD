pkgname=numscript
pkgver=1.0.0
pkgrel=1
pkgdesc="NumScript: a Python virtual machine shell"
arch=('any')
url="https://github.com/skirexwastaken/numscript"
license=('MIT')
depends=('python')
makedepends=('python-pip')

source=("https://github.com/skirexwastaken/numscript-aur/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$srcdir"/*-$pkgver
    python -m pip install --prefix="$pkgdir/usr" .
}

package() {
    cd "$srcdir"/*-$pkgver
    python -m pip install --root="$pkgdir" --prefix=/usr .
}
