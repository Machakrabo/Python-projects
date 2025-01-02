#setup
#importing libraries
import pandas as pd
import numpy as np
#Import visualization packages "Matplotlib" and "Seaborn"
import matplotlib.pyplot as plt
import seaborn as sns
#setting up the location of the file and the columns and reading the file.
url = "https://raw.githubusercontent.com/Machakrabo/Python-projects/main/automobileEDA.csv"
df = pd.read_csv(url)
print(df.head())
#display only the first rows
print(df.info())
#Are values missing?
print(df.isnull().sum())
#Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.
# Ensure relevant columns are numeric
#columns_to_convert = ["bore", "stroke", "compression-ratio", "horsepower"]
#df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')
Matrix_Corr=df[["bore", "stroke", "compression-ratio", "horsepower"]].corr()
print(Matrix_Corr)
# Visualization
sns.regplot(x="engine-size", y="price", data=df)
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.title("Relationship between Engine Size and Price")
plt.show()