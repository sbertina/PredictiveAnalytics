# -*- coding: utf-8 -*-
"""LVADSUSR77_Bertina_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sb72FKLQLOaxLweXrMbd-Ajsw7RU_nj2
"""

#importing modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#reading data
data = pd.read_csv('/content/booking.csv')
data.head()

# data cleaning
imputer = SimpleImputer(strategy='mean')
data[['number of adults', 'number of children', 'number of weekend nights', 'number of week nights', 'lead time', 'average price', 'special requests']] = imputer.fit_transform(data[['number of adults', 'number of children', 'number of weekend nights', 'number of week nights', 'lead time', 'average price', 'special requests']])

data.columns

label_encoder = LabelEncoder()
data['type of meal'] = label_encoder.fit_transform(data['type of meal'])
data['room type'] = label_encoder.fit_transform(data['room type'])
data['market segment type'] = label_encoder.fit_transform(data['market segment type'])
data['booking status'] = label_encoder.fit_transform(data['booking status'])

# cleaning the data
data.drop(['Booking_ID', 'date of reservation'], axis=1, inplace=True)

X = data.drop('booking status', axis=1)
y = data['booking status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fitting the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Accuracy
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))