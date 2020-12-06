#!/usr/bin/env python
# coding: utf-8


#Gerekli Kütüphaneler
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import openpyxl


# Importing the dataset
dataset = pd.read_excel('laptop-veri çekme.xlsx')
X = dataset.iloc[:, :-1].values #X:Bağımsız Değişken
y = dataset.iloc[:, -1].values  #y:Bağımlı Değişken
print(X)
print(y)

# Taking care of missing data SimpleImputer:Boş olan verileri değer girilmesini sağlıyor
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit(X[:, 4:8]) #imputer nesnesini fit:uygula 
X[:, 4:8] = imputer.transform(X[:, 4:8]) #transform fit de uyguladığımız kısımları burada ata
print(X)

# Encoding categorical data
# Encoding the Independent Variable
# OneHotEncoder kullanmamızın sebebi:binary şeklinde sayısal veriye çevir 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# Encoding categorical data
# Encoding the Independent Variable
# OneHotEncoder kullanmamızın sebebi:binary şeklinde sayısal veriye çevir 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# Encoding categorical data
# Encoding the Independent Variable
# OneHotEncoder kullanmamızın sebebi:binary şeklinde sayısal veriye çevir 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [2])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# Encoding the Dependent Variable
# Label Encoding : Sayısal veriye çeviriyor
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)


# Splitting the dataset into the Training set and Test set
# Veri setini test ve train olarak ayırmış olduk
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)


# Feature Scaling 
# Veri Ölçeklemeye yarar yani veriler arasındaki değer aralıklarını belli bir aralığa sıkıştırıyor
from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
X_train[:, 8:] = sc.fit_transform(X_train[:, 8:])
X_test[:, 8:] = sc.transform(X_test[:, 8:])
print(X_train)
print(X_test)








