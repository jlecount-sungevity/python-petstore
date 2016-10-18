# swagger_client.PetApi

All URIs are relative to *http://petstore.swagger.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllers_pet_controller_add_pet**](PetApi.md#controllers_pet_controller_add_pet) | **POST** /pet | Add a new pet to the store
[**controllers_pet_controller_delete_pet**](PetApi.md#controllers_pet_controller_delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
[**controllers_pet_controller_find_pets_by_status**](PetApi.md#controllers_pet_controller_find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
[**controllers_pet_controller_find_pets_by_tags**](PetApi.md#controllers_pet_controller_find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
[**controllers_pet_controller_get_pet_by_id**](PetApi.md#controllers_pet_controller_get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
[**controllers_pet_controller_update_pet**](PetApi.md#controllers_pet_controller_update_pet) | **PUT** /pet | Update an existing pet
[**controllers_pet_controller_update_pet_with_form**](PetApi.md#controllers_pet_controller_update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
[**controllers_pet_controller_upload_file**](PetApi.md#controllers_pet_controller_upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image


# **controllers_pet_controller_add_pet**
> controllers_pet_controller_add_pet(body)

Add a new pet to the store



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
body = swagger_client.Pet() # Pet | Pet object that needs to be added to the store

try: 
    # Add a new pet to the store
    api_instance.controllers_pet_controller_add_pet(body)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_add_pet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pet**](Pet.md)| Pet object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_delete_pet**
> controllers_pet_controller_delete_pet(pet_id, api_key=api_key)

Deletes a pet



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
pet_id = 789 # int | Pet id to delete
api_key = 'api_key_example' # str |  (optional)

try: 
    # Deletes a pet
    api_instance.controllers_pet_controller_delete_pet(pet_id, api_key=api_key)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_delete_pet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| Pet id to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_find_pets_by_status**
> list[Pet] controllers_pet_controller_find_pets_by_status(status)

Finds Pets by status

Multiple status values can be provided with comma separated strings

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
status = ['status_example'] # list[str] | Status values that need to be considered for filter

try: 
    # Finds Pets by status
    api_response = api_instance.controllers_pet_controller_find_pets_by_status(status)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_find_pets_by_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)| Status values that need to be considered for filter | 

### Return type

[**list[Pet]**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_find_pets_by_tags**
> list[Pet] controllers_pet_controller_find_pets_by_tags(tags)

Finds Pets by tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
tags = ['tags_example'] # list[str] | Tags to filter by

try: 
    # Finds Pets by tags
    api_response = api_instance.controllers_pet_controller_find_pets_by_tags(tags)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_find_pets_by_tags: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| Tags to filter by | 

### Return type

[**list[Pet]**](Pet.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_get_pet_by_id**
> Pet controllers_pet_controller_get_pet_by_id(pet_id)

Find pet by ID

Returns a single pet

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PetApi()
pet_id = 789 # int | ID of pet to return

try: 
    # Find pet by ID
    api_response = api_instance.controllers_pet_controller_get_pet_by_id(pet_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_get_pet_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet to return | 

### Return type

[**Pet**](Pet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_update_pet**
> controllers_pet_controller_update_pet(body)

Update an existing pet



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
body = swagger_client.Pet() # Pet | Pet object that needs to be added to the store

try: 
    # Update an existing pet
    api_instance.controllers_pet_controller_update_pet(body)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_update_pet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pet**](Pet.md)| Pet object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_update_pet_with_form**
> controllers_pet_controller_update_pet_with_form(pet_id, name=name, status=status)

Updates a pet in the store with form data



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
pet_id = 789 # int | ID of pet that needs to be updated
name = 'name_example' # str | Updated name of the pet (optional)
status = 'status_example' # str | Updated status of the pet (optional)

try: 
    # Updates a pet in the store with form data
    api_instance.controllers_pet_controller_update_pet_with_form(pet_id, name=name, status=status)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_update_pet_with_form: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet that needs to be updated | 
 **name** | **str**| Updated name of the pet | [optional] 
 **status** | **str**| Updated status of the pet | [optional] 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controllers_pet_controller_upload_file**
> ApiResponse controllers_pet_controller_upload_file(pet_id, additional_metadata=additional_metadata, file=file)

uploads an image



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi()
pet_id = 789 # int | ID of pet to update
additional_metadata = 'additional_metadata_example' # str | Additional data to pass to server (optional)
file = '/path/to/file.txt' # file | file to upload (optional)

try: 
    # uploads an image
    api_response = api_instance.controllers_pet_controller_upload_file(pet_id, additional_metadata=additional_metadata, file=file)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PetApi->controllers_pet_controller_upload_file: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | **int**| ID of pet to update | 
 **additional_metadata** | **str**| Additional data to pass to server | [optional] 
 **file** | **file**| file to upload | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

