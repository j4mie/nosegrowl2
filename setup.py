import os
import re
from setuptools import setup

rel_file = lambda *args: os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)

def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()

def get_version():
    data = read_from(rel_file('nosegrowl2', '__init__.py'))
    return re.search(r"__version__ = '([^']+)'", data).group(1)

setup(
    name='nosegrowl2',
    description = 'A simple Nose plugin for Growl notifications. Requires the command-line growlnotify tool.',
    version=get_version(),
    packages = ['nosegrowl2'],
    include_package_data = True,
    package_data = {
        '': ['*.png'],
    },
    author='Jamie Matthews',
    author_email = 'jamie.matthews@gmail.com',
    install_requires=['nose>=0.10'],
    url = 'https://github.com/j4mie/nosegrowl2',
    license = 'Public Domain',
    zip_safe = False,
    entry_points = {
        'nose.plugins': [
            'growl = nosegrowl2:NoseGrowl'
        ]
    },
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
    ],
)
