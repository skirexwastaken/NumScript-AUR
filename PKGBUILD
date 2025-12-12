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

# CRITICAL: Define Python version for manual installation paths
_py_ver="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

source=("https://github.com/skirexwastaken/numscript-aur/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')  # Replace with real checksum for production

build() {
    cd "$srcdir"/*-$pkgver
    # No build step needed for pure Python
}

package() {
    cd "$srcdir"/*-$pkgver

    # --- MANUAL INSTALLATION WORKAROUND ---
    # We are skipping 'pip install' due to the "Permission denied" error in fakeroot.
    # This manually copies files and creates the wrapper.
    
    # 1. Create the target Python site-packages directory
    install -d "$pkgdir/usr/lib/python${_py_ver}/site-packages/"

    # 2. Copy the Python source code into the staging directory
    # NOTE: Assuming your source directory inside the archive is named 'NumScript' or 'numscript'
    # Based on your setup.py (NumScript:main), let's assume the module folder is 'NumScript'.
    # If this fails, try changing the folder name below.
    cp -r NumScript "$pkgdir/usr/lib/python${_py_ver}/site-packages/"
    
    # 3. Create the final executable wrapper for the user
    install -Dm755 -t "$pkgdir/usr/bin" <<'EOF'
#!/usr/bin/env python3
import sys

# Ensure the main module can be found by adding the Python path
sys.path.insert(0, '/usr/lib/python3.11/site-packages') 

# Call the entry point defined in setup.py (NumScript:main)
from NumScript import main

if __name__ == "__main__":
    main()
EOF
}
