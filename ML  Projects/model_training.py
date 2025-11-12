import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Step 1: Load data again clearly
train_df = pd.read_csv('train.csv')

# Step 2: Encoding categorical data
categorical_features = ['RESOURCE', 'MGR_ID', 'ROLE_ROLLUP_1', 'ROLE_ROLLUP_2', 
                        'ROLE_DEPTNAME', 'ROLE_TITLE', 'ROLE_FAMILY_DESC', 
                        'ROLE_FAMILY', 'ROLE_CODE']

encoder = ColumnTransformer(transformers=[
    ('encoder', OneHotEncoder(handle_unknown='ignore'), categorical_features)],
    remainder='passthrough')

X_encoded = encoder.fit_transform(train_df.drop('ACTION', axis=1))

# Step 3: Feature Scaling
scaler = StandardScaler(with_mean=False)
X_scaled = scaler.fit_transform(X_encoded)

# Step 4: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, train_df['ACTION'], test_size=0.2, random_state=42)

# Decision Tree Model (Corrected)
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)  # <-- corrected line (X_train, y_train)

y_pred_dt = dt.predict(X_test)
print("Decision Tree Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))


import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load split data
X_train = joblib.load('X_train.pkl')
X_test = joblib.load('X_test.pkl')
y_train = joblib.load('y_train.pkl')
y_test = joblib.load('y_test.pkl')

# Train Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Predict and evaluate
y_pred_dt = dt.predict(X_test)
print("Decision Tree Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))

