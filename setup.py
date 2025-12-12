from setuptools import setup, find_packages

setup(
    name="numscript",
    version="1.0.0",
    packages=find_packages(),  # will now find NumScript/ and source/
    install_requires=[],
    entry_points={
        "console_scripts": [
            "numscript=NumScript.NumScript:main",
        ],
    },
)
