from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
import difflib
from datetime import datetime

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

class OrderItem(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    image_url: Optional[str] = None
    selected_color: Optional[str] = None

class Order(BaseModel):
    name: str
    address: str
    city: str
    houseNumber: str
    governorate: str
    items: List[OrderItem]
    total: float
    promo_code: Optional[str] = None
    timestamp: Optional[str] = None

class OrderItemRequest(BaseModel):
    product_id: int
    quantity: int
    selected_color: Optional[str] = None

class OrderRequest(BaseModel):
    name: str
    address: str
    city: str
    houseNumber: str
    governorate: str
    items: List[OrderItemRequest]
    total: float
    promo_code: Optional[str] = None

# --- Mock Data ---

products_db = []

def load_products():
    global products_db
    try:
        with open("products.json", "r") as f:
            data = json.load(f)
            products_db = [Product(**item) for item in data]
    except FileNotFoundError:
        print("products.json not found. Starting with empty product list.")
        products_db = []
    except json.JSONDecodeError:
        print("Error decoding products.json.")
        products_db = []

load_products()

@app.get("/search", response_model=dict)
async def search_products(q: str, page: int = 1, limit: int = 10):
    """
    Search for products by name or description with pagination.
    """
    query = q.lower()
    all_results = [
        p for p in products_db
        if query in p.name.lower() or (p.description and query in p.description.lower())
    ]
    
    # Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated_results = all_results[start:end]
    
    return {
        "items": paginated_results,
        "total": len(all_results),
        "page": page,
        "limit": limit,
        "pages": (len(all_results) + limit - 1) // limit
    }

@app.get("/search/suggestions")
async def search_suggestions(q: str):
    """
    Optimized search returning only names/ids with fuzzy matching.
    """
    if len(q) < 4:
        return []
        
    query = q.lower()
    
    # 1. Exact/Prefix matches
    matches = [p for p in products_db if query in p.name.lower()]
    
    # 2. Fuzzy matches using Levenshtein distance (via difflib)
    # Only if we don't have many exact matches
    if len(matches) < 5:
        all_names = [p.name for p in products_db]
        # cutoff=0.4 allows for some typos
        close_matches = difflib.get_close_matches(query, all_names, n=5, cutoff=0.4)
        
        existing_ids = {p.id for p in matches}
        for name in close_matches:
            product = next((p for p in products_db if p.name == name), None)
            if product and product.id not in existing_ids:
                matches.append(product)
    
    # Return lightweight response
    return [{"id": p.id, "name": p.name} for p in matches]

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

@app.post("/api/orders", tags=["Orders"])
def create_order(order_req: OrderRequest):
    # Reconstruct full order items from DB
    full_items = []
    calculated_subtotal = 0.0
    
    for item_req in order_req.items:
        product = next((p for p in products_db if p.id == item_req.product_id), None)
        if product:
            # Calculate item price (handle discounts if any logic existed)
            # Frontend logic: if quantity >= 2, price = price * 0.9
            
            item_price = product.price
            if item_req.quantity >= 2:
                item_price = item_price * 0.9
                
            item_total = item_price * item_req.quantity
            calculated_subtotal += item_total
            
            full_items.append(OrderItem(
                product_id=product.id,
                name=product.name,
                price=product.price, 
                quantity=item_req.quantity,
                image_url=product.image_url,
                selected_color=item_req.selected_color
            ))
        else:
            raise HTTPException(status_code=400, detail=f"Product with ID {item_req.product_id} not found")

    # Calculate tax (6%)
    tax = calculated_subtotal * 0.06
    final_total = calculated_subtotal + tax
    
    # Create full Order object
    order = Order(
        name=order_req.name,
        address=order_req.address,
        city=order_req.city,
        houseNumber=order_req.houseNumber,
        governorate=order_req.governorate,
        items=full_items,
        total=final_total,
        promo_code=order_req.promo_code,
        timestamp=datetime.now().isoformat()
    )
    
    orders_file = "orders.json"
    orders_data = []
    
    if os.path.exists(orders_file):
        try:
            with open(orders_file, "r") as f:
                orders_data = json.load(f)
        except json.JSONDecodeError:
            pass
            
    orders_data.append(order.dict())
    
    with open(orders_file, "w") as f:
        json.dump(orders_data, f, indent=2)
        
    return {"message": "Order placed successfully", "order": order}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
