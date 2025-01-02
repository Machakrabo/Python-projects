#setup
#importing libraries
import pandas as pd
import numpy as np
#Import visualization packages "Matplotlib" and "Seaborn"
import matplotlib.pyplot as plt
import seaborn as sns
#setting up the location of the file and the columns and reading the file.
path ="D:\Documents\Maloshree\2025\Python projects\automobileEDA.csv"
df = pd.read_csv(path)
print(df.head())
print(df.info())
print(df.isnull().sum())
#cols=["symboling", "normalized-losses","make","aspiration","num-of-doors","body-style","drive-wheels","engine-location",
      #"wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg",
      #"price","city-L/100km","horsepower-binned","diesel","gas"]
