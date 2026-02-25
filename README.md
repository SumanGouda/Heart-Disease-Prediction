# 🫀 Heart Disease Prediction Web App

A Machine Learning powered web application that predicts the risk of heart disease based on medical input parameters.

Built using:
- 🐍 Python
- 🤖 Scikit-Learn
- 🌐 Flask
- 🎨 HTML & CSS

---

## 🚀 Project Overview

This application allows users to enter medical details such as age, blood pressure, cholesterol levels, and more.

The trained ML model predicts:
- ✅ Low Risk of Heart Disease
- ⚠️ High Risk of Heart Disease

It also displays the model confidence score.

---

## 📊 Machine Learning Model

- Algorithm: Logistic Regression *(or replace with your algorithm name)*
- Dataset: UCI Heart Disease Dataset
- Target Variable: Presence of Heart Disease (0 = No, 1 = Yes)

### Features Used:
- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Rest ECG (restecg)
- Max Heart Rate (thalach)
- Exercise Induced Angina (exang)
- Oldpeak
- Slope
- CA
- Thal

---

## 🖥️ Web Application Features

- Clean and simple user interface
- Styled input forms
- Dynamic prediction result page
- Model confidence percentage display
- Responsive layout
- Custom styled buttons

---

## 📂 Project Structure

```
Heart-Disease-Prediction/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install flask scikit-learn numpy pandas
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Test Data

| Feature | Value |
|----------|-------|
| Age | 58 |
| Sex | Male |
| Resting BP | 150 |
| Cholesterol | 260 |
| Max Heart Rate | 120 |
| Oldpeak | 2.3 |
| Chest Pain | Asymptomatic |
| Fasting Blood Sugar | Greater than 120 mg/dl |
| Rest ECG | ST-T-abnormalilty |
| Exercise Included Angina | Yes |
| Slope | Flat |
| CA | 2 |
| Thal | Reversible Defect |

---

## 📈 Future Improvements

- Add model accuracy display
- Add feature importance visualization
- Deploy to cloud (Render / Railway / AWS)
- Improve UI animations
- Add authentication system
- Add dashboard analytics

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Logic |
| Flask | Web Framework |
| Scikit-Learn | Machine Learning |
| HTML | Structure |
| CSS | Styling |

---

## 📌 Disclaimer

This project is for educational purposes only and should not be used as a substitute for professional medical advice.

---

## 👨‍💻 Author

Developed by **Suman**