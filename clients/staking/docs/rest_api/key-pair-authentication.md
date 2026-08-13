# Key Pair Based Authentication

```python
from axvn-hoding_common.configuration import ConfigurationRestAPI
from axvn-hoding_sdk_staking.staking import Staking
from axvn-hoding_sdk_staking.rest_api.models import ClaimBoostRewardsResponse

with open("/path/to/private_key.pem", "r") as key_file:
    private_key = key_file.read()
private_key_passphrase = "your-passphrase"

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    private_key=private_key,
    private_key_passphrase=private_key_passphrase,
)
client = Staking(config_rest_api=configuration)

try:
    response = client.rest_api.claim_boost_rewards()
    data: ClaimBoostRewardsResponse = response.data()
    print(data)
except Exception as e:
    print(e)
```
