# Compression Configuration

```python
from axvn_common.configuration import ConfigurationRestAPI
from axvn_sdk_wallet.wallet import Wallet
from axvn_sdk_wallet.rest_api.models import AccountInfoResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret",
    compression=False
)
client = Wallet(config_rest_api=configuration)

try:
    response = client.rest_api.account_info()
    data: AccountInfoResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
