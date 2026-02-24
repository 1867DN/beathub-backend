"""Brand schema with validation."""
from typing import Optional
from pydantic import Field

from schemas.base_schema import BaseSchema


class BrandSchema(BaseSchema):
    """Schema for Brand entity."""

    name: str = Field(..., min_length=1, max_length=100, description="Brand name (required, unique)")
    logo_path: Optional[str] = Field(None, description="Relative path to brand logo image")
