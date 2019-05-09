from __future__ import print_function
from scipy.stats import skew, norm, probplot
import numpy as np, seaborn as sns, pandas as pd, matplotlib.pyplot as plt, math
from pylab import rcParams
import matplotlib.pyplot as plt

telcom = pd.read_csv(r'C:\Users\Jaqen\Downloads\Churn.csv')

telcom.dropna(inplace=True)
telcom.shape

telcom['Churn'].replace(to_replace='Yes', value=1, inplace=True)
telcom['Churn'].replace(to_replace='No', value=2, inplace=True)
telcom['Churn'].head(5)

# 可视化
churnvalue = telcom['Churn'].value_counts()
lables = telcom['Churn'].value_counts().index

rcParams['figure.figsize']=6, 6
plt.pie(churnvalue, labels=lables, colors=["whitesmoke", "yellow"], explode=(0.1, 0), autopct='%1.1f%%', shadow=True)
plt.title('Proportions of Customer Churn')
plt.show()

f, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

plt.subplot(2,2,1)
gender = sns.countplot(x='gender', hue='Churn', data=telcom, palette='Pastel2')
plt.xlabel('gender')
plt.title('Churn by Gender')

plt.subplots(2,2,2)
seniorcitizen = sns.countplot(x='SeniorCitizen', hue='Churn', data=telcom, palette='Pastel2')
plt.xlabel('partner')
plt.title('Churn by partner')

plt.subplots(2,2,3)
partner = sns.countplot(x='Partner', hue='Churn', data=telcom, palette='Pastel2')
plt.xlabel('partner')
plt.title('Churn by Partner')

plt.subplots(2,2,4)
dependents = sns.countplot(x='Dependents', hue='Churn', data=telcom, palette='Pastel2')
plt.xlabel('dependents')
plt.title('Churn by Partner')