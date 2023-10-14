# swagger-client
Request provides details about OWS and REST requests that GeoServer has handled

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
api_instance = swagger_client.MonitoringApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_monitor_request()
except ApiException as e:
    print("Exception when calling MonitoringApi->delete_monitor_request: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MonitoringApi* | [**delete_monitor_request**](docs/MonitoringApi.md#delete_monitor_request) | **DELETE** /monitor/requests/{request} | 
*MonitoringApi* | [**delete_monitor_requests**](docs/MonitoringApi.md#delete_monitor_requests) | **DELETE** /monitor/requests | 
*MonitoringApi* | [**get_monitor_request**](docs/MonitoringApi.md#get_monitor_request) | **GET** /monitor/requests/{request} | Get a list of requests
*MonitoringApi* | [**get_monitor_requests**](docs/MonitoringApi.md#get_monitor_requests) | **GET** /monitor/requests | Get a list of requests
*MonitoringApi* | [**post_monitor_request**](docs/MonitoringApi.md#post_monitor_request) | **POST** /monitor/requests/{request} | 
*MonitoringApi* | [**post_monitor_requests**](docs/MonitoringApi.md#post_monitor_requests) | **POST** /monitor/requests | 
*MonitoringApi* | [**put_monitor_request**](docs/MonitoringApi.md#put_monitor_request) | **PUT** /monitor/requests/{request} | 
*MonitoringApi* | [**put_monitor_requests**](docs/MonitoringApi.md#put_monitor_requests) | **PUT** /monitor/requests | 


## Documentation For Models

 - [Request](docs/Request.md)
 - [RequestList](docs/RequestList.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
