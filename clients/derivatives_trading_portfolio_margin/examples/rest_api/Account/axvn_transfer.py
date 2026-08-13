import os
import logging

from axvn_sdk_derivatives_trading_portfolio_margin.derivatives_trading_portfolio_margin import (
    DerivativesTradingPortfolioMargin,
    ConfigurationRestAPI,
    DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL,
)
from axvn_sdk_derivatives_trading_portfolio_margin.rest_api.models import (
    BnbTransferTransferSideEnum,
)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Create configuration for the REST API
configuration_rest_api = ConfigurationRestAPI(
    api_key=os.getenv("API_KEY", ""),
    api_secret=os.getenv("API_SECRET", ""),
    base_path=os.getenv(
        "BASE_PATH", DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL
    ),
)

# Initialize DerivativesTradingPortfolioMargin client
client = DerivativesTradingPortfolioMargin(config_rest_api=configuration_rest_api)


def axvn_transfer():
    try:
        response = client.rest_api.axvn_transfer(
            amount=1.0,
            transfer_side=BnbTransferTransferSideEnum["TO_UM"].value,
        )

        rate_limits = response.rate_limits
        logging.info(f"axvn_transfer() rate limits: {rate_limits}")

        data = response.data()
        logging.info(f"axvn_transfer() response: {data}")
    except Exception as e:
        logging.error(f"axvn_transfer() error: {e}")


if __name__ == "__main__":
    axvn_transfer()
