# 🏥 Medical Insurance Charges Prediction

### Machine Learning | Python | Scikit-learn | Streamlit

Predict estimated medical insurance charges based on personal and lifestyle information using a Machine Learning regression model.

🔗 **Live Demo:** [Try the Medical Insurance Prediction App](https://medical-insurance-prediction-glv9ww4vzixugn9rjdpk9x.streamlit.app/)

---

## 📌 Project Overview

Medical insurance charges can vary significantly depending on factors such as age, BMI, smoking habits, and family size.

This project develops a Machine Learning model that estimates medical insurance charges from user-provided information. The trained model is integrated into an interactive Streamlit web application, allowing users to enter their details and receive an estimated insurance cost.

The project demonstrates a complete Machine Learning workflow, from data preprocessing and feature engineering to model evaluation and deployment.

## 🎯 Project Objectives

- Analyze the factors associated with medical insurance charges.
- Preprocess and prepare data for Machine Learning.
- Engineer meaningful features to improve predictive performance.
- Train and evaluate regression models.
- Deploy the selected model as an interactive web application.
- Provide users with quick, accessible insurance cost estimates.

## 📊 Dataset Features

The model uses the following input features:

| Feature | Description |
|---|---|
| `age` | Age of the individual |
| `sex` | Gender |
| `bmi` | Body Mass Index |
| `children` | Number of dependent children |
| `smoker` | Smoking status |
| `region` | Residential region |

**Target variable:** `charges` — medical insurance charges.

## ⚙️ Machine Learning Workflow

1. **Data Understanding:** Explore the dataset, inspect feature distributions, and understand the target variable.
2. **Data Preprocessing:** Prepare numerical and categorical features for model training.
3. **Exploratory Data Analysis (EDA):** Investigate relationships between insurance charges and customer characteristics.
4. **Feature Engineering:** Create additional features to capture useful relationships:
   - `age_bmi`: Interaction between age and BMI.
   - `smoker_num`: Numerical representation of smoking status.
   - `age_smoker`: Interaction between age and smoking status.
   - `bmi_smoker`: Interaction between BMI and smoking status.
   - `bmi_category`: BMI groups based on defined ranges.
5. **Model Training:** Train and compare regression models.
6. **Model Evaluation:** Evaluate predictive performance using MAE, RMSE, and R².
7. **Deployment:** Integrate the selected model into a Streamlit application.

## 🤖 Selected Model

**Gradient Boosting Regressor with Huber Loss**

The selected model uses Huber loss, which combines aspects of squared-error and absolute-error losses and can be less sensitive to large residuals than squared-error loss alone.

Selected hyperparameters:

- `n_estimators`: 300
- `learning_rate`: 0.05
- `max_depth`: 3
- `min_samples_leaf`: 5
- `loss`: Huber

Feature engineering is applied before prediction.

## 📈 Model Performance

The selected model achieved the following results on the test dataset:

| Evaluation Metric | Result |
|---|---:|
| MAE | $1,494.35 |
| RMSE | $4,207.93 |
| R² Score | 0.9036 |

### Understanding the Results

- **MAE:** Predictions differ from actual charges by approximately $1,494 on average in absolute terms.
- **RMSE:** Larger prediction errors receive more weight, resulting in an RMSE of approximately $4,208.
- **R² Score:** The model explains approximately 90.36% of the variation in insurance charges in the evaluated test dataset.

These metrics describe performance on the test dataset. Actual prediction errors may vary for individual users and on new data.

## 🌐 Live Web Application

The application is built with Streamlit and provides an interactive interface where users can:

- Enter personal and lifestyle information.
- Submit their information to the trained model.
- View the estimated medical insurance charges.
- Test different input combinations.

🚀 **[Launch the Live Application](https://medical-insurance-prediction-glv9ww4vzixugn9rjdpk9x.streamlit.app/)**

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas & NumPy** — Data manipulation and numerical operations
- **Scikit-learn** — Model training, preprocessing, and evaluation
- **Matplotlib & Seaborn** — Data visualization
- **Joblib** — Saving and loading the trained model
- **Streamlit** — Interactive web application
- **Git & GitHub** — Version control and project hosting

## 📂 Project Structure

```text
Medical-Insurance-Prediction/
│
├── app.py
├── best_insurance_model.pkl
├── requirements.txt
└── README.md
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/JomanaSobhy-Hub/Medical-Insurance-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Medical-Insurance-Prediction
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at the local address provided by Streamlit.

**Note:** Use compatible Python and package versions for the saved model. The model file was trained with Scikit-learn 1.6.1.

## 🔮 Future Improvements

- Evaluate additional regression algorithms and compare their performance.
- Perform more systematic hyperparameter tuning.
- Add prediction intervals to communicate uncertainty.
- Improve explainability with feature importance and model interpretation tools.
- Expand testing across different customer profiles.
- Further improve the application's user experience and accessibility.

## ⚠️ Disclaimer

This application provides Machine Learning-based estimates for educational and demonstration purposes only. Predictions are not official insurance quotes, financial advice, or a guarantee of actual insurance costs.

## 👩‍💻 Author

**Jomana Sobhy Khalifa**

AI Student | Machine Learning Enthusiast

- **GitHub:** [JomanaSobhy-Hub](https://github.com/JomanaSobhy-Hub)
- **Project Repository:** [Medical Insurance Prediction](https://github.com/JomanaSobhy-Hub/Medical-Insurance-Prediction)
- **Live Demo:** [Streamlit Application](https://medical-insurance-prediction-glv9ww4vzixugn9rjdpk9x.streamlit.app/)

---

⭐ If you find this project interesting, feel free to explore the repository and try the live application!
