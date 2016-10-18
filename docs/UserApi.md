# swagger_client.UserApi

All URIs are relative to *http://petstore.swagger.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllers_user_controller_create_user**](UserApi.md#controllers_user_controller_create_user) | **POST** /user | Create user
[**controllers_user_controller_create_users_with_array_input**](UserApi.md#controllers_user_controller_create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
[**controllers_user_controller_create_users_with_list_input**](UserApi.md#controllers_user_controller_create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
[**controllers_user_controller_delete_user**](UserApi.md#controllers_user_controller_delete_user) | **DELETE** /user/{username} | Delete user
[**controllers_user_controller_get_user_by_name**](UserApi.md#controllers_user_controller_get_user_by_name) | **GET** /user/{username} | Get user by user name
[**controllers_user_controller_login_user**](UserApi.md#controllers_user_controller_login_user) | **GET** /user/login | Logs user into the system
[**controllers_user_controller_logout_user**](UserApi.md#controllers_user_controller_logout_user) | **GET** /user/logout | Logs out current logged in user session
[**controllers_user_controller_update_user**](UserApi.md#controllers_user_controller_update_user) | **PUT** /user/{username} | Updated user


# **controllers_user_controller_create_user**
> controllers_user_controller_create_user(body)

Create user

This can only be done by the logged in user.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.User() # User | Created user object

try: 
    # Create user
    api_instance.controllers_user_controller_create_user(body)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_create_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| Created user object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_create_users_with_array_input**
> controllers_user_controller_create_users_with_array_input(body)

Creates list of users with given input array



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = [swagger_client.User()] # list[User] | List of user object

try: 
    # Creates list of users with given input array
    api_instance.controllers_user_controller_create_users_with_array_input(body)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_create_users_with_array_input: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[User]**](User.md)| List of user object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_create_users_with_list_input**
> controllers_user_controller_create_users_with_list_input(body)

Creates list of users with given input array



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = [swagger_client.User()] # list[User] | List of user object

try: 
    # Creates list of users with given input array
    api_instance.controllers_user_controller_create_users_with_list_input(body)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_create_users_with_list_input: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[User]**](User.md)| List of user object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_delete_user**
> controllers_user_controller_delete_user(username)

Delete user

This can only be done by the logged in user.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | The name that needs to be deleted

try: 
    # Delete user
    api_instance.controllers_user_controller_delete_user(username)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_delete_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_get_user_by_name**
> User controllers_user_controller_get_user_by_name(username)

Get user by user name



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | The name that needs to be fetched. Use user1 for testing. 

try: 
    # Get user by user name
    api_response = api_instance.controllers_user_controller_get_user_by_name(username)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_get_user_by_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be fetched. Use user1 for testing.  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_login_user**
> str controllers_user_controller_login_user(username, password)

Logs user into the system



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | The user name for login
password = 'password_example' # str | The password for login in clear text

try: 
    # Logs user into the system
    api_response = api_instance.controllers_user_controller_login_user(username, password)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_login_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user name for login | 
 **password** | **str**| The password for login in clear text | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_logout_user**
> controllers_user_controller_logout_user()

Logs out current logged in user session



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try: 
    # Logs out current logged in user session
    api_instance.controllers_user_controller_logout_user()
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_logout_user: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_user_controller_update_user**
> controllers_user_controller_update_user(username, body)

Updated user

This can only be done by the logged in user.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | name that need to be deleted
body = swagger_client.User() # User | Updated user object

try: 
    # Updated user
    api_instance.controllers_user_controller_update_user(username, body)
except ApiException as e:
    print "Exception when calling UserApi->controllers_user_controller_update_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| name that need to be deleted | 
 **body** | [**User**](User.md)| Updated user object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

