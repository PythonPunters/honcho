from setuptools import setup, find_packages

from honcho import __version__

setup(
    name = 'redpie.honcho',
    version = __version__,
    packages = find_packages(),

    # metadata for upload to PyPI
    author = 'Kiall Mac Innes',
    author_email = 'kiall.macinnes@redpie.com',
    url = 'https://github.com/redpie/honcho',
    description = 'Fork of http://pypi.python.org/pypi/honcho',
    license = 'MIT',
    keywords = 'sysadmin process procfile',

    test_suite='test.test_simple',

    install_requires=[
        'colorama'
    ],

    entry_points = {
        'console_scripts': [
            'honcho = honcho.command:main'
        ]
    }
)
