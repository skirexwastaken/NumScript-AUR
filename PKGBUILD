# Maintainer: Your Name <youremail@example.com>
pkgname=numscript
pkgver=1.0.0
pkgrel=1
pkgdesc="NumScript: a Python virtual machine shell"
arch=('any')
url="https://github.com/skirexwastaken/numscript-aur"
license=('MIT')
depends=('python')
# CRITICAL: We depend on setuptools to execute the setup.py script
makedepends=('python-setuptools') 

# Define a variable for the extracted source directory name (optional but clean)
_name=NumScript-AUR

source=("https://github.com/skirexwastaken/numscript-aur/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')  # Replace with real checksum for production

build() {
    cd "$srcdir"/$_name-$pkgver
    python setup.py build
}

package() {
    cd "$srcdir"/$_name-$pkgver
    
    # Install into the package directory with correct prefix
    python setup.py install --root="$pkgdir" --prefix=/usr --optimize=1
}

