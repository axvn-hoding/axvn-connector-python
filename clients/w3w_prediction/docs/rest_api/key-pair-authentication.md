# Key Pair Based Authentication

```python
from axvn-hoding_common.configuration import ConfigurationRestAPI
from axvn-hoding_sdk_w3w_prediction.w3w_prediction import W3wPrediction
from axvn-hoding_sdk_w3w_prediction.rest_api.models import ListPredictionCategoriesResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = W3wPrediction(config_rest_api=configuration)

try:
    response = client.rest_api.list_prediction_categories()
    data: ListPredictionCategoriesResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
