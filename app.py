import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("gradient_boosting_churn.pkl")

model = load_model()

st.set_page_config(page_title="Churn Prediction App", page_icon="📡", layout="centered")
st.title("📡 Customer Churn Prediction")
st.write("Masukkan informasi pelanggan untuk memprediksi kemungkinan churn.")

# Mapping Contract (Ordinal Encoding)
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}

# Form input user
with st.form("churn_form"):
    col1, col2 = st.columns(2)

    with col1:
        contract = st.selectbox("Contract", list(contract_map.keys()))
        tenure = st.number_input("Tenure (bulan)", min_value=0, max_value=120, value=12)
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=70.0)

    with col2:
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        payment_method = st.selectbox(
            "Payment Method",
            ["Electronic check", "Credit card (automatic)", "Bank transfer (automatic)", "Mailed check"]
        )
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    # Submit Botton
    submitted = st.form_submit_button("Predict Churn")

if submitted:
    # Convert ke format sesuai preprocessing model
    input_data = pd.DataFrame({
        "Contract": [contract_map[contract]],
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "OnlineSecurity": [1 if online_security == "Yes" else 0],
        "PaymentMethod_Electronic check": [1 if payment_method == "Electronic check" else 0],
        "PaymentMethod_Credit card (automatic)": [1 if payment_method == "Credit card (automatic)" else 0],
        "PaymentMethod_Bank transfer (automatic)": [1 if payment_method == "Bank transfer (automatic)" else 0],
        "PaymentMethod_Mailed check": [1 if payment_method == "Mailed check" else 0],
        "InternetService_DSL": [1 if internet_service == "DSL" else 0],
        "InternetService_Fiber optic": [1 if internet_service == "Fiber optic" else 0],
        "InternetService_No": [1 if internet_service == "No" else 0]
    })

    # Prediksi
    prediction = model.predict(input_data)[0]
    # Mengambil probabilitas kelas 1 (Churn)
    proba_churn = model.predict_proba(input_data)[0][1]
    # Mengambil probabilitas kelas 0 (Tidak Churn)
    proba_not_churn = model.predict_proba(input_data)[0][0]


    st.subheader("Hasil Prediksi")
    if prediction == 1:
        st.error(f"Pelanggan kemungkinan **CHURN** dengan probabilitas {proba_churn:.2%}")
    else:
        st.success(f"Pelanggan kemungkinan **TIDAK CHURN** dengan probabilitas {proba_not_churn:.2%}")