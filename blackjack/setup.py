from setuptools import setup, find_packages

setup(
    name='Blackjack',
    version='2.0',
    packages=find_packages(),
    package_dir={'': 'blackjack'},
    include_package_data=True,
    install_requires=['pygame', 'Sphinx'],
    url='https://github.com/TrevorMcDougald/Blackjack',
    license='MIT',
    author='Trevor McDougald',
    author_email='',
    description='Blackjack Casino Game programmed in Python'
)
