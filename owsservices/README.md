# swagger-client
An OWS service refers to any of the OGC services that GeoServer supports, such as WFS, WMS, and WCS. These endpoints controls the settings of these services.

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
api_instance = swagger_client.OWSServicesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_oseo_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_oseo_settings: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OWSServicesApi* | [**delete_oseo_settings**](docs/OWSServicesApi.md#delete_oseo_settings) | **DELETE** /services/oseo/settings | 
*OWSServicesApi* | [**delete_wcs_settings**](docs/OWSServicesApi.md#delete_wcs_settings) | **DELETE** /services/wcs/settings | 
*OWSServicesApi* | [**delete_wcs_workspace_settings**](docs/OWSServicesApi.md#delete_wcs_workspace_settings) | **DELETE** /services/wcs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**delete_wfs_settings**](docs/OWSServicesApi.md#delete_wfs_settings) | **DELETE** /services/wfs/settings | 
*OWSServicesApi* | [**delete_wfs_workspace_settings**](docs/OWSServicesApi.md#delete_wfs_workspace_settings) | **DELETE** /services/wfs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**delete_wms_settings**](docs/OWSServicesApi.md#delete_wms_settings) | **DELETE** /services/wms/settings | 
*OWSServicesApi* | [**delete_wms_workspace_settings**](docs/OWSServicesApi.md#delete_wms_workspace_settings) | **DELETE** /services/wms/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**delete_wmts_settings**](docs/OWSServicesApi.md#delete_wmts_settings) | **DELETE** /services/wmts/settings | 
*OWSServicesApi* | [**delete_wmts_workspace_settings**](docs/OWSServicesApi.md#delete_wmts_workspace_settings) | **DELETE** /services/wmts/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**get_oseo_settings**](docs/OWSServicesApi.md#get_oseo_settings) | **GET** /services/oseo/settings | 
*OWSServicesApi* | [**get_wcs_settings**](docs/OWSServicesApi.md#get_wcs_settings) | **GET** /services/wcs/settings | 
*OWSServicesApi* | [**get_wcs_workspace_settings**](docs/OWSServicesApi.md#get_wcs_workspace_settings) | **GET** /services/wcs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**get_wfs_settings**](docs/OWSServicesApi.md#get_wfs_settings) | **GET** /services/wfs/settings | 
*OWSServicesApi* | [**get_wfs_workspace_settings**](docs/OWSServicesApi.md#get_wfs_workspace_settings) | **GET** /services/wfs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**get_wms_settings**](docs/OWSServicesApi.md#get_wms_settings) | **GET** /services/wms/settings | 
*OWSServicesApi* | [**get_wms_workspace_settings**](docs/OWSServicesApi.md#get_wms_workspace_settings) | **GET** /services/wms/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**get_wmts_settings**](docs/OWSServicesApi.md#get_wmts_settings) | **GET** /services/wmts/settings | 
*OWSServicesApi* | [**get_wmts_workspace_settings**](docs/OWSServicesApi.md#get_wmts_workspace_settings) | **GET** /services/wmts/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**post_oseo_settings**](docs/OWSServicesApi.md#post_oseo_settings) | **POST** /services/oseo/settings | 
*OWSServicesApi* | [**post_wcs_settings**](docs/OWSServicesApi.md#post_wcs_settings) | **POST** /services/wcs/settings | 
*OWSServicesApi* | [**post_wcs_workspace_settings**](docs/OWSServicesApi.md#post_wcs_workspace_settings) | **POST** /services/wcs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**post_wfs_settings**](docs/OWSServicesApi.md#post_wfs_settings) | **POST** /services/wfs/settings | 
*OWSServicesApi* | [**post_wfs_workspace_settings**](docs/OWSServicesApi.md#post_wfs_workspace_settings) | **POST** /services/wfs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**post_wms_settings**](docs/OWSServicesApi.md#post_wms_settings) | **POST** /services/wms/settings | 
*OWSServicesApi* | [**post_wms_workspace_settings**](docs/OWSServicesApi.md#post_wms_workspace_settings) | **POST** /services/wms/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**post_wmts_settings**](docs/OWSServicesApi.md#post_wmts_settings) | **POST** /services/wmts/settings | 
*OWSServicesApi* | [**post_wmts_workspace_settings**](docs/OWSServicesApi.md#post_wmts_workspace_settings) | **POST** /services/wmts/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**put_oseo_settings**](docs/OWSServicesApi.md#put_oseo_settings) | **PUT** /services/oseo/settings | 
*OWSServicesApi* | [**put_wcs_settings**](docs/OWSServicesApi.md#put_wcs_settings) | **PUT** /services/wcs/settings | 
*OWSServicesApi* | [**put_wcs_workspace_settings**](docs/OWSServicesApi.md#put_wcs_workspace_settings) | **PUT** /services/wcs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**put_wfs_settings**](docs/OWSServicesApi.md#put_wfs_settings) | **PUT** /services/wfs/settings | 
*OWSServicesApi* | [**put_wfs_workspace_settings**](docs/OWSServicesApi.md#put_wfs_workspace_settings) | **PUT** /services/wfs/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**put_wms_settings**](docs/OWSServicesApi.md#put_wms_settings) | **PUT** /services/wms/settings | 
*OWSServicesApi* | [**put_wms_workspace_settings**](docs/OWSServicesApi.md#put_wms_workspace_settings) | **PUT** /services/wms/workspaces/{workspace}/settings | 
*OWSServicesApi* | [**put_wmts_settings**](docs/OWSServicesApi.md#put_wmts_settings) | **PUT** /services/wmts/settings | 
*OWSServicesApi* | [**put_wmts_workspace_settings**](docs/OWSServicesApi.md#put_wmts_workspace_settings) | **PUT** /services/wmts/workspaces/{workspace}/settings | 


## Documentation For Models

 - [WCSInfo](docs/WCSInfo.md)
 - [WFSInfo](docs/WFSInfo.md)
 - [WFSInfoGml](docs/WFSInfoGml.md)
 - [WFSInfoGmlEntry](docs/WFSInfoGmlEntry.md)
 - [WFSInfoGmlGml](docs/WFSInfoGmlGml.md)
 - [WFSInfoMetadataLink](docs/WFSInfoMetadataLink.md)
 - [WMSInfo](docs/WMSInfo.md)
 - [WMSInfoMetadataLink](docs/WMSInfoMetadataLink.md)
 - [WMSInfoVersions](docs/WMSInfoVersions.md)
 - [WMSInfoWatermark](docs/WMSInfoWatermark.md)
 - [WMTSInfo](docs/WMTSInfo.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
