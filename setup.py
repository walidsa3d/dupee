from setuptools import find_packages
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print """warning: pypandoc module not found,
        could not convert Markdown to RST"""
    read_md = lambda f: open(f, 'r').read()

setup(
    name='dupee',
    version='0.2.0',
    description='duplicate file finder',
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='github.com/walidsa3d/dupee',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities'
    ],
    include_package_data=True,
    package_data={'dupee': ['LICENSE', 'README.md']},
    packages=find_packages(exclude=['test', 'tests']),
    long_description=read_md('README.md'),
    entry_points={"console_scripts": ["dupee=dupee.cli:main"]},

)
