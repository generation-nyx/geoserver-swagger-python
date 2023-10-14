# swagger-client
Reset/Reload clears internal caches and reloads configuation from disk

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
api_instance = swagger_client.ReloadApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_reload()
except ApiException as e:
    print("Exception when calling ReloadApi->delete_reload: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ReloadApi* | [**delete_reload**](docs/ReloadApi.md#delete_reload) | **DELETE** /reload | 
*ReloadApi* | [**delete_reset**](docs/ReloadApi.md#delete_reset) | **DELETE** /reset | 
*ReloadApi* | [**get_reload**](docs/ReloadApi.md#get_reload) | **GET** /reload | 
*ReloadApi* | [**get_reset**](docs/ReloadApi.md#get_reset) | **GET** /reset | 
*ReloadApi* | [**post_reload**](docs/ReloadApi.md#post_reload) | **POST** /reload | Reload the configuration from disk, and reset all caches.
*ReloadApi* | [**post_reset**](docs/ReloadApi.md#post_reset) | **POST** /reset | Reset all store, raster, and schema caches.
*ReloadApi* | [**put_reload**](docs/ReloadApi.md#put_reload) | **PUT** /reload | Reload the configuration from disk, and reset all caches.
*ReloadApi* | [**put_reset**](docs/ReloadApi.md#put_reset) | **PUT** /reset | Reset all store, raster, and schema caches.


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
