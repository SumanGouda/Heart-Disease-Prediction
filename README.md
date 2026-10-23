# Heart Disease Risk Prediction

A web app that estimates a person's risk of heart disease from 13 clinical measurements. A Random Forest model, tuned with cross-validated grid search, sits behind a FastAPI backend with a simple HTML form. The whole thing is Dockerized, so you can run it with one command.

> **Disclaimer:** This is a learning and portfolio project. It is not a medical device and must not be used for diagnosis or treatment decisions.

## Quick start (Docker)

```bash
docker run -p 7860:7860 sumangouda/heart-disease-api:latest
```

Then open [http://localhost:7860](http://localhost:7860), fill in the form, and submit.

## What it does

1. You enter 13 clinical values in the web form.
2. The backend builds a one-row DataFrame in the exact column order the model was trained on.
3. The model returns a heart-disease risk percentage, shown as **Low**, **Moderate**, or **High**.

| Risk percent | Level |
|---|---|
| below 30 | Low |
| 30 to 59.9 | Moderate |
| 60 and above | High |

## Input features

| Feature | Description |
|---|---|
| `age` | Age in years |
| `sex` | 1 = male, 0 = female |
| `cp` | Chest pain type (0 to 3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar above 120 mg/dl (1 = yes, 0 = no) |
| `restecg` | Resting ECG result (0 to 2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina (1 = yes, 0 = no) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment (0 to 2) |
| `ca` | Number of major vessels colored by fluoroscopy (0 to 4) |
| `thal` | Thalassemia result (categorical code) |

## Model

The dataset is the classic heart disease dataset (303 rows, 13 features plus a binary target), stored in `data/heart.csv`. Three classifiers were tuned with `GridSearchCV` (5-fold, scored by ROC AUC) on an 80/20 train/test split:

| Model | Best CV AUC | Test accuracy |
|---|---|---|
| **Random Forest** | **0.9134** | **0.8852** |
| XGBoost | 0.9036 | 0.8525 |
| Decision Tree | 0.7968 | 0.8361 |

Random Forest and XGBoost were then compared with 10-fold cross-validation on the full data. Random Forest scored 0.9157 ± 0.0406 AUC against 0.9073 ± 0.0374 for XGBoost, so Random Forest was saved as the final model (`model/heart_disease_rf_model.pkl`).

Best Random Forest parameters: `n_estimators=300`, `max_depth=5`, `min_samples_split=5`, `min_samples_leaf=2`.

**Note on the target:** in this version of the dataset, `target = 1` is the healthier outcome and `0` means disease is present. The app therefore reports risk as the predicted probability of class 0, not class 1.

## Run locally (without Docker)

```bash
pip install -r requirements.txt
python app.py
```

The app starts at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Retrain the model

Open `notebook/Heart Disease Prediction.ipynb` and run all cells. The last cell saves `heart_disease_rf_model.pkl`. Move it into the `model/` folder, keeping the same 13-column feature order, before restarting the app.

## Project structure

```
.
├── app.py                  # FastAPI app: form page and /predict endpoint
├── Dockerfile
├── requirements.txt
├── data/
│   └── heart.csv           # dataset
├── model/
│   └── heart_disease_rf_model.pkl
├── notebook/
│   └── Heart Disease Prediction.ipynb   # EDA, tuning, model comparison
├── static/
│   └── style.css
└── templates/
    └── index.html          # Jinja2 form and result page
```

## Tech stack

Python, scikit-learn, XGBoost, pandas, FastAPI, Jinja2, Docker.
