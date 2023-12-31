# swagger-client
Organisation of security roles

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | the name of the role

try:
    # Delete a role
    api_instance.role_default_delete(role)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://geoserver:8080/geoserver/rest/security*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RolesApi* | [**role_default_delete**](docs/RolesApi.md#role_default_delete) | **DELETE** /roles/role/{role} | Delete a role
*RolesApi* | [**role_default_group_delete**](docs/RolesApi.md#role_default_group_delete) | **DELETE** /roles/role/{role}/group/{group} | Disassociate a role from a group
*RolesApi* | [**role_default_group_post**](docs/RolesApi.md#role_default_group_post) | **POST** /roles/role/{role}/group/{group} | Associate a role with a group
*RolesApi* | [**role_default_post**](docs/RolesApi.md#role_default_post) | **POST** /roles/role/{role} | Add a role
*RolesApi* | [**role_default_user_delete**](docs/RolesApi.md#role_default_user_delete) | **DELETE** /roles/role/{role}/user/{user} | Disassociate a role from a user
*RolesApi* | [**role_default_user_post**](docs/RolesApi.md#role_default_user_post) | **POST** /roles/role/{role}/user/{user} | Associate a role with a user
*RolesApi* | [**role_delete**](docs/RolesApi.md#role_delete) | **DELETE** /service/{serviceName}/role/{role} | Delete a role
*RolesApi* | [**role_group_delete**](docs/RolesApi.md#role_group_delete) | **DELETE** /service/{serviceName}/roles/role/{role}/group/{group} | Disassociate a role from a group
*RolesApi* | [**role_group_post**](docs/RolesApi.md#role_group_post) | **POST** /service/{serviceName}/roles/role/{role}/group/{group} | Associate a role with a group
*RolesApi* | [**role_post**](docs/RolesApi.md#role_post) | **POST** /service/{serviceName}/role/{role} | Add a role
*RolesApi* | [**role_user_delete**](docs/RolesApi.md#role_user_delete) | **DELETE** /service/{serviceName}/roles/role/{role}/user/{user} | Disassociate a role from a user
*RolesApi* | [**role_user_post**](docs/RolesApi.md#role_user_post) | **POST** /service/{serviceName}/roles/role/{role}/user/{user} | Associate a role with a user
*RolesApi* | [**roles_default_get**](docs/RolesApi.md#roles_default_get) | **GET** /roles | Query all roles
*RolesApi* | [**roles_default_group_get**](docs/RolesApi.md#roles_default_group_get) | **GET** /roles/group/{group} | Query all roles for group
*RolesApi* | [**roles_default_user_get**](docs/RolesApi.md#roles_default_user_get) | **GET** /roles/user/{user} | Query all roles for user
*RolesApi* | [**roles_get**](docs/RolesApi.md#roles_get) | **GET** /roles/service/{serviceName}/roles/ | Query all roles
*RolesApi* | [**roles_group_get**](docs/RolesApi.md#roles_group_get) | **GET** /roles/service/{serviceName}/group/{group} | Query all roles for group
*RolesApi* | [**roles_user_get**](docs/RolesApi.md#roles_user_get) | **GET** /roles/service/{serviceName}/user/{user} | Query all roles for user


## Documentation For Models

 - [Role](docs/Role.md)
 - [Roles](docs/Roles.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

