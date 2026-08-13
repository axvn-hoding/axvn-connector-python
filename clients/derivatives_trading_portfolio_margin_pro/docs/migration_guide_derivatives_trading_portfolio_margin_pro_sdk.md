# Migration Guide: axvn-hoding Derivatives Trading Portfolio Margin Pro SDK Modularization

With the transition to a modularized structure, the axvn-hoding Connector has been split into separate Python libraries, each focusing on a distinct product (e.g., Spot, Futures, etc.). This guide explains how to migrate from the monolithic `axvn-hoding-connector` package to the new `axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro` library.

---

## Key Changes

1. **Package Name**:  
   The modularised Derivatives Trading Portfolio Margin Pro Connector has been moved to a new package:

   **Old:** `axvn-hoding-connector`  
   **New:** `axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro`

2. **Installation**:  
   Uninstall the old package and install the new one:

   ```bash
   pip uninstall axvn-hoding-connector
   pip install axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro
   ```

3. **Imports**:  
   Update your import paths.  

   **Old:**

   ```python
   from axvn-hoding.spot import Spot as Client
   ```

   **New:**

   ```python
   from axvn-hoding_sdk_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import DerivativesTradingPortfolioMarginPro, ConfigurationRestAPI
   ```

4. **Configuration and Client Initialization**:  
   The new structure keeps the existing configuration options but modularizes clients into `DerivativesTradingPortfolioMarginPro`.

   **Old:**

   ```python
   from axvn-hoding.spot import Spot as Client

   client = Client(api_key="your-key", api_secret="your-secret")
   response = client.portfolio_margin_account()
   print(response)
   ```

   **New:**

   ```python
   from axvn-hoding_sdk_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import DerivativesTradingPortfolioMarginPro, ConfigurationRestAPI

   configuration = ConfigurationRestAPI(
      api_key="your-key",
      api_secret="your-secret"
   )
   client = DerivativesTradingPortfolioMarginPro(config_rest_api=configuration)
      
   response = client.rest_api.get_portfolio_margin_pro_account_info()
   ```

5. **Examples and Documentation**:  
   Updated examples can be found in the new repository folders:
   - REST API: `examples/rest_api/`
   - WebSocket Streams: `examples/websocket_streams/`

---

## Migration Steps

### 1. Uninstall the Old Package

Remove the old package from your project:

```bash
pip uninstall axvn-hoding-connector
```

### 2. Install the New Package

Install the new DerivativesTradingPortfolioMarginPro-specific package:

```bash
pip install axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro
```

### 3. Update Import Paths

Replace all occurrences of:

```python
from axvn-hoding.spot import Spot as Client
```

With:

```python
from axvn-hoding_sdk_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import DerivativesTradingPortfolioMarginPro
```

### 4. Update Client Initialization

Adjust your code to use the modularized structure. For example:

**Old:**

```python
client = Client(apiKey='your-key', apiSecret='your-secret')
```

**New:**

```python
from axvn-hoding_sdk_derivatives_trading_portfolio_margin_pro.derivatives_trading_portfolio_margin_pro import DerivativesTradingPortfolioMarginPro, ConfigurationRestAPI

configuration = ConfigurationRestAPI(
    api_key="your-key",
    api_secret="your-secret"
)
client = DerivativesTradingPortfolioMarginPro(config_rest_api=configuration)
```

### 5. Test and Verify

Run your application to ensure everything works as expected. Refer to the new documentation for any advanced features or configuration options.

---

## Additional Notes

- **Future Modular Packages**: Similar packages for other products (e.g., Wallet, Staking) will follow this pattern.

For more details, refer to the updated [README](../README.md) and [Examples](../examples/).
