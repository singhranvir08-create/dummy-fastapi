from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# Models
# -----------------------
class Ticket(BaseModel):
    ticket_id: str
    issue: str

class Order(BaseModel):
    order_id: str

class Product(BaseModel):
    product_id: str

class SearchQuery(BaseModel):
    query: str

# -----------------------
# 1. Health
# -----------------------
@app.get("/api/v1/health")
def health():
    return {"status": "ok"}

# -----------------------
# 2. Ticket Escalate
# -----------------------
@app.post("/api/v1/tickets/escalate")
def escalate_ticket(data: Ticket):
    return {"message": f"Ticket {data.ticket_id} escalated"}

# -----------------------
# 3. Logistics Track
# -----------------------
@app.post("/api/v1/logistics/track")
def track_order(data: Order):
    return {
        "order_id": data.order_id,
        "location": "Mumbai Hub",
        "status": "In Transit"
    }

# -----------------------
# 4. Cancel Order
# -----------------------
@app.post("/api/v1/orders/cancel")
def cancel_order(data: Order):
    return {"message": f"Order {data.order_id} cancelled"}

# -----------------------
# 5. Product Media Dispatch
# -----------------------
@app.post("/api/v1/products/media/dispatch")
def media_dispatch(data: Product):
    return {"message": f"Media sent for product {data.product_id}"}

# -----------------------
# 6. Refund Status
# -----------------------
@app.post("/api/v1/refunds/status")
def refund_status(data: Order):
    return {"order_id": data.order_id, "refund": "processing"}

# -----------------------
# 7. Return Eligibility
# -----------------------
@app.get("/api/v1/orders/{order_id}/returns/eligibility-check")
def return_check(order_id: str):
    return {"order_id": order_id, "eligible": True}

# -----------------------
# 8. RMA Create
# -----------------------
@app.post("/api/v1/rma/create")
def create_rma(data: Order):
    return {"rma_id": "RMA123", "order_id": data.order_id}

# -----------------------
# 9. Order Items Search
# -----------------------
@app.post("/api/v1/orders/items/search")
def search_items(data: SearchQuery):
    return {"items": ["item1", "item2"], "query": data.query}

# -----------------------
# 10. Orders Search
# -----------------------
@app.post("/api/v1/orders/search")
def search_orders(data: SearchQuery):
    return {
        "orders": [
            {"order_id": "ORD123", "status": "shipped"},
            {"order_id": "ORD124", "status": "processing"}
        ]
    }

# -----------------------
# 11. Find Order ID
# -----------------------
@app.post("/api/v1/orders/find-id")
def find_order(data: SearchQuery):
    return {"order_id": "ORD123", "query": data.query}

# -----------------------
# 12. Product Stock
# -----------------------
@app.post("/api/v1/products/stock")
def stock(data: Product):
    return {"product_id": data.product_id, "stock": 25}

# -----------------------
# 13. Ticket Notes
# -----------------------
@app.post("/api/v1/tickets/notes")
def ticket_notes(data: Ticket):
    return {"ticket_id": data.ticket_id, "notes": ["Note 1", "Note 2"]}