from typing import Optional, List, Dict, Any

from attrs import define


@define
class LoginResponse:
    device_id: str
    access_token: Optional[str] = None
    challenge_required: bool = False
    challenge_id: Optional[str] = None
    mfa_required: Optional[bool] = False


@define
class HeldStock:
    url: Optional[str]
    instrument: Optional[str]
    instrument_id: Optional[str]
    account: Optional[str]
    account_number: Optional[str]
    average_buy_price: Optional[str]
    pending_average_buy_price: Optional[str]
    quantity: Optional[str]
    intraday_average_buy_price: Optional[str]
    intraday_quantity: Optional[str]
    shares_available_for_exercise: Optional[str]
    shares_held_for_buys: Optional[str]
    shares_held_for_sells: Optional[str]
    shares_held_for_stock_grants: Optional[str]
    shares_held_for_options_collateral: Optional[str]
    shares_held_for_options_events: Optional[str]
    shares_pending_from_options_events: Optional[str]
    shares_available_for_closing_short_position: Optional[str]
    ipo_allocated_quantity: Optional[str]
    ipo_dsp_allocated_quantity: Optional[str]
    avg_cost_affected: Optional[bool]
    avg_cost_affected_reason: Optional[str]
    is_primary_account: Optional[bool]
    updated_at: Optional[str]
    created_at: Optional[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            url=data.get("url"),
            instrument=data.get("instrument"),
            instrument_id=data.get("instrument_id"),
            account=data.get("account"),
            account_number=data.get("account_number"),
            average_buy_price=data.get("average_buy_price"),
            pending_average_buy_price=data.get("pending_average_buy_price"),
            quantity=data.get("quantity"),
            intraday_average_buy_price=data.get("intraday_average_buy_price"),
            intraday_quantity=data.get("intraday_quantity"),
            shares_available_for_exercise=data.get("shares_available_for_exercise"),
            shares_held_for_buys=data.get("shares_held_for_buys"),
            shares_held_for_sells=data.get("shares_held_for_sells"),
            shares_held_for_stock_grants=data.get("shares_held_for_stock_grants"),
            shares_held_for_options_collateral=data.get("shares_held_for_options_collateral"),
            shares_held_for_options_events=data.get("shares_held_for_options_events"),
            shares_pending_from_options_events=data.get("shares_pending_from_options_events"),
            shares_available_for_closing_short_position=data.get("shares_available_for_closing_short_position"),
            ipo_allocated_quantity=data.get("ipo_allocated_quantity"),
            ipo_dsp_allocated_quantity=data.get("ipo_dsp_allocated_quantity"),
            avg_cost_affected=data.get("avg_cost_affected"),
            avg_cost_affected_reason=data.get("avg_cost_affected_reason"),
            is_primary_account=data.get("is_primary_account"),
            updated_at=data.get("updated_at"),
            created_at=data.get("created_at"),
        )


@define
class HeldStocksResponse:
    held_stocks: List[HeldStock] = []


@define
class StockQuoteResponse:
    ask_price: Optional[str]
    ask_size: Optional[int]
    venue_ask_time: Optional[str]
    bid_price: Optional[str]
    bid_size: Optional[int]
    venue_bid_time: Optional[str]
    last_trade_price: Optional[str]
    venue_last_trade_time: Optional[str]
    last_extended_hours_trade_price: Optional[str]
    last_non_reg_trade_price: Optional[str]
    venue_last_non_reg_trade_time: Optional[str]
    previous_close: Optional[str]
    adjusted_previous_close: Optional[str]
    previous_close_date: Optional[str]
    symbol: Optional[str]
    trading_halted: Optional[bool]
    has_traded: Optional[bool]
    last_trade_price_source: Optional[str]
    last_non_reg_trade_price_source: Optional[str]
    updated_at: Optional[str]
    instrument: Optional[str]
    instrument_id: Optional[str]
    state: Optional[str]

    @classmethod
    def from_dict(cls, data):
        return cls(
            ask_price=data["ask_price"],
            ask_size=data["ask_size"],
            venue_ask_time=data["venue_ask_time"],
            bid_price=data["bid_price"],
            bid_size=data["bid_size"],
            venue_bid_time=data["venue_bid_time"],
            last_trade_price=data["last_trade_price"],
            venue_last_trade_time=data["venue_last_trade_time"],
            last_extended_hours_trade_price=data["last_extended_hours_trade_price"],
            last_non_reg_trade_price=data["last_non_reg_trade_price"],
            venue_last_non_reg_trade_time=data["venue_last_non_reg_trade_time"],
            previous_close=data["previous_close"],
            adjusted_previous_close=data["adjusted_previous_close"],
            previous_close_date=data["previous_close_date"],
            symbol=data["symbol"],
            trading_halted=data["trading_halted"],
            has_traded=data["has_traded"],
            last_trade_price_source=data["last_trade_price_source"],
            last_non_reg_trade_price_source=data["last_non_reg_trade_price_source"],
            updated_at=data["updated_at"],
            instrument=data["instrument"],
            instrument_id=data["instrument_id"],
            state=data["state"]
        )


@define
class HeldOption:
    option_id: Optional[str]
    average_price: Optional[str]
    quantity: Optional[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            option_id=data['option_id'],
            average_price=data['average_price'],
            quantity=data['quantity']
        )


@define
class HeldOptionsResponse:
    held_options: List[HeldOption] = []


@define
class OptionInfoResponse:
    chain_symbol: Optional[str] = None
    expiration_date: Optional[str] = None
    strike_price: Optional[str] = None
    issue_date: Optional[str] = None
    type: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            chain_symbol=data['chain_symbol'],
            expiration_date=data['expiration_date'],
            strike_price=data['strike_price'],
            issue_date=data['issue_date'],
            type=data['type'],
        )


@define
class OrderResponse:
    instrument_id: Optional[str]
    symbol: Optional[str]
    quantity: Optional[str]
    price: Optional[str]
    average_price: Optional[str]
    created_at: Optional[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            instrument_id=data['instrument_id'],
            symbol=data['symbol'],
            quantity=data['quantity'],
            price=data['price'],
            average_price=data['average_price'],
            created_at=data['created_at']
        )


@define
class OrdersResponse:
    orders: List[OrderResponse] = []


@define
class OptionOrderExecution:
    price: Optional[str]

    @classmethod
    def from_dict(cls, data):
        return cls(
            price=data["price"]
        )


@define
class OptionOrderLeg:
    strike_price: Optional[str]
    position_effect: Optional[str]
    expiration_date: Optional[str]
    option_type: Optional[str]
    executions: List[OptionOrderExecution] = []

    @classmethod
    def from_dict(cls, data):
        executions = []
        for execution in data.get("executions", []):
            executions.append(OptionOrderExecution.from_dict(execution))

        return cls(
            strike_price=data["strike_price"],
            position_effect=data["position_effect"],
            expiration_date=data["expiration_date"],
            option_type=data["option_type"],
            executions=executions
        )


@define
class OptionOrderResponse:
    chain_symbol: Optional[str]
    created_at: Optional[str]
    quantity: Optional[int]
    canceled_quantity: Optional[int]
    legs: List[OptionOrderLeg] = []

    @classmethod
    def from_dict(cls, data):
        legs = []
        for leg in data.get("legs", []):
            legs.append(OptionOrderLeg.from_dict(leg))

        return cls(
            chain_symbol=data["chain_symbol"],
            created_at=data["created_at"],
            quantity=data["quantity"],
            canceled_quantity=data["canceled_quantity"],
            legs=legs
        )


@define
class OptionOrdersResponse:
    option_orders: List[OptionOrderResponse] = []
