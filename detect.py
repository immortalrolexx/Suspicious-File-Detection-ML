import joblib

# Load saved model and vectorizer
model = joblib.load("suspicious_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("🔎 Suspicious File Detector")
print("----------------------------------")

# Get text description from user
text = input("Describe the file or its behaviour: ")

# Convert to features
X = vectorizer.transform([text])

# Predict
prediction = model.predict(X)[0]
probability = model.predict_proba(X)[0][1]

# Show result
if prediction == 1:
    print(f"\nResult: 🔴 SUSPICIOUS (Confidence: {probability*100:.2f}%)")
else:
    print(f"\nResult: 🟢 SAFE (Confidence: {(1 - probability)*100:.2f}%)")
