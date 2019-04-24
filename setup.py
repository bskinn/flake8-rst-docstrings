"""Setup file for building/installing flake8-rst-docstrings."""

from __future__ import with_statement
from __future__ import print_function

from setuptools import setup


def get_version(fname="flake8_rst_docstrings.py"):
    """Parse our source code to get the current version number."""
    with open(fname) as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])


setup(
    name="flake8-rst-docstrings",
    version=get_version(),
    description="Python docstring reStructuredText (RST) validator",
    long_description=open("README.rst").read(),
    license="MIT",
    author="Peter J. A. Cock",
    author_email="p.j.a.cock@googlemail.com",
    url="https://github.com/peterjc/flake8-rst-docstrings",
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Flake8",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    keywords="PEP 287, pep287, docstrings, rst, reStructuredText",
    py_modules=["flake8_rst_docstrings"],
    install_requires=["flake8 >= 3.0.0", "restructuredtext_lint"],
    entry_points={
        "flake8.extension": ["RST = flake8_rst_docstrings:reStructuredTextChecker"]
    },
    extras_require={
        'test': ["pytest>=4.4.0", "pytest-cov", "pytest-subtests"],
    }
)
