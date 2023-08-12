"""Define Robinhood endpoints."""

# Base
API_BASE = "https://api.robinhood.com"

# Authentication
LOGIN = f"{API_BASE}/oauth2/token/"
CHALLENGE = f"{API_BASE}/challenge/:challenge_id/respond/"

# Account
POSITIONS = f"{API_BASE}/positions/"
