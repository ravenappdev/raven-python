from setuptools import setup, find_packages  # noqa: H301

NAME = "raven"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Raven API",
    author_email="api@ravenapp.dev",
    url="",
    keywords=["Swagger", "Raven API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    # long_description="""\
    # This is OpenAPI defintion for the APIs of Raven.  You can find out more about Raven at [https://ravenapp.dev/](https://ravenapp.dev/).  # noqa: E501
    # """
)
