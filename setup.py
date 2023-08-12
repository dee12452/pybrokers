from setuptools import setup, find_packages

setup(
    name='pybrokers',
    version='1.0.0',
    description='HTTP Apis for stock trading platforms',
    author='OptionBot',
    author_email='optionbot@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dateutil',
        'attrs'
    ],
)
