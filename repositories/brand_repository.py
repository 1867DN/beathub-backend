"""Brand repository for database operations."""
from sqlalchemy.orm import Session

from models.brand import BrandModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.brand_schema import BrandSchema


class BrandRepository(BaseRepositoryImpl):
    """Repository for Brand entity database operations."""

    def __init__(self, db: Session):
        super().__init__(BrandModel, BrandSchema, db)
