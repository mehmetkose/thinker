
from distutils.core import setup
import thinker

setup(
    name='thinker',
    description='Rethinkdb wrapper for asyncio',
    version=thinker.__version__,
    author=thinker.__author__,
    author_email=thinker.__email__,
    packages=['thinker'],
    url='https://github.com/mehmetkose/thinker',
    license='MIT',
    platforms=('Any'),
    keywords='asyncio rethinkdb layer'.split(),
    install_requires=[
        'rethinkdb>=2.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
    ],
)
