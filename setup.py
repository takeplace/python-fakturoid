import os
from setuptools import setup

# work around to prevent http://bugs.python.org/issue15881 from showing up
try:
    import multiprocessing
except ImportError:
    pass

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='fakturoid',
    version='0.1',
    url="https://github.com/farin/python-fakturoid",
    description='Python API for fakturoid.cz',
    long_description=read('README.md'),
    author='Roman Krejcik',
    author_email='farin@farin.cz',
    license='MIT',
    keywords=['fakturoid', 'accounting'],
    packages=['fakturoid'],
    install_requires=['requests', 'python-dateutil'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
)