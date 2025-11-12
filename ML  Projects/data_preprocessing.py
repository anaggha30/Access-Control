import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load datasets
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# Check missing values
print("Missing Values (Train):", train_df.isnull().sum().sum())
print("Missing Values (Test):", test_df.isnull().sum().sum())

# Encoding categorical data
categorical_features = ['RESOURCE', 'MGR_ID', 'ROLE_ROLLUP_1', 'ROLE_ROLLUP_2', 
                        'ROLE_DEPTNAME', 'ROLE_TITLE', 'ROLE_FAMILY_DESC', 
                        'ROLE_FAMILY', 'ROLE_CODE']

encoder = ColumnTransformer(transformers=[
    ('encoder', OneHotEncoder(handle_unknown='ignore'), categorical_features)],
    remainder='passthrough')

X_train_encoded = encoder.fit_transform(train_df.drop('ACTION', axis=1))
X_test_encoded = encoder.transform(test_df.drop('id', axis=1))

print("Encoded shape (Train):", X_train_encoded.shape)
print("Encoded shape (Test):", X_test_encoded.shape)

# Feature Scaling (illustration)
scaler = StandardScaler(with_mean=False)

X_train_scaled = scaler.fit_transform(X_train_encoded)
X_test_scaled = scaler.transform(X_test_encoded)

print("Feature scaling applied successfully.")

from sklearn.model_selection import train_test_split

# Target variable
y = train_df['ACTION']

# Split data into training and testing sets (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_train_scaled, y, test_size=0.2, random_state=42
)

print("Data splitting completed:")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")

import joblib

joblib.dump(X_train, 'X_train.pkl')
joblib.dump(X_test, 'X_test.pkl')
joblib.dump(y_train, 'y_train.pkl')
joblib.dump(y_test, 'y_test.pkl')
