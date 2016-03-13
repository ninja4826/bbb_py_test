try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Beaglebone Py Test',
    'author': 'Ninja4826',
    'url': 'https://github.com/ninja4826/bbb_py_test',
    'author_email': 'hueske.russ690@gmail.com',
    'version': '0.0.1',
    'install_requires': ['Adafruit_BBIO'],
    'packages': ['py_test'],
    'scripts': [],
    'name': 'py_test'
}

setup(**config)
