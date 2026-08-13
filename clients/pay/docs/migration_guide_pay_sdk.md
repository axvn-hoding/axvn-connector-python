# Migration Guide: Axvn Pay SDK Modularization

With the transition to a modularized structure, the Axvn Connector has been split into separate Python libraries, each focusing on a distinct product (e.g., Spot, Futures, etc.). This guide explains how to migrate from the monolithic `axvn-connector` package to the new `axvn-sdk-pay` library.

---

## Key Changes

1. **Package Name**:  
   The modularised Pay Connector has been moved to a new package:

   **Old:** `axvn-connector`  
   **New:** `axvn-sdk-pay`

2. **Installation**:  
   Uninstall the old package and install the new one:

   ```bash
   pip uninstall axvn-connector
   pip install axvn-sdk-pay
   ```

3. **Imports**:  
   Update your import paths.  

   **Old:**

   ```python
   from axvn.spot import Spot as Client
   ```

   **New:**

   ```python
   from axvn_sdk_pay.pay import Pay, ConfigurationRestAPI
   ```

4. **Configuration and Client Initialization**:  
   The new structure keeps the existing configuration options but modularizes clients into `Pay`.

   **Old:**

   ```python
   from axvn.spot import Spot as Client

   client = Client(api_key="your-key", api_secret="your-secret")
   response = client.pay_history(startTimestamp=1637186702000, limit=50)
   print(response)
   ```

   **New:**

   ```python
   from axvn_sdk_pay.pay import Pay, ConfigurationRestAPI

   configuration = ConfigurationRestAPI(
      api_key="your-key",
      api_secret="your-secret"
   )
   client = Pay(config_rest_api=configuration)
      
   response = client.rest_api.get_pay_trade_history(startTimestamp=1637186702000, limit=50)
   ```

5. **Examples and Documentation**:  
   Updated examples can be found in the new repository folders:
   - REST API: `examples/rest_api/`

---

## Migration Steps

### 1. Uninstall the Old Package

Remove the old package from your project:

```bash
pip uninstall axvn-connector
```

### 2. Install the New Package

Install the new Pay-specific package:

```bash
pip install axvn-sdk-pay
```

### 3. Update Import Paths

Replace all occurrences of:

```python
from axvn.spot import Spot as Client
```

With:

```python
from axvn_sdk_pay.pay import Pay
```

### 4. Update Client Initialization

Adjust your code to use the modularized structure. For example:

**Old:**

```python
client = Client(apiKey='your-key', apiSecret='your-secret')
```

**New:**

```python
from axvn_sdk_pay.pay import Pay, ConfigurationRestAPI

configuration = ConfigurationRestAPI(
    api_key="your-key",
    api_secret="your-secret"
)
client = Pay(config_rest_api=configuration)
```

### 5. Test and Verify

Run your application to ensure everything works as expected. Refer to the new documentation for any advanced features or configuration options.

---

## Additional Notes

- **Future Modular Packages**: Similar packages for other products (e.g., Wallet, Staking) will follow this pattern.

For more details, refer to the updated [README](../README.md) and [Examples](../examples/).
