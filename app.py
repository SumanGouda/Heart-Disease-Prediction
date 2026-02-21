# heart_project/app.py
from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model once when server starts
model_path = os.path.join(os.getcwd(), "knn_model.pkl")
model = joblib.load(model_path)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    # -------- Continuous Features --------
    age = int(request.form["age"])
    trestbps = int(request.form["trestbps"])
    chol = int(request.form["chol"])
    thalach = int(request.form["thalach"])
    oldpeak = float(request.form["oldpeak"])

    # -------- Categorical Features --------
    sex = int(request.form["sex"])
    cp = int(request.form["cp"])
    fbs = int(request.form["fbs"])
    restecg = int(request.form["restecg"])
    exang = int(request.form["exang"])
    slope = int(request.form["slope"])
    ca = int(request.form["ca"])
    thal = int(request.form["thal"])

    # -------- Build Feature Vector (Exact Order) --------
    features = [
        age,
        trestbps,
        chol,
        thalach,
        oldpeak
    ]

    # One-hot encoding (must match training column order)

    # sex
    features += [1 if sex == 0 else 0, 1 if sex == 1 else 0]

    # cp (0-3)
    features += [1 if cp == i else 0 for i in range(4)]

    # fbs
    features += [1 if fbs == 0 else 0, 1 if fbs == 1 else 0]

    # restecg (0-2)
    features += [1 if restecg == i else 0 for i in range(3)]

    # exang
    features += [1 if exang == 0 else 0, 1 if exang == 1 else 0]

    # slope (0-2)
    features += [1 if slope == i else 0 for i in range(3)]

    # ca (0-4)
    features += [1 if ca == i else 0 for i in range(5)]

    # thal (0-3)
    features += [1 if thal == i else 0 for i in range(4)]

    # -------- Prediction --------
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1]

    return render_template(
        "result.html",
        prediction=prediction,
        probability=round(probability * 100, 2)
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)