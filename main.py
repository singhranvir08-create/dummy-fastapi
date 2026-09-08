from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ----------------------
# Models
# ----------------------
class OrderSearch(BaseModel):
	query: str


class TrackingRequest(BaseModel):
	order_id: str


# ----------------------
# Routes
# ----------------------
@app.get("/")
def root():
	return {"message": "Dummy API Running 🚀"}


@app.get("/health")
def health():
	return {"status": "ok"}


@app.post("/orders/search")
def search_orders(data: OrderSearch):
	return {
		"orders": [
			{"order_id": "ORD123", "status": "shipped"},
			{"order_id": "ORD124", "status": "processing"},
		]
	}


@app.post("/tracking")
def track_order(data: TrackingRequest):
	return {
		"order_id": data.order_id,
		"location": "Mumbai Hub",
		"status": "In Transit",
	}


@app.post("/refunds/status")
def refund_status():
	return {
		"order_id": "ORD123",
		"refund": "processing",
	}


@app.post("/returns/eligibility")
def return_check():
	return {
		"order_id": "ORD123",
		"eligible": True,
	}
