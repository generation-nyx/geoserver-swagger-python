# swagger-client
A structured coverage store allows description of its \"granules\" and management of them.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://geoserver.org/comm/](http://geoserver.org/comm/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_coverage_stores()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->delete_coverage_stores: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StructuredCoveragesApi* | [**delete_coverage_stores**](docs/StructuredCoveragesApi.md#delete_coverage_stores) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 
*StructuredCoveragesApi* | [**delete_structured_coverage_granule**](docs/StructuredCoveragesApi.md#delete_structured_coverage_granule) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
*StructuredCoveragesApi* | [**delete_structured_coverage_granules**](docs/StructuredCoveragesApi.md#delete_structured_coverage_granules) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
*StructuredCoveragesApi* | [**get_structured_coverage_granule**](docs/StructuredCoveragesApi.md#get_structured_coverage_granule) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | Get the attributes of a particular granule
*StructuredCoveragesApi* | [**get_structured_coverage_granules**](docs/StructuredCoveragesApi.md#get_structured_coverage_granules) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | Get the attributes associated to the granules
*StructuredCoveragesApi* | [**get_structured_coverage_index**](docs/StructuredCoveragesApi.md#get_structured_coverage_index) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | Get the information schema attached to the granules
*StructuredCoveragesApi* | [**post_structured_coverage_granule**](docs/StructuredCoveragesApi.md#post_structured_coverage_granule) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
*StructuredCoveragesApi* | [**post_structured_coverage_granules**](docs/StructuredCoveragesApi.md#post_structured_coverage_granules) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
*StructuredCoveragesApi* | [**post_structured_coverage_index**](docs/StructuredCoveragesApi.md#post_structured_coverage_index) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 
*StructuredCoveragesApi* | [**put_structured_coverage_granule**](docs/StructuredCoveragesApi.md#put_structured_coverage_granule) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
*StructuredCoveragesApi* | [**put_structured_coverage_granules**](docs/StructuredCoveragesApi.md#put_structured_coverage_granules) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
*StructuredCoveragesApi* | [**put_structured_coverage_index**](docs/StructuredCoveragesApi.md#put_structured_coverage_index) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 


## Documentation For Models

 - [Attribute](docs/Attribute.md)
 - [Schema](docs/Schema.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

