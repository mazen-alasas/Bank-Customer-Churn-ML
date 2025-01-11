import streamlit as st
import pandas as pd
import pickle
from utils import *


with open('./best_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Bank Churn Prediction App")
st.markdown("""
### Predict Customer Churn:
Upload customer data to predict whether a customer is likely to churn.
""")

uploaded_file = st.file_uploader("Upload your CSV file", type = ["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.write("### Uploaded Data Preview:")
    st.dataframe(data.head(10))

    droped_columns = ['id', 'CustomerId', 'Surname']
    saved_columns = data[droped_columns].copy()

    data = drop_columns(data, columns = droped_columns)

    data = encode_categorical_columns(data)

    data['Balance'] = scale_columns(data, columns = ['Balance'])

    predictions = model.predict(data)

    data = pd.concat([saved_columns, data], axis = 1)

    data['Exited'] = predictions
    st.write("### Prediction Results:")
    st.dataframe(data)

    st.markdown("### Download Predictions:")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "predictions.csv", "text/csv")

st.sidebar.header("Manual Input")
st.sidebar.markdown("Provide customer details to predict churn:")

geography           = st.sidebar.selectbox("Geography", ['France', 'Spain', 'Germany'])
gender              = st.sidebar.radio("Customer Gender", ['Male', 'Female'])
age                 = st.sidebar.slider("Customer Age", min_value = 18, max_value = 90, step = 1)
credit_score        = st.sidebar.number_input("Credit Score", min_value=300, max_value=1000, step=1)
tenure              = st.sidebar.number_input("Tenure (Years)", min_value=0, max_value=10, step=1)
balance             = st.sidebar.number_input("Balance", min_value=0.0, max_value=250000.0, step=0.01)
num_of_products     = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])
has_card            = st.sidebar.radio("Has Credit Card?", ['Yes', 'No'])
is_active           = st.sidebar.radio("Is Active Member?", ['Yes', 'No'])
estimated_salary    = st.sidebar.number_input("Estimated Salary", min_value=0.0, max_value=200000.0, step=0.01)

if st.sidebar.button("Predict"):
    input_data = pd.DataFrame([[
        credit_score,
        geography,
        gender,
        age,
        tenure,
        balance,
        num_of_products,
        has_card,
        is_active,
        estimated_salary
    ]], columns = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'])

    input_data['Balance'] = balance / 250000.0

    input_data = encode_categorical_columns(input_data)

    result = model.predict(input_data)

    st.markdown(f"## Prediction: {'Churn' if result[0] == 1 else 'No Churn'}")