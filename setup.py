from setuptools import setup
from dictenvy import __version__

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dict-envy',
    version=__version__,
    description='dict-like grouping of environment variables',
    long_description=long_description,
    author='Roman Tomjak',
    author_email='roman.tomjak@made.com',
    url='http://github.com/madedotcom/dict-envy',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
)
