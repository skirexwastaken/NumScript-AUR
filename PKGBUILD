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
sha256sums=('SKIP')

build() {
    cd "$srcdir"/*-$pkgver
    # Optional: build step if needed; otherwise can be empty
}

package() {
    cd "$srcdir"/*-$pkgver

    # Install the Python package
    python -m pip install --root="$pkgdir" --prefix=/usr --no-deps --ignore-installed .

    # Create the wrapper executable
    install -Dm755 -t "$pkgdir/usr/bin" <<'EOF'
#!/usr/bin/env python3
from source.builder import NumScriptVirtualMachine

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
