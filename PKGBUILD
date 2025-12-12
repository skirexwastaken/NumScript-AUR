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
    # Enter the extracted source directory
    cd "$srcdir"/$_name-$pkgver
    
    # Run the standard setuptools build process
    python setup.py build
}

package() {
    # Enter the extracted source directory
    cd "$srcdir"/$_name-$pkgver
    
    # Install the built package into the staging directory ($pkgdir).
    # The --root="$pkgdir" flag correctly tells setuptools to install 
    # the files into the fakeroot environment, and handles creating 
    # the 'numscript' executable based on your setup.py entry point.
    python setup.py install --root="$pkgdir" --optimize=1
}
