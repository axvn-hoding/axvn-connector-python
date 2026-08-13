# Timeout

```python
from axvn_common.configuration import ConfigurationRestAPI
from axvn_sdk_staking.staking import Staking
from axvn_sdk_staking.rest_api.models import ClaimBoostRewardsResponse

configuration = ConfigurationRestAPI(
    api_key="your-api-key",
    api_secret="your-api-secret"
)
client =  Staking(config_rest_api=configuration)

try:
    response = client.rest_api.claim_boost_rewards()
    data: ClaimBoostRewardsResponse = response.data()
    print(data)
except Exception as e:
    logging.error(f"error: {e}")
```
