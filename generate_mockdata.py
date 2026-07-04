import json
import os

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# 1. User History (Data Aggregation Pipeline Source)
# This simulates items pulled from Myntra, Amazon, and Flipkart with different interaction statuses
user_history = [
    {"item_id": 1, "title": "Oversized Black Graphic Hoodie", "source": "Myntra", "status": "bought"},
    {"item_id": 2, "title": "Beige Double-Breasted Formal Blazer", "source": "Amazon", "status": "wishlist"},
    {"item_id": 3, "title": "Floral Print Summer Maxi Dress", "source": "Flipkart", "status": "cart"},
    {"item_id": 4, "title": "Baggy Denim Cargo Pants", "source": "Myntra", "status": "bought"},
    {"item_id": 5, "title": "Black Leather Combat Boots", "source": "Flipkart", "status": "cart"},
    {"item_id": 6, "title": "Loose Fit Skate Sneakers", "source": "Myntra", "status": "bought"},
    {"item_id": 7, "title": "Pinstripe Office Trousers Slim Fit", "source": "Amazon", "status": "wishlist"}
]

# 2. Master Product Catalog
# This simulates the entire catalog available across the web that our model will recommend *from*
product_catalog = [
    {"product_id": 101, "title": "Oversized Vintage Sweatshirt", "brand": "Urban Wear", "price": 1999},
    {"product_id": 102, "title": "Classic Linen White Button-Down Shirt", "brand": "Office Chic", "price": 1499},
    {"product_id": 103, "title": "Bohemian Pastel Ruffle Sundress", "brand": "Wildflower", "price": 2499},
    {"product_id": 104, "title": "Faux Leather Studded Moto Jacket", "brand": "Rebel Style", "price": 3999},
    {"product_id": 105, "title": "Relaxed Fit Cargo Joggers", "brand": "Street Vibe", "price": 1799},
    {"product_id": 106, "title": "Formal Pleated Khaki Trousers", "brand": "Corporate Edge", "price": 2199},
    {"product_id": 107, "title": "Ditsy Floral Wrap Midi Dress", "brand": "Cottage Core", "price": 1899},
    {"product_id": 108, "title": "Chunky Platform Ankle Boots", "brand": "Grunge Lab", "price": 3200}
]

# Save User History to data/user_history.json
with open("data/user_history.json", "w") as f:
    json.dump(user_history, f, indent=4)

# Save Product Catalog to data/product_catalog.json
with open("data/product_catalog.json", "w") as f:
    json.dump(product_catalog, f, indent=4)

print("🎉 Datasets successfully generated inside the 'data/' folder!")