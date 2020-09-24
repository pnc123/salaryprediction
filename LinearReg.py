import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

from sklearn.externals import joblib


df = pd.read_csv("Salary_DataSet.csv")


lr=LR()
lr.fit(df[['Experences']],df['Salary'])
y=lr.predict([[1.6]])
print(y)

joblib.dump(lr,"model.pkl")
