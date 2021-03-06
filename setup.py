#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import io
import os.path
import sys

import setuptools


MODULE_NAME = "pytablereader"
REPOSITORY_URL = "https://github.com/thombashi/{:s}".format(MODULE_NAME)
REQUIREMENT_DIR = "requirements"
ENCODING = "utf8"

pkg_info = {}


def need_pytest():
    return set(["pytest", "test", "ptr"]).intersection(sys.argv)


def get_release_command_class():
    try:
        from releasecmd import ReleaseCommand
    except ImportError:
        return {}

    return {"release": ReleaseCommand}


with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with io.open("README.rst", encoding=ENCODING) as fp:
    long_description = fp.read()

with io.open(os.path.join("docs", "pages", "introduction", "summary.txt"), encoding=ENCODING) as f:
    summary = f.read().strip()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "docs_requirements.txt")) as f:
    docs_requires = [line.strip() for line in f if line.strip()]

setuptools_require = ["setuptools>=38.3.0"]
pytest_runner_require = ["pytest-runner"] if need_pytest() else []

excel_requires = ["xlrd>=1.2.0"]
mediawiki_requires = ["pypandoc"]
sqlite_requires = ["SimpleSQLite>=0.38.0,<1.0.0"]
gs_requires = ["gspread", "oauth2client", "pyOpenSSL"] + sqlite_requires
logging_requires = ["Logbook>=1.1.0,<2.0.0"]
url_requires = ["requests>=2.21.0,<3.0.0"]
optional_requires = ["simplejson>=3.16,<4.0"]
tests_requires = frozenset(
    tests_requires
    + excel_requires
    + mediawiki_requires
    + sqlite_requires
    + optional_requires
)

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    url=REPOSITORY_URL,

    author=pkg_info["__author__"],
    author_email=pkg_info["__email__"],
    description=summary,
    include_package_data=True,
    keywords=[
        "table", "reader", "pandas",
        "CSV", "Excel", "HTML", "JSON", "LTSV", "Markdown", "MediaWiki", "TSV",
        "SQLite",
    ],
    license=pkg_info["__license__"],
    long_description=long_description,
    packages=setuptools.find_packages(exclude=["test*"]),
    project_urls={
        "Documentation": "https://{:s}.rtfd.io/".format(MODULE_NAME),
        "Source": REPOSITORY_URL,
        "Tracker": "{:s}/issues".format(REPOSITORY_URL),
    },

    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=setuptools_require + install_requires,
    setup_requires=setuptools_require + pytest_runner_require,
    tests_require=tests_requires,
    extras_require={
        "all": set(
            excel_requires
            + gs_requires
            + logging_requires
            + mediawiki_requires
            + sqlite_requires
            + url_requires
            + optional_requires
        ),
        "build": ["wheel"],
        "docs": docs_requires,
        "excel": excel_requires,
        "gs": gs_requires,
        "logging": logging_requires,
        "mediawiki": mediawiki_requires,
        "release": ["releasecmd>=0.0.14,<0.1.0"],
        "url": url_requires,
        "sqlite": sqlite_requires,
        "test": tests_requires,
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
    cmdclass=get_release_command_class())
