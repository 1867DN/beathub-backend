"""OrderDetail schema with validation."""
from typing import Optional
from pydantic import Field

from schemas.base_schema import BaseSchema


class OrderDetailSchema(BaseSchema):
    """Schema for OrderDetail entity with validations."""

    quantity: int = Field(
        ...,
        gt=0,
        description="Quantity (required, must be positive)"
    )

    price: Optional[float] = Field(
        None,
        gt=0,
        description="Price (auto-filled from product if not provided)"
    )

    order_id: int = Field(
        ...,
        description="Order ID reference (required)"
    )

    product_id: int = Field(
        ...,
        description="Product ID reference (required)"
    )
