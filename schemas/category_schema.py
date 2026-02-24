"""Category schema with validation."""
from typing import Optional, List, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.product_schema import ProductSchema


class CategoryBasicSchema(BaseSchema):
    """Slim category schema — used inside ProductSchema to avoid circular recursion."""
    name: str = Field(..., min_length=1, max_length=100)


class CategorySchema(BaseSchema):
    """Schema for Category entity with validations."""

    name: str = Field(..., min_length=1, max_length=100, description="Category name (required, unique)")
    products: Optional[List['ProductSchema']] = []
