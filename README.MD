You can explore the live application here: 
https://customerchurnprediction2601.streamlit.app/

Customer Churn Prediction System
Complete Interview Preparation Notes
1. Project Title

Customer Churn Prediction System using Machine Learning

2. Project Objective

The objective of this project is to predict whether a customer is likely to leave a company (churn) or continue using its services.

The system analyzes customer information such as:

Tenure
Monthly charges
Contract type
Payment method
Online security
Tech support
Demographic information

and predicts the probability of customer churn using a Machine Learning model.

The project also provides business recommendations to help retain customers who are at risk of leaving.

3. Problem Statement

Customer acquisition is expensive.

Studies show that retaining an existing customer is significantly cheaper than acquiring a new one.

Telecom companies lose millions of dollars every year due to customer churn.

Without an intelligent prediction system:

Companies react after customers leave
Retention campaigns become ineffective
Revenue decreases
Customer lifetime value drops

This project solves that problem by identifying potential churners before they leave.

4. Why This Project Is Important

Businesses need answers to questions like:

Which customers are likely to leave?
How risky is each customer?
What actions should be taken to retain them?
How much retention budget should be allocated?

Machine Learning helps answer these questions automatically.

5. Real World Use Cases
Telecom

Predict customers who may switch to another network.

Banking

Predict customers who may close their accounts.

Insurance

Predict policy cancellation.

SaaS Companies

Predict subscription cancellations.

OTT Platforms

Predict users who may stop subscriptions.

Examples:

Netflix
Spotify
Amazon Prime
Airtel
Jio
6. Dataset Used

Telco Customer Churn Dataset

Features include:

Customer Information
Gender
Senior Citizen
Partner
Dependents
Service Information
Phone Service
Multiple Lines
Internet Service
Online Security
Tech Support
Billing Information
Monthly Charges
Total Charges
Contract Type
Payment Method
Target Variable
Churn

0 = Stay
1 = Churn
7. Project Workflow
Data Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Streamlit Deployment
8. Data Preprocessing
Missing Value Handling

Checked and cleaned missing values.

Encoding

Categorical variables converted into numerical format.

Examples:

Male → 1
Female → 0
One-Hot Encoding

Used for:

Contract Type
Internet Service
Payment Method
9. Feature Engineering

Created:

Total Charges = Monthly Charges × Tenure

This helps the model understand customer value.

10. Why Feature Engineering Is Important

Raw data often doesn't reveal business meaning.

Example:

Monthly Charge = $80
Tenure = 2 months

This customer has only paid:

$160

Compared to:

Monthly Charge = $80
Tenure = 60 months

Total value:

$4800

The second customer is much more valuable.

11. Machine Learning Algorithm Used
Logistic Regression

Reason:

Easy to interpret
Fast training
Works well for binary classification
Produces probabilities

Output:

0.85 = 85% churn probability
12. Why Logistic Regression?

Because churn prediction is a binary classification problem.

Only two outcomes exist:

Stay
or
Churn

Logistic Regression is one of the strongest baseline models for such problems.

13. Train-Test Split

Dataset divided into:

80% Training Data

20% Testing Data

Training data teaches the model.

Testing data evaluates model performance on unseen customers.

14. Class Imbalance Problem

In churn datasets:

Stay customers > Churn customers

This creates imbalance.

Example:

7000 customers

5000 Stay
2000 Churn

Without handling imbalance, the model may simply predict:

Everyone will Stay

and still appear accurate.

15. Solution for Imbalance

Used:

class_weight = "balanced"

inside Logistic Regression.

This gives higher importance to churn customers during training.

16. Model Evaluation Metrics
Accuracy

Overall correctness.

Precision

Among predicted churners:

How many actually churned?
Recall

Among actual churners:

How many did we successfully identify?
AUC Score

Measures the model's ability to separate churners and non-churners.

17. Why Recall Matters More Than Accuracy

In churn prediction:

Missing a churn customer is expensive.

Example:

Actual Churner

Model predicts:

Stay

Company loses that customer.

Therefore:

Recall is more important than accuracy.

18. Confusion Matrix

Shows:

True Positive
False Positive
True Negative
False Negative
Interpretation

True Positive

Correctly predicted churn

True Negative

Correctly predicted stay

False Positive

Predicted churn but customer stayed

False Negative

Predicted stay but customer churned
19. ROC Curve

ROC means:

Receiver Operating Characteristic

It compares:

True Positive Rate
vs
False Positive Rate
20. AUC Score Interpretation
0.50 → Random Guess
0.60 → Poor
0.70 → Fair
0.80 → Good
0.90 → Excellent
1.00 → Perfect

Your model:

AUC = 0.84

Meaning:

The model has good discriminative power.

21. What Happens During Prediction?

User enters customer details.

The application:

Step 1

Converts inputs into model format.

Step 2

Generates churn probability.

Example:

0.82
Step 3

Converts probability into prediction.

Customer Likely to Churn
22. Why Show Probability Instead of Only Prediction?

Prediction:

Churn

does not show confidence.

Probability:

82%

gives more business value.

Managers can prioritize high-risk customers.

23. Business Recommendation Engine

The system automatically recommends actions.

Examples:

Month-to-Month Contract

Recommendation:

Promote Long-Term Contract
No Tech Support

Recommendation:

Offer Tech Support Package
No Security

Recommendation:

Offer Security Add-on
24. Retention Budget Logic

Formula:

Retention Budget
=
Monthly Charges × Churn Probability × 0.25

Purpose:

Estimate how much effort or incentive should be spent to retain a customer.

25. Why Streamlit?

Advantages:

Fast deployment
Python-based
No frontend knowledge required
Interactive dashboards
Easy cloud hosting
26. Deployment Architecture
GitHub Repository
        ↓
Streamlit Cloud
        ↓
Public URL
27. Challenges Faced
Class Imbalance

Solved using:

class_weight = balanced
Feature Encoding

Handled using One-Hot Encoding.

Deployment Issues

Managed dependencies using:

requirements.txt
Streamlit Integration

Connected trained model with UI.

28. Future Improvements
SHAP Explainability

Explain why each prediction was made.

Customer Segmentation

Group customers by risk level.

Automated Email Alerts

Notify retention teams.

Real-Time Data Pipeline

Predict churn continuously.

Advanced Models
XGBoost
Random Forest
LightGBM
29. Interview Question
Why did you choose Logistic Regression instead of Random Forest?

Answer:

Logistic Regression provides interpretable results, trains quickly, produces probability scores, and serves as a strong baseline model for binary classification problems.

30. Interview Question
Why is churn prediction important?

Answer:

Customer retention is cheaper than customer acquisition. Predicting churn helps companies proactively retain customers and reduce revenue loss.

31. Interview Question
Why is Recall important?

Answer:

A false negative means a churn customer is missed. Missing churners can directly impact revenue, so Recall is prioritized.

32. Interview Question
What is the most important feature?

Answer:

Based on business understanding, contract type, tenure, monthly charges, online security, and tech support are among the strongest indicators of churn.

33. One-Line Project Summary

Developed and deployed a Machine Learning-based Customer Churn Prediction System using Logistic Regression and Streamlit to identify high-risk customers, estimate churn probability, and provide business retention recommendations.


"Which features contribute the most to churn and which features help retain customers?"

Since nee Logistic Regression use pannirukka, business perspective-la answer pannalaam.

Features That Increase Churn Probability

These are generally considered high-risk indicators:
| Feature                  | Why it Increases Churn                                                       |
| ------------------------ | ---------------------------------------------------------------------------- |
| Month-to-Month Contract  | Customer has no long-term commitment                                         |
| Short Tenure             | New customers are more likely to leave                                       |
| High Monthly Charges     | Customers may feel service is expensive                                      |
| Electronic Check Payment | Historically associated with higher churn                                    |
| No Online Security       | Customer is using fewer value-added services                                 |
| No Tech Support          | Customer may face unresolved issues                                          |
| Fiber Optic (sometimes)  | Higher expectations and higher bills can increase dissatisfaction            |
| Paperless Billing        | Often linked with online/self-service users who switch providers more easily |





Example High-Risk Customer
Tenure = 2 months
Contract = Month-to-Month
Monthly Charges = $95
Tech Support = No
Online Security = No

Model will usually assign:

High Churn Probability 
because multiple risk factors are present.

Features That Increase Customer Retention (Stay)

| Feature                   | Why it Helps Retention                     |
| ------------------------- | ------------------------------------------ |
| Two-Year Contract         | Strong commitment                          |
| One-Year Contract         | Moderate commitment                        |
| Long Tenure               | Customer has already invested time         |
| Online Security = Yes     | Using more services                        |
| Tech Support = Yes        | Better customer experience                 |
| Automatic Payment Methods | Reduced payment friction                   |
| Dependents = Yes          | More stable customer profile               |
| Partner = Yes             | Often associated with longer subscriptions |
| Lower Monthly Charges     | Less price pressure                        |

Example Low-Risk Customer

Tenure = 60 months
Contract = Two Year
Online Security = Yes
Tech Support = Yes
Monthly Charges = $70

Model usually predicts:

Low Churn Probability
High Stay Probability


You can say:

"Based on both domain knowledge and the patterns
 learned by the model, customers with 
 month-to-month contracts, short tenure, 
 high monthly charges, no tech support, 
 and no online security tend to have higher 
 churn risk. On the other hand, customers with
  long tenure, long-term contracts, tech support 
  subscriptions, online security services, and 
  automatic payment methods tend to remain with 
  the company longer."


 "How Do You Know These Features Are Important?"

Current answer:

"These conclusions are based on business understanding of customer behavior and patterns commonly observed in churn datasets."

Better answer (future enhancement):

"To quantitatively measure feature importance, I can implement SHAP Explainability or analyze Logistic Regression coefficients. That would show exactly how much each feature contributes to the prediction."

This answer impresses interviewers because it shows you understand the difference between business intuition and model explainability.

One-Line Memory Trick

Think:

CHURN ↑
=
Short Tenure
+
Month-to-Month Contract
+
High Monthly Charges
+
No Security
+
No Tech Support


STAY ↑
=
Long Tenure
+
Two-Year Contract
+
Online Security
+
Tech Support
+
Auto Payment

