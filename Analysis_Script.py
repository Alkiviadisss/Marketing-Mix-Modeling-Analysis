import pandas as pd
import numpy as np
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# --- Import Data ---#
df = pd.read_csv("advertising.csv")

# --- Data Cleaning & Organization ---#
Question = input("Print Data Cleaning Results Y/N")
if Question == "Y":
   Q1 = df.quantile(0.25)
   Q3 = df.quantile(0.75)
   IQR = Q3 - Q1
   lower_bound = Q1 - 1.5 * IQR
   upper_bound = Q3 + 1.5 * IQR
   outliers_count = ((df < lower_bound) | (df > upper_bound)).sum()
   show_outliers = ((df < lower_bound) | (df > upper_bound))
   print(f"Outliers: {outliers_count}")
   print(df[show_outliers.any(axis=1)])
   print(df.isnull().sum())
   print(df.duplicated().sum())
else:
   pass

# --- Data Analysis (EDA) ---#
# Descriptive Analysis
Question1 = input("Print Descriptive Analysis Y/N")
if Question1 == "Y":
   print(df.head())
   print (df.describe())
   print(df.shape)
   print(df.info)
   Total_Spending = (df['TV'] + df['Radio'] + df['Newspaper']).sum()
   print("Total Spending In Thousands is : ", Total_Spending)
else:
    pass

# Inferential Analysis
# Bar Plot To Explore The Data
Question2 = input("Print Plots? Y/N")
if Question2 == "Y":
   Category_Totals = df[['TV', 'Radio', 'Newspaper']].sum()
   Spending_plot = plt.bar(Category_Totals.index, Category_Totals.values, color=['#3498db', '#e67e22', '#2ecc71'])
   plt.title('Total Spending in Each Category')
   plt.ylabel(' Thousands ($)')
   plt.show()
else:
   pass

# Correlations
Question3 = input("Print Correlations & Heatmap? Y/N")
if Question3 == "Y":
   R = df[['TV', 'Radio', 'Newspaper', 'Sales']].corr()
   print("Correlation Coefficient Matrix: ", R)
   heatmap_plt = plt.imshow(R)
   plt.title('Correlation Coefficient')
   plt.show()
else:
   pass

# Linear Regression Model
Question4 = input("Print Regression Model & Corrrelations(R,R2) Y/N")
if Question4 == "Y":
   R = df[['TV', 'Radio', 'Newspaper', 'Sales']].corr()
   x = df["TV"].to_numpy().reshape(-1, 1)
   y = df["Sales"].to_numpy().reshape(-1, 1)
   model = LinearRegression()
   model.fit(x, y)
   R2 = model.score(x, y)
   y_pred = model.predict(x)
   mae = mean_absolute_error(y, y_pred)
   print("R ", R)
   print("R2: ", R2)
   print("MAE: ", mae)
   plt.scatter(x, y, alpha=0.5, label='Data')
   plt.plot(x, model.predict(x), color='red', linewidth=2, label='Linear Regression Model')
   plt.xlabel('TV')
   plt.ylabel('Sales')
   plt.title('Linear Regression: TV vs Sales')
   plt.show()
else:
   pass

# --- Results ---#
#1] ROAS  = Sales/TV <=> 27.000000/296.400000 = 0.0910931174
#   ROAS  = Sales/Radio <=> 27.000000/49.600000 = 0,5443548387096774
#   for every 1000$ we spend on advertising in TV, we sell 91 units (Strong Connection)   (Low Risk / High Stability)
#   for every 1000$ we spend on advertising in Radio, we sell 544 units (Weak Connection)  (Low Risk / High Stability)
#2] ROAS  = Sales/TV <=> 27.000000/114.000000 = 0,2368421052631579
#   for every 1000$ we spend on advertising in Newspaper, we sell 236 units (Weak Connection)  (High Risk / Irrelevant)
#3) MAE = 1.8305872641932412
#   for the total 15.130 units, the model falls down 1.830 units
