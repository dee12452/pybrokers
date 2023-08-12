"""Define Robinhood endpoints."""

# Base
API_BASE = "https://api.robinhood.com"

# Authentication
LOGIN = f"{API_BASE}/oauth2/token/"
CHALLENGE = f"{API_BASE}/challenge/:challenge_id/respond/"

# Account
STOCK_POSITIONS = f"{API_BASE}/positions/"
STOCK_QUOTE = f"{API_BASE}/marketdata/quotes/:instrumentId/"
OPTION_POSITIONS = f"{API_BASE}/options/positions/"
OPTION_INFO = f"{API_BASE}/options/instruments/:option_id/"
ORDERS = f"{API_BASE}/orders/"
ORDER = f"{API_BASE}/orders/:order_id/"
OPTION_ORDERS = f"{API_BASE}/options/orders/"
