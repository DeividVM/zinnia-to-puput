import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_author(package):
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_email(package):
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

setup(
    name='zinnia-to-puput',
    version=get_version('zinnia2puput'),
    packages=find_packages(),
    include_package_data=True,
    keywords="django wagtail puput blog cms zinnia",
    description='Import your Zinnia blog data into Puput.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    install_requires=[
        'puput==0.2',
        'django-blog-zinnia==0.15.2',
        'lxml==3.4.4',
    ],
    url='http://github.com/APSL/zinnia-to-puput',
    author=get_author('zinnia2puput'),
    author_email=get_email('zinnia2puput'),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
