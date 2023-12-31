# coding: utf-8

"""
    GeoWebCache DiskQuota

    The REST API for Disk Quota management provides a RESTful interface through which clients can configure the disk usage limits and expiration policies for a GeoWebCache instance through simple HTTP calls.  Since disk usage increases geometrically by zoom level, one single seeding task could fill up an entire storage device. Because of this, GeoWebCache employs a disk quota system where one can specify the maximum amount of disk space to use for a particular layer, as well as logic on how to proceed when that quota is reached. There are two different policies for managing the disk quotas - Least Frequently Used (LFU) and Least Recently Used (LRU).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-geoserver-gwcdiskquota"
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
    description="GeoWebCache DiskQuota",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoWebCache DiskQuota"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The REST API for Disk Quota management provides a RESTful interface through which clients can configure the disk usage limits and expiration policies for a GeoWebCache instance through simple HTTP calls.  Since disk usage increases geometrically by zoom level, one single seeding task could fill up an entire storage device. Because of this, GeoWebCache employs a disk quota system where one can specify the maximum amount of disk space to use for a particular layer, as well as logic on how to proceed when that quota is reached. There are two different policies for managing the disk quotas - Least Frequently Used (LFU) and Least Recently Used (LRU).  # noqa: E501
    """
)
