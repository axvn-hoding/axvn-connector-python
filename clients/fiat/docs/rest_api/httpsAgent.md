# HTTPS Agent Configuration

```python
import ssl

from axvn_common.configuration import ConfigurationRestAPI
from axvn_sdk_fiat.fiat import Fiat
from axvn_sdk_fiat.rest_api.models import GetFiatDepositWithdrawHistoryResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    https_agent=ssl.create_default_context()
)
client = Fiat(config_rest_api=configuration)

try:
    response = client.rest_api.get_fiat_deposit_withdraw_history()
    data: GetFiatDepositWithdrawHistoryResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
