# swagger_client.HealthstatusApi

All URIs are relative to *http://petstore.swagger.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllers_health_controller_get_status**](HealthstatusApi.md#controllers_health_controller_get_status) | **GET** / | health status


# **controllers_health_controller_get_status**
> str controllers_health_controller_get_status()

health status

health status

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthstatusApi()

try: 
    # health status
    api_response = api_instance.controllers_health_controller_get_status()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling HealthstatusApi->controllers_health_controller_get_status: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

