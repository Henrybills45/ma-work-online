#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# In[2]:


df = pd.read_csv("vehicles_us.csv",sep =',')
df = df.drop(df.columns[0], axis = 1)


# In[3]:


df.head()


# In[4]:


df['state'] = 'owned'
df


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df = df.fillna(0)


# In[8]:


df.head


# In[9]:


df.drop_duplicates()


# In[10]:


df.isna().sum()


# In[11]:


df.info()


# In[12]:


st.header('market of used of cars. Original data')
st.write(""""
#### Filter the data below to see ads by model
""")
show_new_cars = st.checkbox("Include new cars from the dealers")


# In[13]:


show_new_cars


# In[14]:


if not show_new_cars:
    df = df[df.state!='new']


# In[15]:


model_choice = df['model'].unique()
man_made_choice = st.selectbox('select_model:', model_choice)


# In[16]:


man_made_choice


# In[17]:


#creating min and max year as limits sliders
min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

#creating slider
year_range = st.slider( 
    'choose_years',
     value = (min_year,max_year),min_value = min_year,max_value = max_year)


# In[18]:


year_range


# In[19]:


#creating actual range base on the slider that will be used to filfter the dataset
actual_range=list(range(year_range[0],year_range[1]+1))


# In[20]:


filtered_type = df[(df.model==man_made_choice) & (df.model_year.isin(list(actual_range)))]

#showing  the finaltable in streamlit
st.table(filtered_type)


# In[21]:


df


# In[22]:


st.header('days listed analysis')
st.write(""""
###### let's analyse what influence days_listed the most. we will check how distribution of days_listed varies depending on 
transmission,cylinders,type,state
""")

import plotly.express as px

#creating list of options to choose from
list_for_hist = ['transmission','cylinders','type','state']

choice_for_hist = st.selectbox('split for days_listed distribution', list_for_hist)

#Plotly histogram
fig1 = px.histogram(df, x = 'days_listed', color = choice_for_hist)

fig1.update_layout(
title = '<b> split of days_listed by {}</b>'. format(choice_for_hist))

st.plotly_chart(fig1)


# In[23]:


fig1.show()


# In[24]:


st.header('model production analysis')
st.write(""""
###### let's analyse what influence model production the most. we will check how distribution of model production varies depending on 
condition,odometer,type,date_posted
""")

import plotly.express as px

#creating list of options to choose from
list_for_scatter = ['condition','cylinders','model_year','state']

choice_for_scatter = st.selectbox('split for model production', list_for_scatter)

#Plotly histogram
fig2 = px.scatter(df, x = 'model', color = choice_for_scatter)

fig2.update_layout(
title = '<b> split of model by {}</b>'. format(choice_for_scatter))

st.plotly_chart(fig2)


# In[25]:


fig2.show()


# In[26]:


st.header('model year analysis')
st.write(""""
###### let's analyse what influence model year  the most. we will check how distribution of model year varies depending on 
model_year,fuel,is_4wd,date_posted
""")

import plotly.express as px

#creating list of options to choose from
list_for_bar = ['model_year','fuel','is_4wd','date_posted']

choice_for_bar = st.selectbox('split for model production', list_for_bar)

#Plotly histogram
fig3 = px.bar(df, x = 'model', color = choice_for_bar)

fig3.update_layout(
title = '<b> split of model by {}</b>'. format(choice_for_bar))

st.plotly_chart(fig3)


# In[27]:


fig3.show()

