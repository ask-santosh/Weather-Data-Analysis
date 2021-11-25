#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


weather_data = pd.read_csv("weatherHistory.csv")
# weather_data.columns = weather_data.iloc[0]
# weather_data.columns
# weather_data
# weather_data.head()
weather_data.columns.values


# In[5]:


weather_data = weather_data.iloc[1:]


# In[6]:


weather_data.head()


# In[7]:


list(weather_data.columns.values)


# In[ ]:


# We first convert all the numeric data to from object data type to float/int data type.


# In[8]:


weather_data['Temperature (C)'] = weather_data['Temperature (C)'].astype('float')
weather_data['Apparent Temperature (C)'] = weather_data['Apparent Temperature (C)'].astype('float')
weather_data['Humidity'] = weather_data['Humidity'].astype('float')
weather_data['Wind Speed (km/h)'] = weather_data['Wind Speed (km/h)'].astype('float')
weather_data['Wind Bearing (degrees)'] = weather_data['Wind Bearing (degrees)'].astype('int')
weather_data['Visibility (km)'] = weather_data['Visibility (km)'].astype('float')
weather_data['Loud Cover'] = weather_data['Loud Cover'].astype('int')
weather_data['Pressure (millibars)'] = weather_data['Pressure (millibars)'].astype('float')


# In[9]:


weather_data['Precip Type'].fillna(weather_data['Precip Type'].value_counts().index[0], inplace=True)


# In[ ]:


#After removing all the null values.


# In[10]:


weather_data.isnull().sum()


# In[ ]:


# Heat map representation of above data


# In[11]:


import seaborn as sns


# In[12]:


sns.heatmap(weather_data.isnull(), yticklabels=False, cbar=True)


# In[27]:


from datetime import timedelta
import datetime as dt
weather_data


# In[28]:


#Most frequent weather from the Summary column
# weather_data['Formatted Date'] = pd.to_datetime(weather_data['Formatted Date'])
weather = weather_data['Summary'].value_counts().reset_index()
weather.columns = ['Weather', 'Count']
weather


# In[ ]:


#We can observe that the most common weather that prevails is Partly cloudy


# In[35]:


import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(8,4)})
plt.xticks(rotation=90)
sns.lineplot(x=weather['Weather'], y=weather['Count'], data=weather)
plt.show()


# In[ ]:


#In the below graph we can observe that maximum temperature is when the weather is dry.


# In[36]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=90)
plt.title('Weather')
sns.barplot(x=weather_data['Summary'], y=weather_data['Temperature (C)'])


# In[ ]:





# In[ ]:





# In[45]:


#In the below graph remarks that maximum humidity is for the weather types: Foggy, Breezy and Foggy
#and Rainy weather'''


# In[44]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=90)
plt.title('Weather')
sns.barplot(x=weather_data['Summary'], y=weather_data['Humidity'])


# In[40]:


plt.figure(figsize=(8,4))
plt.title("Weather vs Pressue")
plt.xticks(rotation=90)
sns.lineplot(y=weather_data['Pressure (millibars)'],x=weather_data['Summary'])


# In[41]:


pip install pywedge


# In[43]:


import pywedge as pw
x = pw.Pywedge_Charts(weather_data, c=None, y='Humidity')
charts = x.make_charts()


# In[ ]:




