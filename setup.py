from setuptools import setup, find_packages

setup(
    name="numscript",
    version="1.0.0",
    packages=find_packages(include=["NumScript", "NumScript.*"]),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "numscript=NumScript.NumScript:main",
        ],
    },
)
