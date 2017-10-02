from setuptools import setup, find_packages

setup(name='api',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'html5lib',
    ],
)
