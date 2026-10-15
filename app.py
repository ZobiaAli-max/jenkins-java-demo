from flask import Flask, request, jsonify
import random
import math

app = Flask(__name__)

STUDENT_ROLL_NUMBER = "FA23-BDS-046"
SEED = 46

random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Lab 6 Linear Regression Prediction API",
        "registration_number": STUDENT_ROLL_NUMBER
    })


@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])

        if not all(math.isfinite(x) for x in (x1, x2, x3)):
            raise ValueError("Inputs must be finite numbers")

    except (KeyError, ValueError):
        return jsonify({
            "error": "Provide finite numeric values for x1, x2, and x3"
        }), 400

    y = a1 * x1 + a2 * x2 + a3 * x3 + b

    return jsonify({
        "registration_number": STUDENT_ROLL_NUMBER,
        "prediction": round(y, 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
