import streamlit as st
import pickle
import numpy as np

def load_model():
    """Load the model and encoders from the pickle file."""
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load the model and encoders
data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Employee Salary Prediction")

    st.write("""### Information to predict your salary""")

    # Define options for countries and education levels
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education_levels = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    # User inputs
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Experience", 0, 50, 3)

    # Calculate salary button
    if st.button("Calculate Salary"):
        # Transform categorical inputs to numerical values
        country_encoded = le_country.transform([country])[0]
        education_encoded = le_education.transform([education])[0]

        # Prepare input array for prediction
        X = np.array([[country_encoded, education_encoded, experience]])

        # Predict salary
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")

# Run the Streamlit app
if __name__ == "__main__":
    show_predict_page()
