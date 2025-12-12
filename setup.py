from setuptools import setup

setup(
    name="numscript",
    version="1.0.0",
    py_modules=["NumScript"],  # single file module
    install_requires=[],
    entry_points={
        "console_scripts": [
            "numscript=NumScript:main",  # points to main() in NumScript.py
        ],
    },
)
