"""Brand service."""
from sqlalchemy.orm import Session

from models.brand import BrandModel
from repositories.brand_repository import BrandRepository
from schemas.brand_schema import BrandSchema
from services.base_service_impl import BaseServiceImpl
from services.cache_service import cache_service


class BrandService(BaseServiceImpl):
    """Service for Brand entity with caching (brands change rarely)."""

    def __init__(self, db: Session):
        super().__init__(
            repository_class=BrandRepository,
            model=BrandModel,
            schema=BrandSchema,
            db=db
        )
        self.cache = cache_service
        self.cache_prefix = "brands"
        self.cache_ttl = 3600
