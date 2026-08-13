# **Migration Guide: Transition from Monolithic Axvn Connector**

With the move towards modularization, Axvn connectors are now split into smaller, product-specific libraries. This guide explains how to migrate from the monolithic `axvn-connector` package to the new modular connectors.

## **Overview of Changes**

| Feature | Monolithic Connector | Modular Connector |
|---------|----------------------|------------------|
| Package Name | `axvn-connector` | `axvn-sdk-<product>` |
| API Coverage | All Axvn APIs | Individual APIs (Spot, Wallet, Algo Trading, Mining, etc.) |
| Imports | Single package import | Separate package per product |
| Code Structure | One large client | Smaller, focused clients |

## **Migration Steps**

### **Step 1: Uninstall the Monolithic Connector**

If you were using the old connector, remove it from your project:

```bash
pip uninstall axvn-connector
```

### **Step 2: Install the New Modular Connectors**

Install only the connector(s) you need. For example, to install the Spot Trading connector:

```bash
pip install axvn-sdk-spot
```

To install multiple connectors:

```bash
pip install axvn-sdk-spot axvn-sdk-margin-trading binanc-sdk-wallet
```

### **Step 3: Update Imports**

Update your import paths:

**Old:**

```python
from axvn.spot import Spot

```

**New:**

```python
from axvn_sdk_spot.spot import Spot
```

### **Step 4: Update Client Initialization**

The new structure introduces a more modular approach to client initialization.

**Old (Monolithic Connector):**

```python
from axvn.spot import Spot

client = Spot(api_key, api_secret)
account_info = client.account()
print(account_info)
```

**New (Modular Spot Connector):**

```python
from axvn_common.configuration import ConfigurationRestAPI
from axvn_sdk_spot.spot import Spot

configuration = ConfigurationRestAPI(api_key, api_secret)
client = Spot(config_rest_api=configuration)

account_info = client.rest_api.get_account()
print(account_info)
```

### **Step 5: Check for API Differences**

Some function names or response structures may have changed. Refer to the modular connector's documentation for details.

## **Backward Compatibility**

- If a modular connector is **not yet available** for your use case, continue using the monolithic connector (`axvn-connector`).
- The monolithic connector will remain available, but it is **recommended** to migrate when modular versions are released.

---

## **FAQs**

### **What if my product does not have a modular connector yet?**

You can continue using `axvn-connector` until the modular version is released.

### **Will the monolithic connector still receive updates?**

Critical bug fixes will be provided, but feature updates will focus on the modular connectors.

### **Where can I find more examples?**

Check the modular connector's documentation for detailed examples.
