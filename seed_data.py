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
    {"name": "Guitarra Eléctrica"},
    {"name": "Pedal de Efectos"},
    {"name": "Bajo Eléctrico"},
    {"name": "Accesorios"},
    {"name": "Amplificador"},
]

# ── PRODUCTOS ─────────────────────────────────────────────────────────────────
SEED_PRODUCTS: List[Dict] = [
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
            "el clásico sonido de un Fender Twin."
        ),
    },
    {
        "name": "Guitarra Eléctrica Chapman ML1 Modern Slate Blue",
        "price": 850000.00,
        "price_list": 950000.00,
        "discount_percent": 10,
        "stock": 3,
        "category_name": "Guitarra Eléctrica",
        "brand_name": "CHAPMAN GUITARS",
        "description": (
            "Chapman ML1 Modern en color Slate Blue Satin.\n"
            "Cuerpo de caoba, mástil de arce, escala de 25.5 pulgadas. "
            "Perfecta para rock y metal moderno."
        ),
    },
    {
        "name": "Pedal Darkglass Alpha Omega Ultra V2",
        "price": 620000.00,
        "price_list": 680000.00,
        "discount_percent": 8,
        "stock": 2,
        "category_name": "Pedal de Efectos",
        "brand_name": "DARKGLASS",
        "description": (
            "Preamplificador y distorsión para bajo de alta gama.\n"
            "Combina los circuitos Alpha y Omega en una sola unidad con EQ de 4 bandas, "
            "cab sim y salida directa balanceada."
        ),
    },
    {
        "name": "Pedal Flamma FC300 Multi-Effects Processor",
        "price": 195000.00,
        "price_list": 220000.00,
        "discount_percent": 11,
        "stock": 5,
        "category_name": "Pedal de Efectos",
        "brand_name": "FLAMMA",
        "description": (
            "Procesador de efectos múltiples compacto.\n"
            "Incluye más de 90 efectos, looper de 60 segundos, "
            "expresión y conexión USB. Ideal para práctica y escenario."
        ),
    },
    {
        "name": "Correa Gruvgear FretWraps HD Pack x3",
        "price": 42000.00,
        "price_list": 48000.00,
        "discount_percent": 12,
        "stock": 10,
        "category_name": "Accesorios",
        "brand_name": "GRUVGEAR",
        "description": (
            "Pack de 3 FretWraps HD para silenciar cuerdas.\n"
            "Disponibles en distintos tamaños para guitarra, bajo y ukelele. "
            "Herramienta esencial para grabación en estudio."
        ),
    },
    {
        "name": "Púas Clayton Acetal Standard 0.38mm x12",
        "price": 8500.00,
        "price_list": 9500.00,
        "discount_percent": 10,
        "stock": 50,
        "category_name": "Accesorios",
        "brand_name": "CLAYTON",
        "description": (
            "Pack de 12 púas de acetal estándar calibre 0.38mm (extra light).\n"
            "Material de alta calidad que produce un sonido brillante y preciso."
        ),
    },
    {
        "name": "Headrush MX5 Multi-FX & Amp Modeler",
        "price": 1200000.00,
        "price_list": 1350000.00,
        "discount_percent": 11,
        "stock": 2,
        "category_name": "Emulador de Amplificador",
        "brand_name": "HEADRUSH",
        "description": (
            "Potente modelador de amplificadores y procesador de efectos.\n"
            "Pantalla táctil de 7 pulgadas, 33 modelos de amp, 42 efectos de calidad de estudio "
            "y looper de 20 minutos."
        ),
    },
    {
        "name": "Correa Amumu Straps Leather Vintage Brown 8cm",
        "price": 35000.00,
        "price_list": 39000.00,
        "discount_percent": 10,
        "stock": 8,
        "category_name": "Accesorios",
        "brand_name": "AMUMU STRAPS",
        "description": (
            "Correa de cuero genuino marrón vintage de 8cm de ancho.\n"
            "Ajustable de 95cm a 155cm. Extremos de cuero reforzado compatibles con cualquier guitarra o bajo."
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
