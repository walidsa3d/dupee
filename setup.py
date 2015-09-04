from setuptools import setup

setup(
	name = "dupee",
    description = "Duplicate File Finder.",
    author = "Walid Saad",
    packages=['lib'],
    author_email = "walid.sa3d@gmail.com",
    entry_points = {
        'console_scripts': [
            'dupee = lib.main:main'
        ],
    }
)