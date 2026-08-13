# HTTPS Agent Configuration

```python
import ssl

from axvn_common.configuration import ConfigurationRestAPI
from axvn_sdk_rebate.rebate import Rebate
from axvn_sdk_rebate.rest_api.models import GetSpotRebateHistoryRecordsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = Rebate(config_rest_api=configuration)

try:
    response = client.rest_api.get_spot_rebate_history_records()
    data: GetSpotRebateHistoryRecordsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
