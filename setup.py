#!/usr/bin/python3.7
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pingwin', 
    version='1.0.0',  
    description='''Python educational and experimental based desktop application that leaks files through protocols which wasn't made for file transfer. 
    This program will help someone check whether files can be transfered from his own computer to outside the internal network, using these protocols. ''',  # Optional
    url='https://github.com/rayahazi/pingwin',
    author='Raya Hazi',  
    author_email='raayahazi@gmail.com',  
    classifiers=[  
        'Intended Audience :: Developers',
        'Topic :: Cyber security tools :: Hacking Tools',
        'License :: GNU License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='data leak hacking tool', 
    packages=find_packages(exclude=['CORE', 'UI']),  
    python_requires='>=!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=['scapy','tkinter'],  
)
