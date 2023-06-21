####In Class Assignment 4

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

PortlandOregonHousingDF = pd.read_csv('C:\\Users\\yashh\\OneDrive\\Desktop\\PortlandOreganHousing.csv')

PortlandOregonHousingDF.head()

PortlandOregonHousingDF.info()

PortlandOregonHousingDF.describe()

ax = sns.scatterplot(x='Living Area (feet^2)', y = 'Price (1000$s)', data = PortlandOregonHousingDF)

PortlandOregonHousingDF.head()
PortlandOregonHousingDF.info()
data = pd.read_csv('C:\\Users\\yashh\\OneDrive\\Desktop\\ex1data2.txt', header = None)
data.head()
x = data.iloc[:,0]