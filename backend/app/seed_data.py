# app/load_starter_data.py
import requests

BASE_URL = "http://127.0.0.1:8000"

ITEMS = [
    {
        "brand": "Nike", "name": "Oversized Tech Fleece Hoodie",
        "category": "hoodie", "fit_type": "oversized",
        "style_tags": "streetwear,casual", "price": 110.00,
        "image_url": "hoodie_nike_black.png",
        "sizes": [
            {"size": "S", "chest": 40, "length": 26, "shoulder": 19, "sleeve": 25},
            {"size": "M", "chest": 43, "length": 27, "shoulder": 20, "sleeve": 26},
            {"size": "L", "chest": 46, "length": 28, "shoulder": 21, "sleeve": 27},
        ],
    },
    {
        "brand": "Levi's", "name": "Baggy Black Jeans",
        "category": "jeans", "fit_type": "oversized",
        "style_tags": "streetwear,casual", "price": 89.99,
        "image_url": "jeans_levis_black.png",
        "sizes": [
            {"size": "30", "waist": 30, "length": 32},
            {"size": "32", "waist": 32, "length": 32},
            {"size": "34", "waist": 34, "length": 32},
        ],
    },
    {
        "brand": "Nike", "name": "Air Force 1",
        "category": "sneakers", "fit_type": "regular",
        "style_tags": "streetwear,casual,minimal", "price": 120.00,
        "image_url": "shoes_af1_white.png",
        "sizes": [
            {"size": "9"}, {"size": "10"}, {"size": "11"},
        ],
    },
    {
        "brand": "Uniqlo", "name": "Regular Fit Crew Tee",
        "category": "tee", "fit_type": "regular",
        "style_tags": "minimal,casual", "price": 14.99,
        "image_url": "tee_uniqlo_white.png",
        "sizes": [
            {"size": "S", "chest": 36, "length": 27, "shoulder": 17, "sleeve": 8},
            {"size": "M", "chest": 39, "length": 28, "shoulder": 18, "sleeve": 8.5},
            {"size": "L", "chest": 42, "length": 29, "shoulder": 19, "sleeve": 9},
        ],
    },
    {
        "brand": "Carhartt", "name": "Relaxed Fit Cargo Pants",
        "category": "jeans", "fit_type": "regular",
        "style_tags": "streetwear,techwear", "price": 69.99,
        "image_url": "cargo_carhartt_olive.png",
        "sizes": [
            {"size": "30", "waist": 30, "length": 32},
            {"size": "32", "waist": 32, "length": 32},
            {"size": "34", "waist": 34, "length": 32},
        ],
    },
    {
        "brand": "Adidas", "name": "Slim Fit Track Jacket",
        "category": "jacket", "fit_type": "slim",
        "style_tags": "techwear,athleisure", "price": 75.00,
        "image_url": "jacket_adidas_black.png",
        "sizes": [
            {"size": "S", "chest": 38, "length": 25, "shoulder": 17, "sleeve": 24},
            {"size": "M", "chest": 41, "length": 26, "shoulder": 18, "sleeve": 25},
            {"size": "L", "chest": 44, "length": 27, "shoulder": 19, "sleeve": 26},
        ],
    },
    {
        "brand": "New Balance", "name": "550 Sneakers",
        "category": "sneakers", "fit_type": "regular",
        "style_tags": "casual,minimal", "price": 130.00,
        "image_url": "shoes_nb550_green.png",
        "sizes": [
            {"size": "9"}, {"size": "10"}, {"size": "11"},
        ],
    },
    {
        "brand": "Zara", "name": "Oversized Denim Jacket",
        "category": "jacket", "fit_type": "oversized",
        "style_tags": "streetwear,casual", "price": 89.90,
        "image_url": "jacket_zara_denim.png",
        "sizes": [
            {"size": "S", "chest": 42, "length": 26, "shoulder": 20, "sleeve": 25},
            {"size": "M", "chest": 45, "length": 27, "shoulder": 21, "sleeve": 26},
            {"size": "L", "chest": 48, "length": 28, "shoulder": 22, "sleeve": 27},
        ],
    },
    {
        "brand": "H&M", "name": "Slim Fit Chinos",
        "category": "jeans", "fit_type": "slim",
        "style_tags": "preppy,formal,minimal", "price": 39.99,
        "image_url": "chinos_hm_khaki.png",
        "sizes": [
            {"size": "30", "waist": 30, "length": 32},
            {"size": "32", "waist": 32, "length": 32},
            {"size": "34", "waist": 34, "length": 32},
        ],
    },
    {
        "brand": "Champion", "name": "Regular Fit Hoodie",
        "category": "hoodie", "fit_type": "regular",
        "style_tags": "casual,athleisure", "price": 55.00,
        "image_url": "hoodie_champion_grey.png",
        "sizes": [
            {"size": "S", "chest": 38, "length": 26, "shoulder": 18, "sleeve": 24},
            {"size": "M", "chest": 41, "length": 27, "shoulder": 19, "sleeve": 25},
            {"size": "L", "chest": 44, "length": 28, "shoulder": 20, "sleeve": 26},
        ],
    },
]

def load():
    for item in ITEMS:
        r = requests.post(f"{BASE_URL}/clothing/", json=item)
        if r.status_code == 200:
            print(f"Added: {item['brand']} {item['name']}")
        else:
            print(f"FAILED: {item['brand']} {item['name']} -> {r.status_code} {r.text}")

if __name__ == "__main__":
    load()