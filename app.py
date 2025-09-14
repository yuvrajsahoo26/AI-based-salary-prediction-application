import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Employee Salary Prediction", layout="centered")
st.title("Employee Salary Prediction App")
st.write("Enter employee details to predict if their salary is above or below $50K per year.")

@st.cache_resource
def load_model():
    return joblib.load("best_model_pipeline.pkl")

pipeline = load_model()

# Mappings as per your label encoding
workclass_mapping = {
    "Federal-gov": 0,
    "Local-gov": 1,
    "Others": 2,
    "Private": 3,
    "Self-emp-inc": 4,
    "Self-emp-not-inc": 5,
    "State-gov": 6
}
marital_mapping = {
    "Divorced": 0,
    "Married-civ-spouse": 1,
    "Married-spouse-absent": 2,
    "Never-married": 3,
    "Separated": 4,
    "Widowed": 5
}
gender_mapping = {
    "Female": 0,
    "Male": 1
    }
occupation_mapping = {
    "Adm-clerical": 0,
    "Craft-repair": 1,
    "Exec-managerial": 2,
    "Farming-fishing": 3,
    "Handlers-cleaners": 4,
    "Machine-op-inspct": 5,
    "Other-service": 6,
    "Priv-house-serv": 7,
    "Prof-specialty": 8,
    "Protective-serv": 9,
    "Sales": 10,
    "Tech-support": 11,
    "Transport-moving": 12,
    "Unknown": 13
}
relationship_mapping = {
    "Husband": 0,
    "Not-in-family": 1,
    "Other-relative": 2,
    "Own-child": 3,
    "Unmarried": 4,
    "Wife": 5
}
race_mapping = {
    "Amer-Indian-Eskimo": 0,
    "Asian-Pac-Islander": 1,
    "Black": 2,
    "Other": 3,
    "White": 4
}
country_mapping = {
    "Cambodia": 0, "Canada": 1, "China": 2, "Columbia": 3, "Cuba": 4, "Dominican-Republic": 5,
    "Ecuador": 6, "El-Salvador": 7, "England": 8, "France": 9, "Germany": 10, "Greece": 11,
    "Guatemala": 12, "Haiti": 13, "Holand-Netherlands": 14, "Honduras": 15, "Hong": 16,
    "Hungary": 17, "India": 18, "Iran": 19, "Ireland": 20, "Italy": 21, "Jamaica": 22,
    "Japan": 23, "Laos": 24, "Mexico": 25, "Nicaragua": 26, "Other": 27,
    "Outlying-US(Guam-USVI-etc)": 28, "Peru": 29, "Philippines": 30, "Poland": 31,
    "Portugal": 32, "Puerto-Rico": 33, "Scotland": 34, "South": 35, "Taiwan": 36,
    "Thailand": 37, "Trinadad&Tobago": 38, "United-States": 39, "Vietnam": 40, "Yugoslavia": 41
}

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 18, 75, 30)
        gender = st.selectbox("Gender", list(gender_mapping.keys()))
        race = st.selectbox("Race", list(race_mapping.keys()))
        native_country = st.selectbox("Native Country", list(country_mapping.keys()), index=39)
        educational_num = st.slider("Education Level (5-16)", 5, 16, 10)
    with col2:
        workclass = st.selectbox("Work Class", list(workclass_mapping.keys()))
        hours_per_week = st.slider("Hours per Week", 1, 99, 40)
        occupation = st.selectbox("Occupation", list(occupation_mapping.keys()))
        marital_status = st.selectbox("Marital Status", list(marital_mapping.keys()))
        relationship = st.selectbox("Relationship", list(relationship_mapping.keys()))
        capital_gain = st.slider("Capital Gain ($)", 0, 20000, 0, step=1000)
        capital_loss = st.slider("Capital Loss ($)", 0, 5000, 0, step=100)

    submitted = st.form_submit_button("Predict Salary")

if submitted:
    input_df = pd.DataFrame({
        'age': [age],
        'workclass': [workclass_mapping[workclass]],
        'marital-status': [marital_mapping[marital_status]],
        'occupation': [occupation_mapping[occupation]],
        'relationship': [relationship_mapping[relationship]],
        'race': [race_mapping[race]],
        'gender': [gender_mapping[gender]],
        'native-country': [country_mapping[native_country]],
        'educational-num': [educational_num],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'hours-per-week': [hours_per_week]
    })
    prediction = pipeline.predict(input_df.values)
    if prediction[0] == 1:
        st.success("Prediction: Income > $50K per year")
    else:
        st.info("Prediction: Income ≤ $50K per year")

st.markdown("---")
st.caption("Created by Yuvraj Sahoo")
