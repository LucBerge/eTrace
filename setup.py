import sys
if sys.version_info < (3, 5):
    sys.exit('Y2T requires Python 3.5+')

long_description = open("README.md", "r").read()

import setuptools
setuptools.setup(
	name='eTrace',
	version='1.0',
	author='LucBerge',
	author_email='lucas.bergeron@outlook.fr',
	description="Trace your email on internet",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/LucBerge/eTrace',
	packages=setuptools.find_packages(),
	install_requires=['requests']
)
