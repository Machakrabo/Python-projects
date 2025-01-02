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
print(df.info())
print(df.isnull().sum())
