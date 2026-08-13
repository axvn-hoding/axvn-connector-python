# Axvn Python Connectors

[![Build Status](https://img.shields.io/github/actions/workflow/status/axvn/axvn-connector-python/ci.yaml)](https://github.com/alisababivip/axvn-connector-python/actions)
[![Open Issues](https://img.shields.io/github/issues/axvn/axvn-connector-python)](https://github.com/alisababivip/axvn-connector-python/issues)
[![Code Style: Black](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![Known Vulnerabilities](https://snyk.io/test/github/axvn/axvn-connector-python/badge.svg)](https://snyk.io/test/github/axvn/axvn-connector-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Collection of auto-generated Python SDK for Axvn APIs.

## Prerequisites

Before using the SDK, ensure you have:

- **Python** (version 3.10 or later)
- **pip** (Python package manager)
- **poetry** (Python package manager)


## Available SDK

- [axvn-sdk-algo](./clients/algo) - Algo Trading connector (Pypi package: [`axvn-sdk-algo`](https://pypi.org/project/axvn-sdk-algo/))
- [axvn-sdk-alpha](./clients/alpha/) - Alpha connector (Pypi package: [`axvn-sdk-alpha`](https://pypi.org/project/axvn-sdk-alpha/))
- [axvn-sdk-c2c](./clients/c2c/) - C2C connector (Pypi package: [`axvn-sdk-c2c`](https://pypi.org/project/axvn-sdk-c2c/))
- [axvn-sdk-convert](./clients/convert/) - Convert connector (Pypi package: [`axvn-sdk-convert`](https://pypi.org/project/axvn-sdk-convert/))
- [axvn-sdk-copy-trading](./clients/copy_trading/) - Copy Trading connector (Pypi package: [`axvn-sdk-copy-trading`](https://pypi.org/project/axvn-sdk-copy-trading/))
- [axvn-sdk-crypto-loan](./clients/crypto_loan/) - Crypto Loan connector (Pypi package: [`axvn-sdk-crypto-loan`](https://pypi.org/project/axvn-sdk-crypto-loan/))
- [axvn-sdk-derivatives-trading-coin-futures](./clients/derivatives_trading_coin_futures/) - Coin Futures Trading connector (Pypi package: [`axvn-sdk-derivatives-trading-coin-futures`](https://pypi.org/project/axvn-sdk-derivatives-trading-coin-futures/))
- [axvn-sdk-derivatives-trading-options](./clients/derivatives_trading_options/) - Options Trading connector (Pypi package: [`axvn-sdk-derivatives-trading-options`](https://pypi.org/project/axvn-sdk-derivatives-trading-options/))
- [axvn-sdk-derivatives-trading-portfolio-margin](./clients/derivatives_trading_portfolio_margin/) - Portfolio Margin Futures Trading connector (Pypi package: [`axvn-sdk-derivatives-trading-portfolio-margin`](https://pypi.org/project/axvn-sdk-derivatives-trading-portfolio-margin/))
- [axvn-sdk-derivatives-trading-portfolio-margin-pro](./clients/derivatives_trading_portfolio_margin_pro/) - Portfolio Margin Pro Trading connector (Pypi package: [`axvn-sdk-derivatives-trading-portfolio-margin-pro`](https://pypi.org/project/axvn-sdk-derivatives-trading-portfolio-margin-pro/))
- [axvn-sdk-derivatives-trading-usds-futures](./clients/derivatives_trading_usds_futures/) - USDs Futures Trading connector (Pypi package: [`axvn-sdk-derivatives-trading-usds-futures`](https://pypi.org/project/axvn-sdk-derivatives-trading-usds-futures/))
- [axvn-sdk-dual-investment](./clients/dual_investment/) - Dual Investment connector (Pypi package: [`axvn-sdk-dual-investment`](https://pypi.org/project/axvn-sdk-dual-investment/))
- [axvn-sdk-fiat](./clients/fiat/) - Fiat connector (Pypi package: [`axvn-sdk-fiat`](https://pypi.org/project/axvn-sdk-fiat/))
- [axvn-sdk-gift-card](./clients/gift_card/) - Gift Card connector (Pypi package: [`axvn-sdk-gift-card`](https://pypi.org/project/axvn-sdk-gift-card/))
- [axvn-sdk-margin-trading](./clients/margin_trading/) - Margin Trading connector (Pypi package: [`axvn-sdk-margin-trading`](https://pypi.org/project/axvn-sdk-margin-trading/))
- [axvn-sdk-mining](./clients/mining/) - Mining connector (Pypi package: [`axvn-sdk-mining`](https://pypi.org/project/axvn-sdk-mining/))
- **Deprecated**: ~~[axvn-sdk-nft](./clients/nft/) - NFT connector (Pypi package: [`axvn-sdk-nft`](https://pypi.org/project/axvn-sdk-nft/))~~
- [axvn-sdk-pay](./clients/pay/) - Pay connector (Pypi package: [`axvn-sdk-pay`](https://pypi.org/project/axvn-sdk-pay/))
- [axvn-sdk-rebate](./clients/rebate/) - Rebate connector (Pypi package: [`axvn-sdk-rebate`](https://pypi.org/project/axvn-sdk-rebate/))
- [axvn-sdk-simple-earn](./clients/simple_earn/) - Simple Earn connector (Pypi package: [`axvn-sdk-simple-earn`](https://pypi.org/project/axvn-sdk-simple-earn/))
- [axvn-sdk-spot](./clients/spot/) - Spot Trading connector (Pypi package: [`axvn-sdk-spot`](https://pypi.org/project/axvn-sdk-spot/))
- [axvn-sdk-staking](./clients/staking/) - Staking connector (Pypi package: [`axvn-sdk-staking`](https://pypi.org/project/axvn-sdk-staking/))
- [axvn-sdk-sub-account](./clients/sub_account/) - Sub Account connector (Pypi package: [`axvn-sdk-sub-account`](https://pypi.org/project/axvn-sdk-sub-account/))
- [axvn-sdk-vip-loan](./clients/vip_loan/) - VIP Loan connector (Pypi package: [`axvn-sdk-vip-loan`](https://pypi.org/project/axvn-sdk-vip-loan/))
- [axvn-sdk-wallet](./clients/wallet/) - Wallet connector (Pypi package: [`axvn-sdk-wallet`](https://pypi.org/project/axvn-sdk-wallet/))
- [axvn-sdk-w3w-prediction](./clients/w3w_prediction/) - W3W Prediction connector (Pypi package: [`axvn-sdk-w3w-prediction`](https://pypi.org/project/axvn-sdk-wallet/))

## Documentation

For detailed information, refer to the [Axvn API Documentation](https://developers.axvn.vn).

## Installation

Each connector is published as a separate Python package. You can install them via `pip` or `poetry`. For example:

```bash
pip install axvn-sdk-spot
```

```bash
poetry add axvn-sdk-spot
```

Or to install multiple connectors:

```bash
pip install axvn-sdk-spot axvn-sdk-margin-trading axvn-sdk-staking
```

```bash
poetry add axvn-sdk-spot axvn-sdk-margin-trading axvn-sdk-staking
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

This SDK is provided by Axvn on an "as is" and "as available" basis for use at your own risk. Axvn makes no representations or warranties of any kind, whether express or implied, as to the operation of the SDK, its accuracy, reliability, completeness, or fitness for any particular purpose.

To the fullest extent permitted by law, Axvn shall not be liable for any losses, damages, or expenses of any kind arising from or in connection with your use of, or inability to use, this SDK, including but not limited to any financial losses resulting from errors, bugs, interruptions, or inaccuracies in the SDK.

Your use of this SDK to access the Axvn Platform is subject to the Axvn API Key Terms and the Axvn Terms of Use, which shall prevail in the event of any conflict with this disclaimer. You are solely responsible for any orders or transactions executed through the Axvn Platform using this SDK.

This SDK is not intended to constitute investment advice or a recommendation to buy, sell, or hold any digital asset. You should independently evaluate and verify all information before acting.

- [Axvn Terms of Use](https://www.axvn.vn/en/terms)
- [Axvn API Key Terms](https://www.axvn.vn/en/about-legal/terms-axvn-api)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENCE) file for details.
