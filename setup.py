"""
TimeUUID
-------------
Sequentially sortable, time-based UUIDs
"""

from setuptools import setup
import os


setup(
    name='TimeUUID',
    version='0.1',
    url='https://github.com/Tamarabyte/TimeUUID',
    license='MIT',
    description='Sequentially sortable, time-based UUIDs',

    py_modules=['timeUUID'],
    platforms='any',
    test_suite='test_timeUUID',
    
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    ]
)
