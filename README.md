# Bank Customer Churn ML with Streamlit

Predict customer churn in a bank **`Classic Binary Classification Problem `** using machine learning techniques.  
This project includes:
- A **[Jupyter Notebook](https://github.com/mazen-alasas/Bank-Customer-Churn-ML/blob/main/notebooks/training.ipynb)** for data analysis and modeling.
- An interactive **[Streamlit Web App]()** for deployment.

---

## Table of Contents
- [Bank Customer Churn ML with Streamlit](#bank-customer-churn-ml-with-streamlit)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Dataset](#dataset)
  - [Features](#features)
  - [How to Run](#how-to-run)
  - [Project Structure](#project-structure)
  - [Results](#results)
  - [Contributing](#contributing)
  - [Contact](#contact)

---

## About the Project
**Goal**: Predict whether a customer continues with their account or closes it (e.g., churns) using machine learning models.  

**Tech Stack**:  
- Python  
- Pandas  
- Matplotlib/Seaborn  
- Scikit-learn  
- Streamlit  

**Motivation**: Churn prediction is crucial for customer retention and helps banks improve their services.

---

## Dataset
The dataset used for this project is the [Bank Churn Dataset on Kaggle](https://www.kaggle.com/competitions/playground-series-s4e1/overview).  

---

## Features
- `Customer` ID: A unique identifier for each customer
- `Surname`: The customer's surname or last name
- `Credit` Score: A numerical value representing the customer's credit score
- `Geography`: The country where the customer resides (France, Spain or Germany)
- `Gender`: The customer's gender (Male or Female)
- `Age`: The customer's age.
- `Tenure`: The number of years the customer has been with the bank
- `Balance`: The customer's account balance
- `NumOfProducts`: The number of bank products the customer uses (e.g., savings account, credit card)
- `HasCrCard`: Whether the customer has a credit card (1 = yes, 0 = no)
- `IsActiveMember`: Whether the customer is an active member (1 = yes, 0 = no)
- `EstimatedSalary`: The estimated salary of the customer
- `Exited`: Whether the customer has churned (1 = yes, 0 = no)

---

## How to Run
To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mazen-alasas/Bank-Customer-Churn-ML.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Bank-Customer-Churn-ML
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
   ```

**Note:** This project was developed using Python 3.12

---

## Project Structure
```plaintext
📁 Bank-Customer-Churn-ML
├── 📂 app
│   ├── app.py
│   └── utils.py
├── 📂 data 
│   ├── sample_submission.csv
│   ├── test.csv
│   └── train.csv
├── 📂 images
│   └── cm.png
├── 📂 notebooks
│   └── training.ipynb
├── LICENSE
├── README.md
├── best_model.pkl
└── requirements.txt
```

---

## Results
- **Model Performance:**
  - Accuracy: `86.53%`
  - Precision: `75.47%`
  - Recall: `54.63%`
  - F1 Score: `63.38%`
  - Confusion matrix
   <p align = "center">
      <img src="images\cm.png">
   </p>
---

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.  

---

## Contact
Created by [Mazen Ahmed Alasas](https://github.com/mazen-alasas) - feel free to reach out!
  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mazen-ahmed-alasas-772831244/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@mazen_labs)

