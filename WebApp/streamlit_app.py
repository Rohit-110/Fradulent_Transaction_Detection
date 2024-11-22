import numpy as np
import pickle
import time
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
    # Add custom CSS for styling
    st.markdown("""
        <style>
            @keyframes gradientBackground {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            body {
                background: linear-gradient(270deg, #FF7EB3, #65C7F7, #0052D4);
                background-size: 400% 400%;
                animation: gradientBackground 15s ease infinite;
                color: #333;
                font-family: 'Arial', sans-serif;
            }
            .container {
                max-width: 700px;
                margin: 0 auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }
            .header {
                text-align: center;
                margin-bottom: 30px;
            }
            .header img {
                width: 100%; /* Make image take up 100% of the parent width */
                max-width: 800px; /* Optional: Set a maximum width */
                height: auto; /* Automatically adjust height to maintain aspect ratio */
                margin-bottom: 10px;
                animation: pulse 2s infinite;
            }
            .header h1 {
                color: white; /* White color */
                font-size: 40px; /* Enlarged font size */
                font-weight: bold; /* Bold font */
                text-align: center;
            }
            .header p {
                color: #444;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
        <div class="header">
            <img src="https://financialcrimeacademy.org/wp-content/uploads/2022/05/2-43-1024x576.jpg" alt="App Logo">
            <h1>Fraudulent Transaction Detection</h1>
            <p>AI-powered predictions for safer financial transactions</p>
        </div>
    """, unsafe_allow_html=True)

    # Centered Input Form
    # st.markdown('<div class="container">', unsafe_allow_html=True)
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
            <img src="https://i.pinimg.com/originals/e8/06/52/e80652af2c77e3a73858e16b2ffe5f9a.gif" alt="Safe Transaction" style="width: 60%; max-width: 400px; border-radius: 10px;">
        </div>
    """
    danger_html = """
        <div class="result-container">
            <img src="https://i.pinimg.com/originals/16/82/8c/16828cec9b85bbb355070bd6e8a49597.gif" alt="Fraudulent Transaction" style="width: 60%; max-width: 400px; border-radius: 10px;">
        </div>
    """

    # Submit Button
    if st.button("Predict Transaction Status", key="predict_button", use_container_width=True):
        output = predict_fraud(card1, card2, card4, card6, addr1, addr2, TransactionAmt, P_emaildomain, ProductCD, DeviceType)
        final_output = output * 80
        st.subheader(f"Prediction Score: {final_output:.2f}%")

        if final_output > 75.0:
            st.markdown(danger_html, unsafe_allow_html=True)
            st.error("Alert! This transaction is likely fraudulent.")
        else:
            st.markdown(safe_html, unsafe_allow_html=True)
            st.success("Good news! This transaction appears legitimate.")

if __name__ == '__main__':
    main()
