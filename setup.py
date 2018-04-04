from setuptools import setup, find_packages
from codecs import open
import os

from metrics_bumpversion import __version__
here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', format='md', to='rst')
except(IOError, ImportError):
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and
                    (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='metrics.bumpversion',
    version=__version__,
    description='plugin for the metrics package (extracts version from .bumpversion.cfg)',
    long_description=long_description,
    license='MIT',
    url='https://github.com/markfink/metrics.bumpversion/',
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Mark Fink',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='mark@mark-fink.de',
    entry_points={
        'metrics.plugin.10': [
            'bumpversion=metrics_bumpversion.info',
        ],
    }
)
