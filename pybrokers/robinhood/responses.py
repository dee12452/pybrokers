from typing import Optional, List, Dict, Any

from attrs import define


@define
class LoginResponse:
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
        return HeldStock(
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
