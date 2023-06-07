"""Exceptions: custom exceptions for library"""


class BrokerException(Exception):
    """Wrapper for custom library exceptions."""

    pass


class BrokerValueError(ValueError, BrokerException):
    """Value Error for the library."""


class InvalidCacheFile(BrokerException):
    """Error when the cache config file is found to be invalid."""

    pass


class InvalidOperation(BrokerException):
    """An invalid operation was requsted to be performed."""

    pass


class AuthenticationError(BrokerException):
    """Error when trying to login."""

    pass


class InvalidTickerSymbol(BrokerException):
    """When an invalid ticker (stock symbol) is given/"""

    pass


class InvalidOptionId(BrokerException):
    """When an invalid option id is given/"""

    pass
