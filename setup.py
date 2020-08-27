# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cimec_infotech/__init__.py
from cimec_infotech import __version__ as version

setup(
	name='ltsp_billing',
	version=version,
	description='LTSP Billing Customisations',
	author='4C Solutions',
	author_email='info@4csolutions.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
