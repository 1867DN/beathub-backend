"""
SqlAlchemy model for products.

This module defines the ProductModel class which represents a product in the database.
"""

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, CheckConstraint
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ProductModel(BaseModel):
    """
    Class representing a product in the database.

    This class represents a product. It inherits from BaseModel and adds additional fields
    specific to products: name, price, stock, and category_id. It also defines relationships with
    CategoryModel, ReviewModel, and OrderDetailModel.

    Database constraints:
        - stock must be >= 0 (enforced at DB level)
        - price must be > 0 (enforced by Pydantic validation)
    """

    __tablename__ = 'products'

    # Table-level constraints
    __table_args__ = (
        CheckConstraint('stock >= 0', name='check_product_stock_non_negative'),
    )

    name = Column(String, index=True)
    price = Column(Float, index=True)           # Precio transferencia/cash
    price_list = Column(Float, nullable=True)   # Precio de lista
    discount_percent = Column(Integer, nullable=True, default=0)  # % descuento (ej: 9)
    description = Column(Text, nullable=True)   # Descripción larga del producto
    image_path = Column(String, nullable=True)  # Imagen del producto
    stock = Column(Integer, default=0, nullable=False, index=True)
    is_active = Column(String, nullable=False, default='true')  # Visible en la tienda
    is_new = Column(String, nullable=False, default='false')    # Destacado como "Lo nuevo"
    is_featured = Column(String, nullable=False, default='false')  # En cartelera home
    category_id = Column(Integer, ForeignKey('categories.id_key'), index=True)
    brand_id = Column(Integer, ForeignKey('brands.id_key'), nullable=True, index=True)

    category = relationship(
        'CategoryModel',
        back_populates='products',
        lazy='select',
    )
    brand = relationship(
        'BrandModel',
        back_populates='products',
        lazy='select',
    )
    reviews = relationship(
        'ReviewModel',
        back_populates='product',
        cascade='all, delete-orphan',
        lazy='select',
    )
    order_details = relationship(
        'OrderDetailModel',
        back_populates='product',
        cascade='all, delete-orphan',
        lazy='select',
    )
