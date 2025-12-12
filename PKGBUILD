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
    # Use destdir instead of --root. destdir is the preferred way 
    # for installation/staging in this build context.
    # The --prefix=/usr tells pip where to put the files (e.g., in /usr/lib/python3.x/site-packages).
    python -m pip install \
        --prefix=/usr \
        --destdir="$pkgdir" \
        --no-deps \
        --ignore-installed \
        --no-cache-dir \
        .

    # Create the wrapper executable (this part was mostly correct, but moved here for clarity)
    install -Dm755 -t "$pkgdir/usr/bin" <<'EOF'
#!/usr/bin/env python3
from numscript.source.builder import NumScriptVirtualMachine

def main():
    engine = NumScriptVirtualMachine()
    try:
        engine.cli()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
EOF
}
