from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class BrandModel(BaseModel):
    __tablename__ = 'brands'

    name = Column(String, unique=True, index=True, nullable=False)
    logo_path = Column(String, nullable=True)  # ruta relativa a la imagen, ej: "assets/brands/amt.png"
    products = relationship('ProductModel', back_populates='brand', lazy="select")
