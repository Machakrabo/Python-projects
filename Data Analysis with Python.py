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
#datatype of the columns
print(df.dtypes)
#data type of a specific column for example of column "body-style"
print("Data type of column 'body-style' is:\n")
print(df["body-style"].dtype)
#Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.
# Ensure relevant columns are numeric
#columns_to_convert = ["bore", "stroke", "compression-ratio", "horsepower"]
#df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')
matrix_corr=df[["bore", "stroke", "compression-ratio", "horsepower"]].corr()
print(matrix_corr)
# Visualization1
sns.regplot(x="engine-size", y="price", data=df)
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.title("Relationship between Engine Size and Price")
plt.show()
#Find the correlation between x="stroke" and y="price".
matrix_corr2=df[["stroke","price"]].corr()
print(matrix_corr2)
# Visualization2
sns.boxplot(x="body-style", y="price", data=df)
plt.xlabel("body-style")
plt.ylabel("Price")
plt.title("Relationship between body-style and Price")
plt.show()
#Using descriptive statistical analysis function
descriptive_Analysis_All = df.describe()
print(descriptive_Analysis_All)
#value count of the horsepower of the cars greater than 100 HP
count_horsepower_plus100 = df["horsepower"][df["horsepower"] > 100].value_counts().to_frame()
print (count_horsepower_plus100)
#value count of the horsepower of the cars lesser than 100 HP
count_horsepower_less100 = df["horsepower"][df["horsepower"] < 100].value_counts().to_frame()
print (count_horsepower_less100)
#value count of the horsepower of cars between 50 and 70 HP
count_horsepower_btwn_50_70 = df["horsepower"][(df["horsepower"] > 50) & (df["horsepower"] < 70)].value_counts().to_frame()
print(count_horsepower_btwn_50_70)
#identify the cars having horsepower between 50 and 70 HP
horsepower_btwn_50_70_all = df[["horsepower", "make", "body-style", "aspiration"]][(df["horsepower"] > 50) & (df["horsepower"] < 70)]
print("the cars having horsepower between 50 and 70 HP are \n:", horsepower_btwn_50_70_all)