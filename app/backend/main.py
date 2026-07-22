from fastapi import FastAPI
from app.backend.models import Customer
from app.database.crud import insert_customer
from app.database.crud import insert_customer, get_all_customers
from app.database.crud import (
    insert_customer,
    get_all_customers,
    update_customer
)
from app.database.crud import (
    insert_customer,
    get_all_customers,
    update_customer,
    delete_customer
)
from app.backend.services import predict_customer
app = FastAPI(
    title="Customer Churn Intelligence API",
    version="1.0.0"
)
from app.database.crud import save_prediction
@app.get("/")
def home():
    return {"message": "Customer Churn Intelligence API is Running 🚀"}

@app.post("/customers")
def add_customer(customer: Customer):

    customer_id = insert_customer(customer)

    return {
        "message": "Customer saved successfully!",
        "customer_id": customer_id
    }
@app.get("/customers")
def view_customers():

    customers = get_all_customers()

    return {
        "total_customers": len(customers),
        "customers": customers
    }
@app.put("/customers/{customer_id}")
def edit_customer(customer_id: int, customer: Customer):

    update_customer(customer_id, customer)

    return {
        "message": "Customer updated successfully!"
    }
@app.delete("/customers/{customer_id}")
def remove_customer(customer_id: int):

    delete_customer(customer_id)

    return {
        "message": "Customer deleted successfully!"
    }
@app.post("/predict")
def predict(customer: Customer):

    customer_id = insert_customer(customer)

    prediction, probability, risk = predict_customer(customer)

    save_prediction(
        customer_id,
        prediction,
        probability,
        risk
    )

    return {
        "customer_id": customer_id,
        "prediction": prediction,
        "probability": round(probability, 4),
        "risk_level": risk
    }
    