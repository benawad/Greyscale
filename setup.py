try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import py2exe

config = {
    'description': 'Turn any image to grayscale',
    'author': 'Ben Awad',
    'url': 'julieawad.com',
    'download_url': 'Where to download it.',
    'author_email': 'benawad97@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Greyscale'],
    'scripts': ['runner.py'],
    'name': 'Greyscale',
    'console': ['runner.py']
}

setup(**config)