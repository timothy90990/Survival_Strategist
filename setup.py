from setuptools import setup, find_packages

setup(
    name='castaway_retreat',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'SQLAlchemy',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'castaway_retreat = src.main:main',
        ],
    },
)
