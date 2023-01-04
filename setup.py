from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sobulk_search/__init__.py
from sobulk_search import __version__ as version

setup(
	name="sobulk_search",
	version=version,
	description="This allow user to search bulk using and excel which contain the list of Sales Order",
	author="John Rech Cabatana",
	author_email="cabatana.johnrech.g@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
