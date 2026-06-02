import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

# ------------------------
# UI STYLE
# ------------------------
st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

h1 {
    text-align: center;
    color: #1F4E79;
    font-weight: 700;
}

.stButton > button {
    background-color: #1F4E79;
    color: white;
    border-radius: 6px;
    border: none;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# LOAD MODEL
# ------------------------
model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# ------------------------
# TITLE
# ------------------------
st.title("Customer Churn Prediction System")
st.write("Machine Learning Based Customer Churn Prediction Dashboard")

# ------------------------
# MODEL METRICS
# ------------------------
st.sidebar.header("Model Performance")

st.sidebar.metric(
    "Recall (Churn Class)",
    "79%"
)

st.sidebar.metric(
    "Precision (Churn Class)",
    "49%"
)

st.sidebar.metric(
    "AUC Score",
    "0.84"
)

# ------------------------
# INPUTS
# ------------------------
col1, col2, col3 = st.columns(3)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

with col2:

    tenure = st.slider(
        "Tenure",
        0,
        72
    )

    phone = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    monthly = st.number_input(
    "Monthly Charges",
    min_value=18.0,
    max_value=120.0,
    value=70.0
)
    

with col3:

    total = tenure * monthly

    st.metric(
        "Estimated Total Charges",
        f"${total:.2f}"
    )

    multiple = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

# ------------------------
# BUILD INPUT
# ------------------------
input_data = pd.DataFrame(
    columns=model_columns
)

input_data.loc[0] = 0

input_data["gender"] = 1 if gender == "Male" else 0
input_data["SeniorCitizen"] = senior
input_data["Partner"] = 1 if partner == "Yes" else 0
input_data["Dependents"] = 1 if dependents == "Yes" else 0
input_data["tenure"] = tenure
input_data["PhoneService"] = 1 if phone == "Yes" else 0
input_data["PaperlessBilling"] = 1 if paperless == "Yes" else 0
input_data["MonthlyCharges"] = monthly
input_data["TotalCharges"] = total

if multiple == "Yes":
    input_data["MultipleLines_Yes"] = 1

elif multiple == "No phone service":
    input_data["MultipleLines_No phone service"] = 1

if internet == "Fiber optic":
    input_data["InternetService_Fiber optic"] = 1

elif internet == "No":
    input_data["InternetService_No"] = 1

if online_security == "Yes":
    input_data["OnlineSecurity_Yes"] = 1

elif online_security == "No internet service":
    input_data["OnlineSecurity_No internet service"] = 1

if tech_support == "Yes":
    input_data["TechSupport_Yes"] = 1

elif tech_support == "No internet service":
    input_data["TechSupport_No internet service"] = 1

if contract == "One year":
    input_data["Contract_One year"] = 1

elif contract == "Two year":
    input_data["Contract_Two year"] = 1

if payment == "Electronic check":
    input_data["PaymentMethod_Electronic check"] = 1

elif payment == "Mailed check":
    input_data["PaymentMethod_Mailed check"] = 1

elif payment == "Credit card (automatic)":
    input_data[
        "PaymentMethod_Credit card (automatic)"
    ] = 1

# ------------------------
# BUTTON
# ------------------------
if st.button("Predict Churn"):
    probability = model.predict_proba(
        input_data
    )[0][1]

    # get class prediction (0 = stay, 1 = churn)
    prediction = int(model.predict(input_data)[0])

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error(
            "Customer Likely to CHURN"
        )

    else:

        st.success(
            "Customer Likely to STAY"
        )

    # ------------------------
    # CHURN PROBABILITY
    # ------------------------

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))
    if probability < 0.40:
        st.success("Low Risk Customer")

    elif probability < 0.70:
        st.warning("Medium Risk Customer")

    else:
        st.error("High Risk Customer")
    # ------------------------
    # BUSINESS RECOMMENDATION
    # ------------------------

    st.subheader("Business Recommendations")

    # Dynamic retention budget
    estimated_cost = monthly * probability * 0.25

    # Customer value
    customer_value = total

    col_a, col_b = st.columns(2)

    with col_a:
        st.metric(
            "Estimated Retention Budget",
            f"${estimated_cost:.2f}"
        )

    with col_b:
        st.metric(
            "Customer Value",
            f"${customer_value:.2f}"
        )

    recommendations = []

    if probability > 0.70:
        recommendations.append(
            "Personal Retention Call"
        )

    if contract == "Month-to-month":
        recommendations.append(
            "Promote Long-Term Contract"
        )

    if tech_support == "No":
        recommendations.append(
            "Offer Tech Support Package"
        )

    if online_security == "No":
        recommendations.append(
            "Offer Security Add-on"
        )

    if paperless == "Yes":
        recommendations.append(
            "Send Loyalty Campaign"
        )

    if payment == "Electronic check":
        recommendations.append(
            "Promote Automatic Payment Method"
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Maintain Current Relationship"
        )

    recommendation_df = pd.DataFrame({
        "Recommended Action": recommendations
    })

    st.dataframe(
        recommendation_df,
       use_container_width=True
    )
    st.subheader("Model Evaluation")

    st.image(
        "confusion_matrix.png",
        caption="Confusion Matrix"
    )

    st.image(
        "roc_curve.png",
        caption="ROC Curve"
    )
        # ------------------------
    # DOWNLOAD RESULTS
    # ------------------------
    stay_probability = 1 - probability

    prediction_text = (
        "Churn"
        if prediction == 1
        else "Stay"
    )

    result_df = pd.DataFrame({

        "Gender": [gender],
        "Senior Citizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],

        "Tenure": [tenure],
        "Phone Service": [phone],
        "Paperless Billing": [paperless],

        "Monthly Charges": [monthly],
        "Total Charges": [total],

        "Multiple Lines": [multiple],
        "Internet Service": [internet],

        "Online Security": [online_security],
        "Tech Support": [tech_support],

        "Contract": [contract],
        "Payment Method": [payment],

        "Prediction": [prediction_text],

        "Churn Probability (%)": [
            round(probability * 100, 2)
        ],

        "Stay Probability (%)": [
            round(stay_probability * 100, 2)
        ],

        "Customer Value": [
            round(customer_value, 2)
        ],

        "Estimated Retention Budget": [
            round(estimated_cost, 2)
        ],

        "Recommendations": [
            ", ".join(recommendations)
        ]

    })

    csv = result_df.to_csv(index=False)

    st.download_button(
        label="Download Prediction Report",
        data=csv,
        file_name="customer_churn_report.csv",
        mime="text/csv"
    )
