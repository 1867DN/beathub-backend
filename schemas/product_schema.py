"""Product schema for request/response validation."""
from typing import Optional, List, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema
from schemas.category_schema import CategoryBasicSchema

if TYPE_CHECKING:
    from schemas.review_schema import ReviewSchema


class ProductSchema(BaseSchema):
    """Schema for Product entity with validations."""

    name: str = Field(..., min_length=1, max_length=200, description="Product name (required)")
    price: float = Field(..., gt=0, description="Precio transferencia/cash")
    price_list: Optional[float] = Field(None, description="Precio de lista")
    discount_percent: Optional[int] = Field(0, ge=0, le=100, description="Porcentaje de descuento")
    description: Optional[str] = Field(None, description="Descripción del producto")
    image_path: Optional[str] = Field(None, description="Ruta de imagen del producto")
    stock: int = Field(default=0, ge=0, description="Stock disponible")
    is_active: Optional[str] = Field('true', description="Visible en la tienda")
    is_new: Optional[str] = Field('false', description="Destacado como Lo nuevo")
    is_featured: Optional[str] = Field('false', description="En cartelera del home")

    category_id: int = Field(..., description="Category ID reference (required)")
    brand_id: Optional[int] = Field(None, description="Brand ID reference (optional)")

    category: Optional[CategoryBasicSchema] = None
    reviews: Optional[List['ReviewSchema']] = []
