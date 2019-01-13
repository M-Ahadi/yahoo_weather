import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'certifi==2018.11.29',
    'chardet==3.0.4',
    'httplib2==0.12.0',
    'idna==2.8',
    'oauth2==1.9.0.post1',
    'requests==2.21.0',
    'urllib3==1.24.1'
]

about = {}
with open(os.path.join(here, 'yahoo_weather', '__version__.py'), mode='rt', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    license=about['__license__'],
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url=about['__url__'],
    install_requires=requires,
    packages=find_packages(),
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)
