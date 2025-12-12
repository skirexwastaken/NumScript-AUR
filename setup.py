from setuptools import setup, find_packages

setup(
    name="numscript",
    version="1.0.0",
    packages=find_packages(),  # will include NumScript and all subfolders
    install_requires=[],
    entry_points={
        "console_scripts": [
            "numscript=NumScript.NumScript:main",  # main() in NumScript.py
        ],
    },
)
