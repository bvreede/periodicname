from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "periodicname",
    version = "0.1.0",
    description = ("Spell using elements of the periodic table."),
    license = "MIT",
    url = "https://github.com/bvreede/periodicname",
    packages = find_packages(),
    install_requires=required,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)