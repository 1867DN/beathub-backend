"""Brand controller with proper dependency injection."""
from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.base_controller_impl import BaseControllerImpl
from schemas.brand_schema import BrandSchema
from schemas.product_schema import ProductSchema
from services.brand_service import BrandService
from services.product_service import ProductService
from config.database import get_db


class BrandController(BaseControllerImpl):
    """Controller for Brand entity with CRUD operations."""

    def __init__(self):
        super().__init__(
            schema=BrandSchema,
            service_factory=lambda db: BrandService(db),
            tags=["Brands"]
        )
        self._register_brand_routes()

    def _register_brand_routes(self):
        """Register extra brand-specific routes."""

        @self.router.get("/{id_key}/products", response_model=List[ProductSchema], status_code=status.HTTP_200_OK)
        async def get_products_by_brand(
            id_key: int,
            skip: int = 0,
            limit: int = 100,
            db: Session = Depends(get_db)
        ):
            """Get all products that belong to a specific brand."""
            product_service = ProductService(db)
            return product_service.get_by_brand(id_key, skip=skip, limit=limit)
