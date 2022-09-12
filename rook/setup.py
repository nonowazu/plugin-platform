from setuptools import setup, find_packages
from pathlib import Path

CWD = Path(__file__)

with open(CWD / 'requirements.txt') as reqs, open(CWD / 'README.md') as readme, open(CWD / '.python-version') as pyversion:
    requirements = reqs.read()
    readme_md = readme.read()
    python_version = pyversion.read().strip()

setup(
    name='rook',
    version='0.0.1',
    author='Nonowazu',
    author_email='oowazu.nonowazu@gmail.com',
    description='A plugin-platform backend',
    long_description=readme_md,
    long_description_content_type='text/markdown',
    python_requires=f'>={python_version}',
    packages=find_packages(),
)