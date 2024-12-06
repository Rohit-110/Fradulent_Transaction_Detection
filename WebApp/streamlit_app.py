import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the saved model
loaded_model = pickle.load(open('./final_model.sav', 'rb'))

# Function for Prediction
@st.cache_data(persist=True)
def predict_fraud(card1, card2, card4, card6, addr1, addr2, TransactionAmt, P_emaildomain, ProductCD, DeviceType):
    input_data = np.array([[card1, card2, card4, card6, addr1, addr2, TransactionAmt, P_emaildomain, ProductCD, DeviceType]])
    prediction = loaded_model.predict_proba(input_data)
    pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

# Main function
def main():
    # Apply custom CSS for styling
    st.markdown("""
        <style>
            body {
                background: linear-gradient(120deg, #1e3c72, #2a5298);
                color: white;
                font-family: 'Arial', sans-serif;
            }
            .stApp {
                background: linear-gradient(120deg, #1e3c72, #2a5298);
                color: white;
                font-family: 'Arial', sans-serif;
            }
            .block-container {
                padding: 2rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
            }
            h1, h2, h3, h4, h5, h6 {
                color: white !important;
            }
            p, label, .stMarkdown {
                color: #f0f0f0 !important;
            }
            .stButton button {
                background-color: #6a11cb;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #2575fc;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
        
        <div class="header">
            <h1>Fraudulent Transaction Detection</h1>
            <img src="https://financialcrimeacademy.org/wp-content/uploads/2022/05/2-43-1024x576.jpg" height="300" width="450" alt="App Logo">
            <p>AI-powered predictions for safer financial transactions</p>
        </div>
    """, unsafe_allow_html=True)

    # Input Form Section
    TransactionAmt = st.number_input("Transaction Amount (USD)", 0, 20000, step=1, key="TransactionAmt")

    card1 = st.number_input("Payment Card 1 (USD)", 0, 20000, step=1, key="card1")
    card2 = st.number_input("Payment Card 2 (USD)", 0, 20000, step=1, key="card2")
    card4 = st.radio("Card Category", [1, 2, 3, 4], key="card4")
    st.info("1: Discover | 2: Mastercard | 3: American Express | 4: Visa")

    card6 = st.radio("Card Type", [1, 2], key="card6")
    st.info("1: Credit | 2: Debit")

    addr1 = st.slider("Billing Zip Code", 0, 500, step=1, key="addr1")
    addr2 = st.slider("Billing Country Code", 0, 100, step=1, key="addr2")

    P_emaildomain = st.selectbox("Purchaser Email Domain", [0, 1, 2, 3, 4], key="P_emaildomain")
    st.info("0: Gmail | 1: Outlook | 2: Mail.com | 3: Others | 4: Yahoo")

    ProductCD = st.selectbox("Product Code", [0, 1, 2, 3, 4], key="ProductCD")
    st.info("0: C | 1: H | 2: R | 3: S | 4: W")

    DeviceType = st.radio("Device Type", [1, 2], key="DeviceType")
    st.info("1: Mobile | 2: Desktop")
    st.markdown('</div>', unsafe_allow_html=True)

   # Safe and Danger Visuals
    safe_html = """
        <div class="result-container">
            <img src="https://i.pinimg.com/originals/e8/06/52/e80652af2c77e3a73858e16b2ffe5f9a.gif" alt="Safe Transaction">
        </div>
    """
    danger_html = """
        <div class="result-container">
            <img src="https://i.pinimg.com/originals/16/82/8c/16828cec9b85bbb355070bd6e8a49597.gif" alt="Fraudulent Transaction">
        </div>
    """

    # Submit Button
    if st.button("Predict Transaction Status", key="predict_button"):
        output = predict_fraud(card1, card2, card4, card6, addr1, addr2, TransactionAmt, P_emaildomain, ProductCD, DeviceType)
        final_output = output * (100)
        st.subheader(f"Prediction Score: {final_output:.2f}%")

        if final_output > 75.0:
            st.markdown(danger_html, unsafe_allow_html=True)
            st.error("Alert! This transaction is likely fraudulent.")
        else:
            st.markdown(safe_html, unsafe_allow_html=True)
            st.success("Good news! This transaction appears legitimate.")

if __name__ == '__main__':
    main()
