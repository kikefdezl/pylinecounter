from setuptools import setup

__version__ = "0.1.0"

setup(
    name="pylinecounter",
    py_modules=['pylinecounter'],
    version=__version__,
    url="https://github.com/kikefdezl/pylinecounter",
    description="A package to count the lines of a Python project.",
    author="Enrique Fernández-Laguilhoat Sánchez-Biezma",
    author_email="enriquelagui@outlook.com",
    entry_points={
        "console_scripts": [
            "pylinecounter=pylinecounter:main",
        ],
    },
)
