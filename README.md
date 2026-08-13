# axvn-hoding Python Connectors

[![Build Status](https://img.shields.io/github/actions/workflow/status/axvn-hoding/axvn-connector-python/ci.yaml)](https://github.com/axvn-hoding/axvn-connector-python/actions)
[![Open Issues](https://img.shields.io/github/issues/axvn-hoding/axvn-connector-python)](https://github.com/axvn-hoding/axvn-connector-python/issues)
[![Code Style: Black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![Known Vulnerabilities](https://snyk.io/test/github/axvn-hoding/axvn-connector-python/badge.svg)](https://snyk.io/test/github/axvn-hoding/axvn-connector-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Collection of auto-generated Python SDK for axvn-hoding APIs.

## Prerequisites

Before using the SDK, ensure you have:

- **Python** (version 3.10 or later)
- **pip** (Python package manager)
- **poetry** (Python package manager)


## Available SDK

- [axvn-hoding-sdk-algo](./clients/algo) - Algo Trading connector (Pypi package: [`axvn-hoding-sdk-algo`](https://pypi.org/project/axvn-hoding-sdk-algo/))
- [axvn-hoding-sdk-alpha](./clients/alpha/) - Alpha connector (Pypi package: [`axvn-hoding-sdk-alpha`](https://pypi.org/project/axvn-hoding-sdk-alpha/))
- [axvn-hoding-sdk-c2c](./clients/c2c/) - C2C connector (Pypi package: [`axvn-hoding-sdk-c2c`](https://pypi.org/project/axvn-hoding-sdk-c2c/))
- [axvn-hoding-sdk-convert](./clients/convert/) - Convert connector (Pypi package: [`axvn-hoding-sdk-convert`](https://pypi.org/project/axvn-hoding-sdk-convert/))
- [axvn-hoding-sdk-copy-trading](./clients/copy_trading/) - Copy Trading connector (Pypi package: [`axvn-hoding-sdk-copy-trading`](https://pypi.org/project/axvn-hoding-sdk-copy-trading/))
- [axvn-hoding-sdk-crypto-loan](./clients/crypto_loan/) - Crypto Loan connector (Pypi package: [`axvn-hoding-sdk-crypto-loan`](https://pypi.org/project/axvn-hoding-sdk-crypto-loan/))
- [axvn-hoding-sdk-derivatives-trading-coin-futures](./clients/derivatives_trading_coin_futures/) - Coin Futures Trading connector (Pypi package: [`axvn-hoding-sdk-derivatives-trading-coin-futures`](https://pypi.org/project/axvn-hoding-sdk-derivatives-trading-coin-futures/))
- [axvn-hoding-sdk-derivatives-trading-options](./clients/derivatives_trading_options/) - Options Trading connector (Pypi package: [`axvn-hoding-sdk-derivatives-trading-options`](https://pypi.org/project/axvn-hoding-sdk-derivatives-trading-options/))
- [axvn-hoding-sdk-derivatives-trading-portfolio-margin](./clients/derivatives_trading_portfolio_margin/) - Portfolio Margin Futures Trading connector (Pypi package: [`axvn-hoding-sdk-derivatives-trading-portfolio-margin`](https://pypi.org/project/axvn-hoding-sdk-derivatives-trading-portfolio-margin/))
- [axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro](./clients/derivatives_trading_portfolio_margin_pro/) - Portfolio Margin Pro Trading connector (Pypi package: [`axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro`](https://pypi.org/project/axvn-hoding-sdk-derivatives-trading-portfolio-margin-pro/))
- [axvn-hoding-sdk-derivatives-trading-usds-futures](./clients/derivatives_trading_usds_futures/) - USDs Futures Trading connector (Pypi package: [`axvn-hoding-sdk-derivatives-trading-usds-futures`](https://pypi.org/project/axvn-hoding-sdk-derivatives-trading-usds-futures/))
- [axvn-hoding-sdk-dual-investment](./clients/dual_investment/) - Dual Investment connector (Pypi package: [`axvn-hoding-sdk-dual-investment`](https://pypi.org/project/axvn-hoding-sdk-dual-investment/))
- [axvn-hoding-sdk-fiat](./clients/fiat/) - Fiat connector (Pypi package: [`axvn-hoding-sdk-fiat`](https://pypi.org/project/axvn-hoding-sdk-fiat/))
- [axvn-hoding-sdk-gift-card](./clients/gift_card/) - Gift Card connector (Pypi package: [`axvn-hoding-sdk-gift-card`](https://pypi.org/project/axvn-hoding-sdk-gift-card/))
- [axvn-hoding-sdk-margin-trading](./clients/margin_trading/) - Margin Trading connector (Pypi package: [`axvn-hoding-sdk-margin-trading`](https://pypi.org/project/axvn-hoding-sdk-margin-trading/))
- [axvn-hoding-sdk-mining](./clients/mining/) - Mining connector (Pypi package: [`axvn-hoding-sdk-mining`](https://pypi.org/project/axvn-hoding-sdk-mining/))
- **Deprecated**: ~~[axvn-hoding-sdk-nft](./clients/nft/) - NFT connector (Pypi package: [`axvn-hoding-sdk-nft`](https://pypi.org/project/axvn-hoding-sdk-nft/))~~
- [axvn-hoding-sdk-pay](./clients/pay/) - Pay connector (Pypi package: [`axvn-hoding-sdk-pay`](https://pypi.org/project/axvn-hoding-sdk-pay/))
- [axvn-hoding-sdk-rebate](./clients/rebate/) - Rebate connector (Pypi package: [`axvn-hoding-sdk-rebate`](https://pypi.org/project/axvn-hoding-sdk-rebate/))
- [axvn-hoding-sdk-simple-earn](./clients/simple_earn/) - Simple Earn connector (Pypi package: [`axvn-hoding-sdk-simple-earn`](https://pypi.org/project/axvn-hoding-sdk-simple-earn/))
- [axvn-hoding-sdk-spot](./clients/spot/) - Spot Trading connector (Pypi package: [`axvn-hoding-sdk-spot`](https://pypi.org/project/axvn-hoding-sdk-spot/))
- [axvn-hoding-sdk-staking](./clients/staking/) - Staking connector (Pypi package: [`axvn-hoding-sdk-staking`](https://pypi.org/project/axvn-hoding-sdk-staking/))
- [axvn-hoding-sdk-sub-account](./clients/sub_account/) - Sub Account connector (Pypi package: [`axvn-hoding-sdk-sub-account`](https://pypi.org/project/axvn-hoding-sdk-sub-account/))
- [axvn-hoding-sdk-vip-loan](./clients/vip_loan/) - VIP Loan connector (Pypi package: [`axvn-hoding-sdk-vip-loan`](https://pypi.org/project/axvn-hoding-sdk-vip-loan/))
- [axvn-hoding-sdk-wallet](./clients/wallet/) - Wallet connector (Pypi package: [`axvn-hoding-sdk-wallet`](https://pypi.org/project/axvn-hoding-sdk-wallet/))
- [axvn-hoding-sdk-w3w-prediction](./clients/w3w_prediction/) - W3W Prediction connector (Pypi package: [`axvn-hoding-sdk-w3w-prediction`](https://pypi.org/project/axvn-hoding-sdk-wallet/))

## Documentation

For detailed information, refer to the [axvn-hoding API Documentation](https://developers.axvn.vn).

## Installation

Each connector is published as a separate Python package. You can install them via `pip` or `poetry`. For example:

```bash
pip install axvn-hoding-sdk-spot
```

```bash
poetry add axvn-hoding-sdk-spot
```

Or to install multiple connectors:

```bash
pip install axvn-hoding-sdk-spot axvn-hoding-sdk-margin-trading axvn-hoding-sdk-staking
```

```bash
poetry add axvn-hoding-sdk-spot axvn-hoding-sdk-margin-trading axvn-hoding-sdk-staking
```

## Contributing

Since this repository contains auto-generated code using OpenAPI Generator, we encourage you to:

1. Open a GitHub issue to discuss your ideas or report bugs
2. Allow maintainers to implement necessary changes through the code generation process

## Code Style

This repository follows **PEP 8** standards and enforces **Black** for formatting. Before submitting a pull request, format your code:

```bash
black .
```

Run type checks:

```bash
mypy .
```

## Migration Guide

If you're upgrading from the previous unified connector, refer to our [Migration Guide](./MIGRATION.md) for detailed steps on transitioning to the new modular structure.

## Disclaimer

This SDK is provided by axvn-hoding on an "as is" and "as available" basis for use at your own risk. axvn-hoding makes no representations or warranties of any kind, whether express or implied, as to the operation of the SDK, its accuracy, reliability, completeness, or fitness for any particular purpose.

To the fullest extent permitted by law, axvn-hoding shall not be liable for any losses, damages, or expenses of any kind arising from or in connection with your use of, or inability to use, this SDK, including but not limited to any financial losses resulting from errors, bugs, interruptions, or inaccuracies in the SDK.

Your use of this SDK to access the axvn-hoding Platform is subject to the axvn-hoding API Key Terms and the axvn-hoding Terms of Use, which shall prevail in the event of any conflict with this disclaimer. You are solely responsible for any orders or transactions executed through the axvn-hoding Platform using this SDK.

This SDK is not intended to constitute investment advice or a recommendation to buy, sell, or hold any digital asset. You should independently evaluate and verify all information before acting.

- [axvn-hoding Terms of Use](https://www.axvn.vn/en/terms)
- [axvn-hoding API Key Terms](https://www.axvn.vn/en/about-legal/terms-axvn-hoding-api)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENCE) file for details.
