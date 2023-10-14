# swagger-client
A coverage is a raster data set which originates from a coverage store.

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
api_instance = swagger_client.CoveragesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_coverage()
except ApiException as e:
    print("Exception when calling CoveragesApi->delete_coverage: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CoveragesApi* | [**delete_coverage**](docs/CoveragesApi.md#delete_coverage) | **DELETE** /workspaces/{workspace}/coverages/{coverage} | 
*CoveragesApi* | [**delete_coverage_store**](docs/CoveragesApi.md#delete_coverage_store) | **DELETE** /workspaces/{workspace}/coverages | 
*CoveragesApi* | [**delete_workspace_coverage**](docs/CoveragesApi.md#delete_workspace_coverage) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
*CoveragesApi* | [**delete_workspace_coverage_store**](docs/CoveragesApi.md#delete_workspace_coverage_store) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages | 
*CoveragesApi* | [**get_coverage**](docs/CoveragesApi.md#get_coverage) | **GET** /workspaces/{workspace}/coverages/{coverage} | 
*CoveragesApi* | [**get_coverage_store**](docs/CoveragesApi.md#get_coverage_store) | **GET** /workspaces/{workspace}/coverages | 
*CoveragesApi* | [**get_workspace_coverage**](docs/CoveragesApi.md#get_workspace_coverage) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
*CoveragesApi* | [**get_workspace_coverage_store**](docs/CoveragesApi.md#get_workspace_coverage_store) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages | 
*CoveragesApi* | [**post_coverage**](docs/CoveragesApi.md#post_coverage) | **POST** /workspaces/{workspace}/coverages/{coverage} | 
*CoveragesApi* | [**post_coverage_reset**](docs/CoveragesApi.md#post_coverage_reset) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/reset | Reset the caches related to this specific coverage.
*CoveragesApi* | [**post_coverage_store**](docs/CoveragesApi.md#post_coverage_store) | **POST** /workspaces/{workspace}/coverages | 
*CoveragesApi* | [**post_workspace_coverage**](docs/CoveragesApi.md#post_workspace_coverage) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
*CoveragesApi* | [**post_workspace_coverage_store**](docs/CoveragesApi.md#post_workspace_coverage_store) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages | 
*CoveragesApi* | [**put_coverage**](docs/CoveragesApi.md#put_coverage) | **PUT** /workspaces/{workspace}/coverages/{coverage} | 
*CoveragesApi* | [**put_coverage_reset**](docs/CoveragesApi.md#put_coverage_reset) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/reset | Reset the caches related to this specific coverage.
*CoveragesApi* | [**put_coverage_store**](docs/CoveragesApi.md#put_coverage_store) | **PUT** /workspaces/{workspace}/coverages | 
*CoveragesApi* | [**put_workspace_coverage**](docs/CoveragesApi.md#put_workspace_coverage) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
*CoveragesApi* | [**put_workspace_coverage_store**](docs/CoveragesApi.md#put_workspace_coverage_store) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages | 


## Documentation For Models

 - [CoverageInfo](docs/CoverageInfo.md)
 - [CoverageInfoAttributes](docs/CoverageInfoAttributes.md)
 - [CoverageInfoAttributesAttribute](docs/CoverageInfoAttributesAttribute.md)
 - [CoverageInfoDataLinks](docs/CoverageInfoDataLinks.md)
 - [CoverageInfoDataLinksMetadataLink](docs/CoverageInfoDataLinksMetadataLink.md)
 - [CoverageInfoDimensions](docs/CoverageInfoDimensions.md)
 - [CoverageInfoDimensionsCoverageDimension](docs/CoverageInfoDimensionsCoverageDimension.md)
 - [CoverageInfoDimensionsRange](docs/CoverageInfoDimensionsRange.md)
 - [CoverageInfoGrid](docs/CoverageInfoGrid.md)
 - [CoverageInfoGridInterpolationMethods](docs/CoverageInfoGridInterpolationMethods.md)
 - [CoverageInfoGridRange](docs/CoverageInfoGridRange.md)
 - [CoverageInfoGridTransform](docs/CoverageInfoGridTransform.md)
 - [CoverageInfoKeywords](docs/CoverageInfoKeywords.md)
 - [CoverageInfoLatLonBoundingBox](docs/CoverageInfoLatLonBoundingBox.md)
 - [CoverageInfoMetadatalinks](docs/CoverageInfoMetadatalinks.md)
 - [CoverageInfoMetadatalinksMetadataLink](docs/CoverageInfoMetadatalinksMetadataLink.md)
 - [CoverageInfoNamespace](docs/CoverageInfoNamespace.md)
 - [CoverageInfoNativeBoundingBox](docs/CoverageInfoNativeBoundingBox.md)
 - [CoverageInfoResponseSRS](docs/CoverageInfoResponseSRS.md)
 - [CoverageInfoStore](docs/CoverageInfoStore.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse200Coverages](docs/InlineResponse200Coverages.md)
 - [InlineResponse200CoveragesCoverage](docs/InlineResponse200CoveragesCoverage.md)
 - [MetadataEntry](docs/MetadataEntry.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
