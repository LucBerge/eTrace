#!/usr/bin/python

import setuptools

long_description = open("README.md", "r").read()

setuptools.setup(
	name='eTrace',
	version='1.0',
	author='LucBerge',
	author_email='lucas.bergeron@outlook.fr',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/LucBerge/eTrace',
	packages=setuptools.find_packages(),
	install_requires=['requests']
)
