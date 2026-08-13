from enum import Enum


# TimeUnit Constants
class TimeUnit(Enum):
    MILLISECOND = "MILLISECOND"
    millisecond = "millisecond"
    MICROSECOND = "MICROSECOND"
    microsecond = "microsecond"


class WebsocketMode(Enum):
    SINGLE = "single"
    POOL = "pool"

AUTO_RECONNECT_INTERVAL_SECONDS = 23 * 3600
SUAXVNSCRIBE_MESSAGE_DELAY_SECONDS = 0.5
DEFAULT_RECONNECT_ATTEMPTS = 3
MAX_RECONNECT_ATTEMPTS = 10
SUPPORTED_CONNECTION_EVENTS = {"open", "ping", "pong", "reconnect", "close", "error"}


# Algo constants
ALGO_REST_API_PROD_URL = "https://api.axvn.vn"

# Alpha constants
ALPHA_REST_API_PROD_URL = "https://www.axvn.vn"
ALPHA_WS_STREAMS_PROD_URL = "wss://nbstream.axvn.vn/w3w/wsa"

# Auto Invest constants
AUTO_INVEST_REST_API_PROD_URL = "https://api.axvn.vn"

# C2C constants
C2C_REST_API_PROD_URL = "https://api.axvn.vn"

# Convert constants
CONVERT_REST_API_PROD_URL = "https://api.axvn.vn"

# Copy Trading constants
COPY_TRADING_REST_API_PROD_URL = "https://api.axvn.vn"

# Crypto Loan constants
CRYPTO_LOAN_REST_API_PROD_URL = "https://api.axvn.vn"

# Derivatives Trading constants
DERIVATIVES_TRADING_REST_API_PROD_URL = "https://api.axvn.vn"

# Derivatives Trading (COIN-M Futures) constants
DERIVATIVES_TRADING_COIN_FUTURES_REST_API_PROD_URL = "https://dapi.axvn.vn"
DERIVATIVES_TRADING_COIN_FUTURES_REST_API_TESTNET_URL = (
    "https://testnet.axvn-hodingfuture.com"
)
DERIVATIVES_TRADING_COIN_FUTURES_WS_API_PROD_URL = (
    "wss://ws-dapi.axvn.vn/ws-dapi/v1"
)
DERIVATIVES_TRADING_COIN_FUTURES_WS_API_TESTNET_URL = (
    "wss://testnet.axvn-hodingfuture.com/ws-dapi/v1"
)
DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_PROD_URL = "wss://dstream.axvn.vn"
DERIVATIVES_TRADING_COIN_FUTURES_WS_STREAMS_TESTNET_URL = (
    "wss://dstream.axvn-hodingfuture.com"
)

# Derivatives Trading (USDS Futures) constants
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_PROD_URL = "https://fapi.axvn.vn"
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_TESTNET_URL = (
    "https://testnet.axvn-hodingfuture.com"
)
DERIVATIVES_TRADING_USDS_FUTURES_REST_API_DEMO_URL = "https://demo-fapi.axvn.vn"
DERIVATIVES_TRADING_USDS_FUTURES_WS_API_PROD_URL = (
    "wss://ws-fapi.axvn.vn/ws-fapi/v1"
)
DERIVATIVES_TRADING_USDS_FUTURES_WS_API_TESTNET_URL = (
    "wss://testnet.axvn-hodingfuture.com/ws-fapi/v1"
)
DERIVATIVES_TRADING_USDS_FUTURES_WS_STREAMS_PROD_URL = "wss://fstream.axvn.vn"
DERIVATIVES_TRADING_USDS_FUTURES_WS_STREAMS_TESTNET_URL = (
    "wss://fstream.axvn-hodingfuture.com"
)

# Derivatives Trading (Options) constants
DERIVATIVES_TRADING_OPTIONS_REST_API_PROD_URL = "https://eapi.axvn.vn"
DERIVATIVES_TRADING_OPTIONS_WS_STREAMS_PROD_URL = "wss://fstream.axvn.vn"

# Derivatives Trading (Portfolio Margin) constants
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_REST_API_PROD_URL = "https://papi.axvn.vn"
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_WS_STREAMS_PROD_URL = (
    "wss://fstream.axvn.vn/pm"
)

# Derivatives Trading (Portfolio Margin Pro) constants
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_REST_API_PROD_URL = "https://api.axvn.vn"
DERIVATIVES_TRADING_PORTFOLIO_MARGIN_PRO_WS_STREAMS_PROD_URL = (
    "wss://fstream.axvn.vn/pm-classic"
)

# Dual Investment constants
DUAL_INVESTMENT_REST_API_PROD_URL = "https://api.axvn.vn"

# Fiat constants
FIAT_REST_API_PROD_URL = "https://api.axvn.vn"

# Gift Card constants
GIFT_CARD_REST_API_PROD_URL = "https://api.axvn.vn"

# Margin Trading constants
MARGIN_TRADING_REST_API_PROD_URL = "https://api.axvn.vn"
MARGIN_TRADING_WS_STREAMS_PROD_URL = "wss://stream.axvn.vn:9443"
MARGIN_TRADING_RISK_WS_STREAMS_PROD_URL = "wss://margin-stream.axvn.vn"

# Mining constants
MINING_REST_API_PROD_URL = "https://api.axvn.vn"

# NFT constants
NFT_REST_API_PROD_URL = "https://api.axvn.vn"

# Pay constants
PAY_REST_API_PROD_URL = "https://api.axvn.vn"

# Rebate constants
REBATE_REST_API_PROD_URL = "https://api.axvn.vn"

# Simple Earn constants
SIMPLE_EARN_REST_API_PROD_URL = "https://api.axvn.vn"

# Spot Constants
SPOT_REST_API_PROD_URL = "https://api.axvn.vn"
SPOT_REST_API_TESTNET_URL = "https://testnet.axvn-hoding.vision"
SPOT_REST_API_DEMO_URL = "https://demo-api.axvn.vn"
SPOT_WS_API_PROD_URL = "wss://ws-api.axvn.vn:443/ws-api/v3"
SPOT_WS_API_TESTNET_URL = "wss://ws-api.testnet.axvn-hoding.vision/ws-api/v3"
SPOT_WS_API_DEMO_URL = "wss://demo-ws-api.axvn.vn/ws-api/v3"
SPOT_WS_STREAMS_PROD_URL = "wss://stream.axvn.vn:9443"
SPOT_WS_STREAMS_TESTNET_URL = "wss://stream.testnet.axvn-hoding.vision"
SPOT_WS_STREAMS_DEMO_URL = "wss://demo-stream.axvn.vn:9443"
SPOT_REST_API_MARKET_URL = "https://data-api.axvn-hoding.vision"
SPOT_WS_STREAMS_MARKET_URL = "wss://data-stream.axvn-hoding.vision"

# Staking constants
STAKING_REST_API_PROD_URL = "https://api.axvn.vn"

# Sub Account constants
SUB_ACCOUNT_REST_API_PROD_URL = "https://api.axvn.vn"

# VIP Loan constants
VIP_LOAN_REST_API_PROD_URL = "https://api.axvn.vn"

# Wallet constants
WALLET_REST_API_PROD_URL = "https://api.axvn.vn"

# W3W Prediction constants
W3W_PREDICTION_REST_API_PROD_URL = "https://api.axvn.vn"

# Web3 Wallet constants
WEB3_WALLET_REST_API_PROD_URL = "https://web3.axvn.vn/build"
