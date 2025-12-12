# Maintainer: Your Name <youremail@example.com>
pkgname=numscript
pkgver=1.0.0
pkgrel=1
pkgdesc="NumScript: a Python virtual machine shell"
arch=('any')
url="https://github.com/skirexwastaken/numscript-aur"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
# Define a variable for the extracted source directory name (optional but clean)
_name=NumScript-AUR

source=("https://github.com/skirexwastaken/numscript-aur/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')  # Replace with real checksum for production

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

