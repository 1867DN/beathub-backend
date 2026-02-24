#!/usr/bin/env python3
"""
seed_data.py - Script para cargar datos iniciales en BeatHub

Este script carga categorías y productos de ejemplo en la base de datos.
Ideal para desarrollo local y testing.

Uso:
    # Local (con dependencias instaladas):
    python seed_data.py
    
    # Docker (recomendado):
    docker exec -i ecommerce_api_dev python seed_data.py

Notas:
    - Elimina datos existentes antes de insertar (para desarrollo)
    - No usar en producción sin modificar
"""

import os
import sys
from typing import Dict, List

# Setup path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    from models.brand import BrandModel
    from models.category import CategoryModel
    from models.product import ProductModel
    from config.database import DATABASE_URI
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("   Asegúrate de estar en el contenedor Docker o tener las dependencias instaladas.")
    sys.exit(1)

# Datos de inicialización
SEED_BRANDS: List[Dict[str, str]] = [
    {"name": "AMT",               "logo_path": "amt.png"},
    {"name": "AMUMU STRAPS",      "logo_path": "amumu_straps.png"},
    {"name": "ANLEON",            "logo_path": "anleon.png"},
    {"name": "ALTO PROFESSIONAL", "logo_path": "alto_professional.png"},
    {"name": "BARE KNUCKLE",      "logo_path": "bare_knuckle.png"},
    {"name": "CHAPMAN GUITARS",   "logo_path": "chapman_guitars.png"},
    {"name": "CLAYTON",           "logo_path": "clayton.png"},
    {"name": "DARKGLASS",         "logo_path": "darkglass.png"},
    {"name": "DEMONFX",           "logo_path": "demonfx.png"},
    {"name": "DSM HUMBOLDT",      "logo_path": "dsm_humboldt.png"},
    {"name": "FLANGER",           "logo_path": "flanger.png"},
    {"name": "FLAMMA",            "logo_path": "flamma.png"},
    {"name": "GRUVGEAR",          "logo_path": "gruvgear.png"},
    {"name": "HEADRUSH",          "logo_path": "headrush.png"},
    {"name": "SPIRA GUITARS",     "logo_path": "spira_guitars.png"},
]

# ── CATEGORÍAS ───────────────────────────────────────────────────────────────
SEED_CATEGORIES: List[Dict[str, str]] = [
    {"name": "Emulador de Amplificador"},
]

# ── PRODUCTOS ─────────────────────────────────────────────────────────────────
# Formato: name, price (transferencia), price_list (lista), discount_percent,
#          stock, category_name, brand_name, description
SEED_PRODUCTS: List[Dict] = [
    # ── AMT ──
    {
        "name": "Pedal Legend Amps Amt F1 Twin Emulates Guitarra MINT",
        "price": 178056.00,
        "price_list": 197840.00,
        "discount_percent": 9,
        "stock": 1,
        "category_name": "Emulador de Amplificador",
        "brand_name": "AMT",
        "description": (
            "AMT F-1 LEGEND AMPS\n"
            "El F-1 fue uno de los primeros diseños de la serie Legend Amps, diseñado para lograr "
            "el clásico sonido de un Fender Twin. Se puede usar para crear un preamp multi canal "
            "desde canales mono de cualquiera de los pedales de la serie Legend Amps (P-1, B-1, M-1, R-1, S-1). "
            "Así la serie se expande constantemente, ofreciendo la oportunidad de lograr un sonido 100% análogo para tu guitarra.\n\n"
            "Este pedal es un preamp con un canal limpio interno y la posibilidad de alternarlo con un canal externo "
            "(cualquier otro pedal de overdrive). Posee un loop de efectos con una entrada estándar de -10dB preparada "
            "para enchufar cualquier efecto auxiliar y boostearlo a 0dB o más, lo cual es más que suficiente para operar "
            "directamente con la potencia del amplificador. En caso de conectar a una mixer o computadora, el preamp tiene "
            "simulador de caja y parlantes."
        ),
    },
]


def seed_database() -> None:
    """
    Carga los datos iniciales en la base de datos.
    
    Limpia datos existentes y carga categorías y productos desde SEED_CATEGORIES
    y SEED_PRODUCTS.
    
    Raises:
        Exception: Si hay error durante la carga
    """
    engine = create_engine(DATABASE_URI)
    SessionLocal = sessionmaker(bind=engine)
    db: Session = SessionLocal()
    
    try:
        # Fase 1: Limpiar datos existentes
        print("🔄 Limpiando datos existentes...")
        db.query(ProductModel).delete()
        db.query(CategoryModel).delete()
        db.query(BrandModel).delete()
        db.commit()
        print("✅ Datos eliminados\n")

        # Fase 2: Insertar marcas
        print("🏷️  Insertando marcas...")
        brands_map: Dict[str, int] = {}

        for brand_data in SEED_BRANDS:
            brand = BrandModel(name=brand_data["name"], logo_path=brand_data.get("logo_path"))
            db.add(brand)
            db.flush()
            brands_map[brand_data["name"]] = brand.id_key
            print(f"  ✓ {brand_data['name']}")

        db.commit()
        print(f"✅ {len(SEED_BRANDS)} marcas insertadas\n")

        # Categorías
        categories_map: Dict[str, int] = {}
        if SEED_CATEGORIES:
            print("📂 Insertando categorías...")
            for cat_data in SEED_CATEGORIES:
                category = CategoryModel(name=cat_data["name"])
                db.add(category)
                db.flush()
                categories_map[cat_data["name"]] = category.id_key
                print(f"  ✓ {cat_data['name']}")
            db.commit()
            print(f"✅ {len(SEED_CATEGORIES)} categorías insertadas\n")

        # Productos
        if SEED_PRODUCTS:
            print("🎵 Insertando productos...")
            successful_products = 0
            for prod_data in SEED_PRODUCTS:
                category_id = categories_map.get(prod_data.get("category_name"))
                brand_id = None
                if prod_data.get("brand_name"):
                    brand_id = next((b.id_key for b in db.query(BrandModel).filter(BrandModel.name == prod_data["brand_name"]).all()), None)
                product = ProductModel(
                    name=prod_data["name"],
                    price=prod_data["price"],
                    price_list=prod_data.get("price_list"),
                    discount_percent=prod_data.get("discount_percent", 0),
                    description=prod_data.get("description"),
                    stock=prod_data["stock"],
                    category_id=category_id,
                    brand_id=brand_id,
                )
                db.add(product)
                successful_products += 1
                print(f"  ✓ {prod_data['name']}")
            db.commit()
            print(f"✅ {successful_products} productos insertados\n")

        print("🎉 ¡Seed completado exitosamente!")
        print(f"   ├─ Marcas: {len(SEED_BRANDS)}")
        print(f"   ├─ Categorías: {len(SEED_CATEGORIES)}")
        print(f"   └─ Productos: {len(SEED_PRODUCTS)}\n")

    except Exception as e:
        db.rollback()
        print(f"❌ Error durante seed: {type(e).__name__}: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 50)
    print("🚀 BeatHub - Seed Data Script")
    print("=" * 50 + "\n")
    
    try:
        seed_database()
        print("✅ Script finalizado correctamente\n")
    except Exception as e:
        print(f"❌ Script falló. Verifica la conexión a DB.\n")
        sys.exit(1)
