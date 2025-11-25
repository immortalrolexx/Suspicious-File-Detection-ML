import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load dataset
data = pd.read_csv("dataset.csv")

# 2. Separate features and labels
X_text = data["content"]
y = data["label"]

# 3. Convert text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X_text)

# 4. Train–test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 5. Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Save model and vectorizer
joblib.dump(model, "suspicious_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and vectorizer saved successfully.")
