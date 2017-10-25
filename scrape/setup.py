from setuptools import setup

setup(name='api',
    version='0.0.1',
    packages=['apt_scrape'],
    install_requires=[
        'beautifulsoup4',
        'html5lib',
        'selenium'
    ],
    include_package_data=True
)
