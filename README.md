# Financial Transaction Fraud Detection using ML and DNN + XAI

## Introduction
Artificial Intelligence (AI) has entered the business mainstream, opening new opportunities to solve the most complex business problems. During the Covid-19 pandemic, the use of online payments skyrocketed, accelerating the shift toward digital transactions using cards and mobile apps instead of cash.

As per Statista research, Visa is the market leader among digital payment processors globally, with more than $10 trillion in transactions. In UK e-commerce, Visa and Mastercard are the most frequently used payment options, available with 98% of the top 500 online retailers in 2020.

---

## Impact of AI in Finance & Banking
The finance and banking industry has benefited from digital technologies like AI, creating the new discipline of FinTech. AI is projected to save the banking industry approximately $1 trillion by 2030 and $447 billion by 2023.

AI applications in FinTech include fraud detection, risk management, investment management, predictive analytics, and anti-money laundering.


---

## Financial Transaction Fraud Detection
While digitization creates opportunities for development and growth, it also attracts cybercriminals, making financial fraud a major business problem.

Fraud losses increased by 30%, with £754 million stolen from bank transactions in the UK in 2021. Additionally, 76% of credit card fraud losses in the UK resulted from Card-not-Present (CNP) fraud, totaling £470.2 million.

---

## Research Problem
### Can we 'trust AI' just because it is very accurate?
Several ML methods have been applied to detect fraudulent behavior in financial data. However, most fraud detection systems rely on black-box models, making it difficult for non-AI experts or decision-makers to understand and trust their predictions.

Explainable AI (XAI) addresses this challenge by providing transparency and trustworthiness through human-readable explanations of AI models.

---

## Research Aim and Objectives
This research aims to implement an **Explainable AI (XAI)-driven Interface and a Proof of Concept (POC) Web Application** for financial transaction fraud detection.

### Objectives:
1. Build a robust classification engine using five ML algorithms and two DNN algorithms.
2. Evaluate model performance using metrics like Accuracy, AUC-ROC, Precision, and Recall.
3. Implement five XAI methods to improve trust and model explainability for the best-performing model.
4. Develop a POC web application for real-time fraud detection.

---

## Explainable AI (XAI)
Explainable AI (XAI) makes black-box AI models intuitive and understandable for business users without sacrificing performance or accuracy.

> "While Intelligence is the primary deliverable of AI, Explainability is the fundamental need of an AI product."


---

## Research Methodology
The design process is inspired by the CRISP-DM framework to achieve the stated objectives. XAI is incorporated to ensure the system's transparency and usability.


---
## Results
- Tree-based model **Light GBM with Hypertuning**  outperformed ensemble and linear models.
- Best-performing model: **Light GBM** achieved 98.27% accuracy and an AUC-ROC score of 0.96.

![Model Performance](https://user-images.githubusercontent.com/31254745/191382637-26c54d01-a548-46a9-868b-051dff5ab4a7.png)

---

## Conclusion
This project implemented an XAI-driven fraud detection system, making predictions transparent and trustworthy. The approach improves decision-making confidence and reduces fraud in financial services and banking.

---

## How to Set Up Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Rohit-110/Fradulent_Transaction_Detection/
2. Navigate to the directory:
  ```bash
  cd Fraudulent_Transaction_Detection
   ```
3. Install dependencies:
   ```bash
   git clone https://github.com/Rohit-110/Fradulent_Transaction_Detection/
   ```
4. Run the application:
  ```bash
  streamlit run app.py
  ```

