"""Product controller with search support."""
from typing import List
from fastapi import Depends, status
from sqlalchemy.orm import Session

from controllers.base_controller_impl import BaseControllerImpl
from schemas.product_schema import ProductSchema
from services.product_service import ProductService
from config.database import get_db
from models.product import ProductModel


class ProductController(BaseControllerImpl):
    """Controller for Product entity with search and filter."""

    def __init__(self):
        super().__init__(
            schema=ProductSchema,
            service_factory=lambda db: ProductService(db),
            tags=["Products"]
        )
        self._register_product_routes()

    def _register_product_routes(self):
        """Register product-specific routes."""

        @self.router.get("/search/", response_model=List[ProductSchema], status_code=status.HTTP_200_OK)
        async def search_products(
            q: str = "",
            skip: int = 0,
            limit: int = 100,
            db: Session = Depends(get_db)
        ):
            """Search products by name (case-insensitive). Only active products."""
            query = db.query(ProductModel).filter(
                ProductModel.is_active != 'false'
            )
            if q:
                query = query.filter(ProductModel.name.ilike(f"%{q}%"))
            return query.offset(skip).limit(limit).all()

        @self.router.get("/admin-all/", response_model=List[ProductSchema], status_code=status.HTTP_200_OK)
        async def get_all_products_admin(
            skip: int = 0,
            limit: int = 200,
            db: Session = Depends(get_db)
        ):
            """Get ALL products including inactive ones (for admin panel)."""
            service = self.service_factory(db)
            return service.get_all(skip=skip, limit=limit, include_inactive=True)
