import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef4ff 100%);
    }
    .card {
        background: white;
        padding: 1.2rem;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    .title-text {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
    }
    .subtitle-text {
        color: #475569;
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title-text">Customer Churn Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Assess customer retention risk with a polished, real-time prediction experience.</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧾 Customer Information Form")
    st.caption("Complete the profile details below and submit the form to get a churn prediction.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", ["Female", "Male"])
            senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
            partner = st.selectbox("Partner", ["Yes", "No"])
            dependents = st.selectbox("Dependents", ["Yes", "No"])
            tenure_months = st.number_input("Tenure Months", min_value=0, max_value=240, value=12, step=1)
            phone_service = st.selectbox("Phone Service", ["Yes", "No"])
            multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
            internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
            online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

        with col2:
            device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
            tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
            streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
            streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
            payment_method = st.selectbox(
                "Payment Method",
                [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)",
                ],
            )
            monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.35, step=0.01)
            total_charges = st.number_input("Total Charges", min_value=0.0, value=300.0, step=0.01)

        submitted = st.form_submit_button("Predict Churn Risk", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        payload = {
            "gender": gender,
            "senior_citizen": senior_citizen,
            "partner": partner,
            "dependents": dependents,
            "tenure_months": int(tenure_months),
            "phone_service": phone_service,
            "multiple_lines": multiple_lines,
            "internet_service": internet_service,
            "online_security": online_security,
            "online_backup": online_backup,
            "device_protection": device_protection,
            "tech_support": tech_support,
            "streaming_tv": streaming_tv,
            "streaming_movies": streaming_movies,
            "contract": contract,
            "paperless_billing": paperless_billing,
            "payment_method": payment_method,
            "monthly_charges": float(monthly_charges),
            "total_charges": float(total_charges),
        }

        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=20)
            response.raise_for_status()
            result = response.json()

            st.success("Prediction completed successfully.")
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 🔎 Prediction Results")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Churn Prediction", result.get("prediction", "Unknown"))
            with col_b:
                st.metric("Probability", f"{result.get('probability', 0):.4f}")
            with col_c:
                st.metric("Risk Level", result.get("risk_level", "Unknown"))
            st.markdown('</div>', unsafe_allow_html=True)

        except requests.exceptions.ConnectionError:
            st.error("The backend server is not reachable. Please start the FastAPI app first.")
        except requests.exceptions.HTTPError as exc:
            st.error(f"Prediction request failed: {exc}")
        except Exception as exc:
            st.error(f"An unexpected error occurred: {exc}")
