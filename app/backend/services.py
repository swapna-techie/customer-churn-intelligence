import joblib

model = joblib.load("models/random_forest_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

print("Model Loaded Successfully!")
import pandas as pd

def predict_customer(customer):
    data = pd.DataFrame([{
        "Gender": customer.gender,
        "Senior Citizen": customer.senior_citizen,
        "Partner": customer.partner,
        "Dependents": customer.dependents,
        "Tenure Months": customer.tenure_months,
        "Phone Service": customer.phone_service,
        "Multiple Lines": customer.multiple_lines,
        "Internet Service": customer.internet_service,
        "Online Security": customer.online_security,
        "Online Backup": customer.online_backup,
        "Device Protection": customer.device_protection,
        "Tech Support": customer.tech_support,
        "Streaming TV": customer.streaming_tv,
        "Streaming Movies": customer.streaming_movies,
        "Contract": customer.contract,
        "Paperless Billing": customer.paperless_billing,
        "Payment Method": customer.payment_method,
        "Monthly Charges": customer.monthly_charges,
        "Total Charges": customer.total_charges
    }])
    print("DataFrame:")
    print(data)

    print("\nColumns:")
    print(data.columns.tolist())

    print("\nData Types:")
    print(data.dtypes)
    processed = preprocessor.transform(data)

    prediction = int(model.predict(processed)[0])
    probability = float(model.predict_proba(processed)[0][1])

    prediction_label = "Yes" if prediction == 1 else "No"

    risk = "High" if probability >= 0.5 else "Low"

    return prediction_label, probability, risk