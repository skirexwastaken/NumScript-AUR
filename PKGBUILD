# Maintainer: Your Name <youremail@example.com>
pkgname=numscript
pkgver=1.0.0
pkgrel=1
pkgdesc="NumScript: a Python virtual machine shell"
arch=('any')
url="https://github.com/skirexwastaken/numscript-aur"
license=('MIT')
depends=('python')
makedepends=('python-pip')

source=("https://github.com/skirexwastaken/numscript-aur/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')  # Replace with real checksum for production

build() {
    cd "$srcdir"/*-$pkgver
    # No build step needed for pure Python
}

package() {
    cd "$srcdir"/*-$pkgver

    # Install Python package into $pkgdir. 
    # The --destdir and --prefix flags are crucial for correct staging.
    # This step will automatically create the 'numscript' executable 
    # in $pkgdir/usr/bin based on the 'console_scripts' entry point 
    # defined in setup.py (numscript=NumScript:main).
    python -m pip install \
        --prefix=/usr \
        --destdir="$pkgdir" \
        --no-deps \
        --ignore-installed \
        --no-cache-dir \
        .
        
    # --- MANUAL WRAPPER REMOVED ---
    # The block below is no longer needed:
    # install -Dm755 -t "$pkgdir/usr/bin" <<'EOF'
    # #!/usr/bin/env python3
    # ...
    # EOF
}
