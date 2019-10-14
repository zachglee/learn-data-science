import numpy as np 
import pandas as pd 
import re
import nltk 
import matplotlib.pyplot as plt

print("beginning")

#%matplotlib inline

data_source_url = "Tweets.csv"

print("importing...")

airline_tweets = pd.read_csv(data_source_url)

print("hey we got here!")

print(airline_tweets.head())

plot_size = plt.rcParams["figure.figsize"] 
print(plot_size[0]) 
print(plot_size[1])

plot_size[0] = 8
plot_size[1] = 6
plt.rcParams["figure.figsize"] = plot_size
airline_tweets.airline.value_counts().plot(kind='pie', autopct='%1.0f%%')