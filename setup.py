#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# setup.py
from setuptools import setup, find_packages

setup(
    name='missing_imputer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Bayesian imputation for financial time series using Gaussian Processes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/finance-missing-imputation',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

