
from distutils.core import setup

setup(
    name='thinker',
    version='1.0.0',
    packages=['thinker'],
    url='https://github.com/mehmetkose/thinker',
    license='MIT',
    author='Mehmet Kose',
    author_email='mehmet@linux.com',
    description='Rethinkdb wrapper for asyncio',
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
