# coding: utf-8

"""
    GeoServer Layer Groups

    A layer group is a group of layers that can be referenced as a single layer as part of a WMS request. A layer group can also be used as a container for layers.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-geoserver-layergroups"
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
    description="GeoServer Layer Groups",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoServer Layer Groups"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A layer group is a group of layers that can be referenced as a single layer as part of a WMS request. A layer group can also be used as a container for layers.  # noqa: E501
    """
)