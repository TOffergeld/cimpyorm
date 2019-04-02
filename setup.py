"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""
# IMPORTANT: this file is autogenerated. Do not edit it manually.
# All changes will be lost after `poetry-setup` command execution.
# ----------------------------------------------------------------
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name='cimpyorm',  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.5.5',  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="A database-backed ORM for CIM datasets.",  # Required
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url="http://www.ifht.rwth-aachen.de",  # Optional
    author="Thomas Offergeld",  # Optional
    author_email="offergeld@ifht.rwth-aachen.de",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],  # Optional
    packages=find_packages(exclude=[
        'cimpyorm/config.ini',
        'cimpyorm/Test/Deployment/**',
        '**/.pytest_cache/**',
    ]),  # Required
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'Click',
        'sqlalchemy (>=1.2,<2.0)',
        'networkx (>=2.2,<3.0)',
        'numpy (>=1.15,<2.0)',
        'lxml (>=4.2,<5.0)',
        'pytest (>=4.0,<5.0)',
        'pandas (>=0.24.1,<0.25.0)',
        'tabulate (>=0.8.3,<0.9.0)',
    ],  # Optional
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi
    dependency_links=[],  # Optional
    # https://stackoverflow.com/a/16576850
    package_data={"cimpyorm": ["res/*"]},
    include_package_data=True,
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
        'homepage': 'http://www.ifht.rwth-aachen.de',
    },
    entry_points='''
    [console_scripts]
    cimpyorm=cimpyorm.cli:cli
    '''
)
