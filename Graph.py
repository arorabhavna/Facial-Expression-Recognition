import matplotlib
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from collections import Counter
data = pd.read_csv('database.csv')
data.set_index("Name", inplace=True)
data.head()
with open("./temp/list.txt") as f:
    l=f.read().splitlines()
age = pd.DataFrame(columns=['Age'])
gender={'male':0,'female':0}
education = {}
profession ={}
for i in l:
    try:
        age.loc[len(age)] = data.loc[i]['Age']
        gender[data.loc[i]['Gender']] += 1
        if data.loc[i]['Education'] not in education:
            education[data.loc[i]['Education']]=0
        education[data.loc[i]['Education']]+=1
        if data.loc[i]['Profession'] not in education:
            profession[data.loc[i]['Profession']]=0
        profession[data.loc[i]['Profession']]+=1
    except:
        continue
age['bin'] = pd.cut(age['Age'], list(range(0, 101, 10)),labels=['1-10', '10-20', '20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100'])
plt.figure()
temp=Counter(age['bin'])
plt.bar(temp.keys(),temp.values())
plt.savefig('./temp/Age.png')
plt.figure()
plt.bar(gender.keys(),gender.values())
plt.savefig('./temp/Gender.png')
plt.figure()
plt.bar(education.keys(), education.values())
plt.savefig('./temp/Education.png')
plt.figure()
plt.bar(profession.keys(), profession.values())
plt.savefig('./temp/Profession.png')
