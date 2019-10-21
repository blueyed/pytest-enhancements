from setuptools import setup

setup(
    name="pytest-enhancements",
    setup_requires="setupmeta",
    versioning="devcommit",
    maintainer="Daniel Hahler",
    url="https://github.com/blueyed/pytest-enhancements",
    author="Daniel Hahler",
    py_modules=["pytest_enhancements"],
    package_dir={"": "src"},
    description="Improvements for pytest (rejected upstream)",
    keywords="pytest plugin enhancements",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    entry_points={"pytest11": ["pytest-enhancements = pytest_enhancements"]},
    extra_requires={"testing": ["pytest"]},
)