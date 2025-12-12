from setuptools import setup, find_packages

setup(
    name="numscript",
    version="1.0.0",
    packages=find_packages(include=["NumScript", "NumScript.*"]),
    include_package_data=True,
    package_data={
        "NumScript": [
            "source/json/*.json",
            "source/*.ns", 
        ]
    },
    entry_points={
        "console_scripts": [
            "numscript=NumScript.NumScript:main",
        ],
    },
    python_requires=">=3.10",  # Minimum Python version
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
