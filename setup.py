try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'salt pillar sync tool for easy synchronization of secret pillars',
    'author': 'Marc Siebeneicher',
    'url': 'https://github.com/msiebeneicher/PiSy',
    'download_url': 'https://github.com/msiebeneicher/PiSy/releases',
    'author_email': 'marc.siebeneicher@trivago.com ',
    'version': '0.1.0',
    'install_requires': [
        'PyYAML',
        'six'
    ],
    'packages': ['pisy'],
    'scripts': [
        'bin/pisy'
    ],
    'name': 'pisy',
    'classifiers': [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Configuration Management :: Salt :: Tools',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
}

setup(**config)