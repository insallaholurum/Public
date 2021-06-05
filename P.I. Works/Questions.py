#!/usr/bin/env python
# coding: utf-8

import pandas as pd
df = pd.read_csv("data.csv")

#question 1
Countries = df['country'].value_counts().index
for i in Countries:
    country = df.loc[df.country==i]
    try:
        minimum = test['daily_vaccinations'].min()
        df['daily_vaccinations'].fillna(value=minimum,inplace=True)
    except:
        df['daily_vaccinations'].fillna(0,inplace=True)
#control
print(df['daily_vaccinations'].isna().value_counts()[0] == len(df))

#question 2
print(list(df.groupby('country').median().sort_values(by='daily_vaccinations',ascending=False)[0:3].index))


#question3
print(df.loc[df.date=='1/6/2021']['daily_vaccinations'].sum())


#question4
"""
#SQL QUERY

SELECT coalesce(daily_vaccinations,median(daily_vaccinations))
FROM data 
GROUP BY country;

"""





# In[ ]:




