from setuptools import setup, find_packages

setup(
    name='neo4j_connection',
    version='0.2.0',
    description='OGM for Support-Manager\'s neo4j database.',
    long_description='',
    url='https://github.com/Support-Manager/neo4j-connection',
    author='Linus Bartsch, Martin Bartsch',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    keywords='neo4j database ogm',
    install_requires=['py2neo'],
    packages=find_packages(),
    data_files=None
)
