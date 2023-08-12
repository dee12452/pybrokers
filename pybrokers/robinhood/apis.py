"""robinhood.py: a collection of utilities for working with Robinhood's Private API."""
from typing import Optional, Dict, Any, Callable, List
from uuid import uuid4

import requests

from pybrokers.exceptions import AuthenticationError, BrokerException
from pybrokers.robinhood.responses import LoginResponse, HeldStocksResponse, HeldStock, HeldOptionsResponse, HeldOption, \
    OptionInfoResponse, OrdersResponse, OrderResponse, StockQuoteResponse, OptionOrdersResponse, OptionOrderResponse
from pybrokers.robinhood.urls import LOGIN, CHALLENGE, STOCK_POSITIONS, OPTION_INFO, STOCK_QUOTE, OPTION_POSITIONS, \
    ORDERS, OPTION_ORDERS


def login(email: str,
          password: str,
          device_token: Optional[str],
          challenge_id: Optional[str],
          mfa: Optional[str]) -> LoginResponse:
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
        return LoginResponse(access_token=data['access_token'], device_id=device_token)

    if 'challenge' in data:
        return LoginResponse(challenge_required=True, challenge_id=data['challenge']['id'], device_id=device_token)

    if 'mfa_required' in data:
        return LoginResponse(mfa_required=True, device_id=device_token)

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
    headers: Dict[str, Any] = _create_headers(access_token)
    stocks_response: HeldStocksResponse = HeldStocksResponse()

    def _collect_responses(data: Dict[str, Any]):
        new_held_stocks = [HeldStock.from_dict(held_stock) for held_stock in data.get("results", [])]
        stocks_response.held_stocks.extend(new_held_stocks)

    _get_paginated(STOCK_POSITIONS, headers=headers, response_collector=lambda data: _collect_responses(data))
    return stocks_response


def fetch_stock_quote(access_token: str, instrument_id: str) -> StockQuoteResponse:
    data: Dict[str, Any] = _get(STOCK_QUOTE.replace(":instrument_id", instrument_id), _create_headers(access_token))
    return StockQuoteResponse.from_dict(data)


def fetch_held_options(access_token: str) -> HeldOptionsResponse:
    headers: Dict[str, Any] = _create_headers(access_token)
    options_response: HeldOptionsResponse = HeldOptionsResponse()

    def _collect_responses(data: Dict[str, Any]):
        new_held_options = [HeldOption.from_dict(held_option) for held_option in data.get("results", [])]
        options_response.held_options.extend(new_held_options)

    _get_paginated(OPTION_POSITIONS, headers=headers, response_collector=lambda data: _collect_responses(data))
    return options_response


def fetch_option_info(access_token: str, option_id: str) -> OptionInfoResponse:
    data: Dict[str, Any] = _get(OPTION_INFO.replace(":option_id", option_id), _create_headers(access_token))
    return OptionInfoResponse.from_dict(data)


def fetch_orders(access_token: str) -> OrdersResponse:
    headers: Dict[str, Any] = _create_headers(access_token)
    orders_response = OrdersResponse()

    def _collect_responses(data: Dict[str, Any]):
        new_order = [OrderResponse.from_dict(order) for order in data.get("results", [])]
        orders_response.orders.extend(new_order)

    _get_paginated(ORDERS, headers=headers, response_collector=lambda data: _collect_responses(data))

    return orders_response


def fetch_option_orders(access_token: str) -> OptionOrdersResponse:
    headers: Dict[str, Any] = _create_headers(access_token)
    orders_response = OptionOrdersResponse()

    def _collect_responses(data: Dict[str, Any]):
        new_option_order = [OptionOrderResponse.from_dict(order) for order in data.get("results", [])]
        orders_response.option_orders.extend(new_option_order)

    _get_paginated(OPTION_ORDERS, headers=headers, response_collector=lambda data: _collect_responses(data))

    return orders_response


def _create_headers(access_token: str, additional_headers: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    headers = {
        'Authorization': f"Bearer {access_token}",
    }
    if additional_headers:
        for additional_header in additional_headers:
            headers.update(additional_header)

    return headers


def _get(url: str, headers: Dict[str, Any]) -> Dict[str, Any]:
    response = requests.get(url, headers=headers)
    if not response:
        raise BrokerException('No response from robinhood. Verify internet connection is available.')

    return response.json()


def _get_paginated(initial_url: str,
                   headers: Dict[str, Any],
                   response_collector: Callable[[Dict[str, Any]], None]) -> None:
    response = requests.get(initial_url, headers=headers)
    if not response:
        raise BrokerException('No response from robinhood. Verify internet connection is available.')

    collecting_responses = True
    while collecting_responses:
        data = response.json()
        response_collector(data)
        next_url = data.get("next")
        if next_url:
            response = requests.get(next_url, headers=headers)
            if not response:
                raise BrokerException('No response from robinhood. Verify internet connection is available.')
            continue

        collecting_responses = False
