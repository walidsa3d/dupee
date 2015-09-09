from setuptools import setup
from setuptools import find_packages


setup(
    name='dupee',
    version='0.1',
    description='duplicate file finder',
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='github.com/walidsa3d/dupee',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console :: Curses',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities'
    ],
    include_package_data=True,
    package_data={'dupee': ['LICENSE', 'README.md']},
    packages=find_packages(exclude=['test', 'tests']),
    long_description='duplicate file finder',
    entry_points={"console_scripts": ["dupee=dupee.cli:main"]},

)
