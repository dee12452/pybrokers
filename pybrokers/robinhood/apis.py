"""robinhood.py: a collection of utilities for working with Robinhood's Private API."""
from typing import Optional, Dict, Any
from uuid import uuid4

import requests

from pybrokers.exceptions import AuthenticationError, BrokerException
from pybrokers.robinhood.responses import LoginResponse, HeldStocksResponse, HeldStock
from pybrokers.robinhood.urls import LOGIN, CHALLENGE, POSITIONS


def login(email: str, password: str, device_token: Optional[str], challenge_id: Optional[str], mfa: Optional[str]) -> LoginResponse:
    payload: Dict[str, Any] = {
        "client_id": "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS",
        "expires_in": 86400,
        "grant_type": "password",
        "password": password,
        "scope": "internal",
        "username": email,
        "challenge_type": "sms",
        "device_token": device_token or str(uuid4()),
    }
    if mfa:
        payload['mfa_code'] = mfa

    headers: Dict[str, Any] = {}
    if challenge_id:
        headers['X-ROBINHOOD-CHALLENGE-RESPONSE-ID'] = challenge_id

    response = requests.post(LOGIN, json=payload, headers=headers)
    if not response:
        raise BrokerException('No response from robinhood. Verify internet connection is available.')

    data = response.json()
    if 'access_token' in data:
        return LoginResponse(access_token=data['access_token'])

    if 'challenge' in data:
        return LoginResponse(challenge_required=True, challenge_id=data['challenge']['id'])

    if 'mfa_required' in data:
        return LoginResponse(mfa_required=True)

    raise AuthenticationError(data.get('detail', 'Unknown error when attempting to login.'))


def challenge(challenge_id: str, challenge_response: str) -> str:
    payload: Dict[str, Any] = {
        "response": challenge_response,
    }

    url = CHALLENGE.replace(':challenge_id', challenge_id)
    response = requests.post(url, json=payload)
    if not response:
        raise BrokerException('No response from robinhood. Verify internet connection is available.')

    data = response.json()

    if data.get('status', '') == 'validated':
        return challenge_id

    raise AuthenticationError(data.get('detail', 'Challenge failed. Please try again.'))


def fetch_held_stocks(access_token: str) -> HeldStocksResponse:
    headers: Dict[str, Any] = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(POSITIONS, headers=headers)
    if not response:
        raise BrokerException('No response from robinhood. Verify internet connection is available.')

    stocks_response: HeldStocksResponse = HeldStocksResponse()
    collecting_responses = True
    while collecting_responses:
        data = response.json()
        new_held_stocks = [HeldStock.from_dict(held_stock) for held_stock in data.get("results", [])]
        stocks_response.held_stocks.extend(new_held_stocks)
        next_url = data.get("next")
        if not next_url:
            collecting_responses = False
        else:
            response = requests.get(next_url, headers=headers)
            if not response:
                raise BrokerException('No response from robinhood. Verify internet connection is available.')

    return stocks_response
