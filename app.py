"""
FastAPI app serving the Heart Disease Risk Prediction model.

Expects a trained model at model/heart_disease_rf_model.pkl, trained on the
RAW (non-one-hot, non-scaled) 13-feature dataframe, in this exact column order:
    age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
 
"""

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
import joblib
import os

app = FastAPI(title="Heart Disease Risk Prediction")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

MODEL_PATH = os.path.join(BASE_DIR, "model", "heart_disease_rf_model.pkl")

# Exact column order the model was trained on (raw df.drop('target', axis=1).columns)
FEATURE_ORDER = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

model = None
model_load_error = None
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model_load_error = str(e)


@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"result": None, "model_load_error": model_load_error}
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    age: int = Form(...),
    sex: int = Form(...),
    cp: int = Form(...),
    trestbps: int = Form(...),
    chol: int = Form(...),
    fbs: int = Form(...),
    restecg: int = Form(...),
    thalach: int = Form(...),
    exang: int = Form(...),
    oldpeak: float = Form(...),
    slope: int = Form(...),
    ca: int = Form(...),
    thal: int = Form(...),
):
    if model is None:
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "result": None,
                "model_load_error": model_load_error or "Model failed to load.",
                "form_values": locals(),
            },
        )

    input_dict = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal,
    }

    # Build a single-row DataFrame in the exact training column order.
    input_df = pd.DataFrame([input_dict], columns=FEATURE_ORDER)

    prediction = int(model.predict(input_df)[0])
    # NOTE: in this specific dataset, target=1 corresponds to the healthier outcome
    # and target=0 to disease presence (confirmed empirically - verify with your own
    # pd.crosstab(df['cp'], df['target']) style checks if you regenerate the dataset).
    # So "risk of heart disease" = P(class 0), not P(class 1).
    probability = float(model.predict_proba(input_df)[0][0])

    risk_percent = round(probability * 100, 1)

    if risk_percent < 30:
        risk_level = "Low"
    elif risk_percent < 60:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    result = {
        "prediction": prediction,
        "risk_percent": risk_percent,
        "risk_level": risk_level,
    }

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "result": result,
            "model_load_error": None,
            "form_values": input_dict,
        },
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
