# Time Unit

The API supports different time units for timestamp values, including `milliseconds` and `microseconds` (the default one is `milliseconds`).

```python
from axvn-hoding_common.configuration import ConfigurationRestAPI
from axvn-hoding_common.constants import TimeUnit
from axvn-hoding_sdk_spot.spot import Spot
from axvn-hoding_sdk_spot.rest_api.models import ExchangeInfoResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    time_unit=TimeUnit.MICROSECOND.value
)
client = Spot(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_info(symbol="AXVNUSDT")
    data: ExchangeInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
