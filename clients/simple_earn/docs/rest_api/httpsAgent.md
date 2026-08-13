# HTTPS Agent Configuration

```python
import ssl

from axvn_common.configuration import ConfigurationRestAPI
from axvn_sdk_simple_earn.simple_earn import SimpleEarn
from axvn_sdk_simple_earn.rest_api.models import GetSimpleEarnLockedProductListResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = SimpleEarn(config_rest_api=configuration)

try:
    response = client.rest_api.get_simple_earn_flexible_product_list()
    data: GetSimpleEarnLockedProductListResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
