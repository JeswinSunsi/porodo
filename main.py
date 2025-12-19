from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="TechNova API", description="API for TechNova E-commerce Store")

# CORS middleware for Vue frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---

class Product(BaseModel):
    id: int
    name: str
    price: float
    original_price: Optional[float] = None
    description: Optional[str] = None
    short_description: Optional[str] = None
    image_url: str
    category: Optional[str] = None
    specs: Optional[dict] = None
    colors: Optional[List[str]] = None
    badges: Optional[List[str]] = None

class CartItem(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    image_url: str
    selected_color: Optional[str] = None

class Review(BaseModel):
    author: str
    role: Optional[str] = None
    rating: int
    comment: str

class Promotion(BaseModel):
    title: str
    description: str
    code: Optional[str] = None
    discount_percentage: Optional[int] = None

# --- Mock Data ---

products_db = [
    Product(
        id=1,
        name="Sony WH-1000XM5",
        price=348.00,
        original_price=399.00,
        short_description="Noise Cancelling / 30h Bat",
        description="Experience the next level of silence. The WH-1000XM5 headphones feature our best noise canceling yet, with two processors controlling 8 microphones for unprecedented noise reduction and exceptional call quality.",
        image_url="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?q=80&w=600&auto=format&fit=crop",
        category="Audio",
        specs={
            "Battery Life": "30 Hours (NC On)",
            "Weight": "250g",
            "Bluetooth": "Version 5.2",
            "Charging": "USB-C (3min = 3hr)",
            "Driver Unit": "30mm",
            "Noise Canceling": "Active (Auto NC)"
        },
        colors=["Black", "Gray", "Blue"],
        badges=["Sale"]
    ),
    Product(
        id=2,
        name="MacBook Air M2",
        price=1099.00,
        short_description="Midnight / 256GB SSD",
        image_url="https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?q=80&w=600&auto=format&fit=crop",
        category="Laptops"
    ),
    Product(
        id=3,
        name="Apple Watch Ultra",
        price=799.00,
        short_description="Titanium Case / 49mm",
        image_url="https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=600&auto=format&fit=crop",
        category="Wearables",
        badges=["Hot"]
    ),
    Product(
        id=4,
        name="JBL Flip 6",
        price=99.00,
        short_description="Waterproof / Black",
        image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600&auto=format&fit=crop",
        category="Audio"
    ),
    Product(
        id=5,
        name="iPhone 15 Pro Max",
        price=1199.00,
        short_description="Titanium / 256GB",
        image_url="https://images.unsplash.com/photo-1696446701796-da61225697cc?q=80&w=600&auto=format&fit=crop",
        category="Smartphones"
    ),
    Product(
        id=6,
        name="iPad Air 5",
        price=559.00,
        short_description="M1 Chip / Space Gray",
        image_url="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?q=80&w=600&auto=format&fit=crop",
        category="Tablets",
        badges=["Refurb"]
    ),
    Product(
        id=7,
        name="MX Master 3S",
        price=99.00,
        short_description="Ergonomic / Silent",
        image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?q=80&w=600&auto=format&fit=crop",
        category="Accessories"
    ),
    Product(
        id=8,
        name="GoPro Hero 12",
        price=399.00,
        short_description="5.3K Video / Waterproof",
        image_url="https://images.unsplash.com/photo-1564466021189-e99b53a5b3f6?q=80&w=600&auto=format&fit=crop",
        category="Cameras"
    ),
    Product(
        id=9,
        name="Universal Headphone Stand",
        price=49.00,
        short_description="Aluminum Silver",
        image_url="https://images.unsplash.com/photo-1623998021646-4c31cc9b4743?q=80&w=200&auto=format&fit=crop",
        category="Accessories"
    )
]

cart_db = [
    CartItem(
        product_id=1,
        name="Sony WH-1000XM5",
        price=348.00,
        quantity=1,
        image_url="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?q=80&w=200&auto=format&fit=crop",
        selected_color="Midnight Black"
    ),
    CartItem(
        product_id=9,
        name="Universal Headphone Stand",
        price=49.00,
        quantity=1,
        image_url="https://images.unsplash.com/photo-1623998021646-4c31cc9b4743?q=80&w=200&auto=format&fit=crop",
        selected_color="Aluminum Silver"
    )
]

reviews_db = [
    Review(
        author="Alex Chen",
        role="Developer",
        rating=5,
        comment="The delivery was insanely fast. Ordered the S24 Ultra yesterday, and it arrived this morning. Packaging was secure and pristine."
    ),
    Review(
        author="Sarah Jenkins",
        role="Designer",
        rating=5,
        comment="Love the clean design of the site and how easy it is to find specs. Prices are competitive with Amazon, but the support is real humans."
    ),
    Review(
        author="Michael Ross",
        role="Gamer",
        rating=5,
        comment="The VR headset I bought had a small issue, and they replaced it within 24 hours. Best customer service I've experienced in years."
    )
]

promotions_db = [
    Promotion(
        title="Flash Sale",
        description="Get 20% OFF all smartphones.",
        code="TECH20",
        discount_percentage=20
    ),
    Promotion(
        title="VR Gear Sale",
        description="30% Off VR Gear",
        discount_percentage=30
    ),
    Promotion(
        title="Newsletter",
        description="10% OFF your first order",
        discount_percentage=10
    )
]

# --- Endpoints ---

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Welcome to TechNova API"}

@app.get("/products", response_model=List[Product], tags=["Products"])
def get_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int):
    product = next((p for p in products_db if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/cart", response_model=List[CartItem], tags=["Cart"])
def get_cart():
    return cart_db

@app.get("/reviews", response_model=List[Review], tags=["Social Proof"])
def get_reviews():
    return reviews_db

@app.get("/promotions", response_model=List[Promotion], tags=["Marketing"])
def get_promotions():
    return promotions_db

@app.get("/home/products", response_model=List[Product], tags=["Home"])
def get_home_products():
    """Returns the products displayed in the 'Trending Now' section of the home page."""
    # IDs 1-8 correspond to the products in the index.html grid
    trending_ids = [1, 2, 3, 4, 5, 6, 7, 8]
    return [p for p in products_db if p.id in trending_ids]

@app.get("/home/trending-products-2", response_model=List[Product], tags=["Home"])
def get_home_trending_products_2():
    """Returns the products displayed in the second 'Trending Now' section of the home page."""
    # Just picking some products for the second section
    trending_ids = [2, 4, 6, 8, 1, 3] 
    return [p for p in products_db if p.id in trending_ids]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
