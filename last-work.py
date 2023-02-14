#!/usr/bin/env python
# coding: utf-8

# STREAMLIT PROJECT WORK

# Contents
# 
# 1. Introduction
# Data overview
# Conclusions
# 
# 2. Data preprocessing
# Header style
# Missing values
# Duplicates
# Conclusions
# 
# 3.Graphs
# Scatter chart graph
# Histogram graph
# Bar chart graph
# conclusions
# 

# Introduction
# 
# Over the years, an upsurge has been seen in data driven decision making in the modern business world. 
# With the revolutionary development in software technology, SQL, programming,Python,Streamlit. 
# Extracting and filtering valuable information from the data silos has become easy. 
# Then based on this vital, compelling, and valuable information, many important business decisions are taken.
# One of the various reasons to learn Data science is that nowadays, Data science helps in development and
# shaping our planet.

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


# Conclusions
# 
# Data on user behavior is stored in the file 'vehicles_us.csv.' There is no information about
# the quality of the data and all is loader n working fine.

# In[4]:


df['state'] = 'owned'
df.head()


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df = df.fillna(0)


# In[8]:


df.head()


# In[9]:


df.drop_duplicates()


# In[10]:


st.header('market of used of cars. Original data')
st.write(""""
#### Filter the data below to see ads by model
""")
show_new_cars = st.checkbox("Include new cars from the dealers")


# In[11]:


show_new_cars


# In[12]:


if not show_new_cars:
    df = df[df.state!='new']


# In[13]:


model_choice = df['model'].unique()
man_made_choice = st.selectbox('select_model:', model_choice)


# In[14]:


man_made_choice


# In[15]:


#creating min and max year as limits sliders
min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

#creating slider
year_range = st.slider( 
    'choose_years',
     value = (min_year,max_year),min_value = min_year,max_value = max_year)


# In[16]:


year_range


# In[17]:


#creating actual range base on the slider that will be used to filfter the dataset
actual_range=list(range(year_range[0],year_range[1]+1))


# In[18]:


filtered_type = df[(df.model==man_made_choice) & (df.model_year.isin(list(actual_range)))]

#showing  the finaltable in streamlit
st.table(filtered_type)


# Conclusions
# 
# In this chapter, i did data processing and all have been check. All duplicate have been check 
# and solutions haven apply to it also also NaN have been turned or change to 0.0 so in this 
# data all NaN is now 0.0. Missing valus have been clear and treated. To go further, this
# data is cleared and ready to be use to work. One more column was added to the dataset
# which is State and st.hearder and st.selectbox was also introduce in this section.

# In[19]:


st.header('days listed analysis')
st.write(""""
###### let's analyse what influence days_listed the most. we will check how distribution of days_listed varies depending on 
transmission,cylinders,type,state
""")

import plotly.express as px

#creating list of options to choose from
list = ['transmission','cylinders','type','state']

choice = st.selectbox('split for days_listed distribution',list)
transmission = choice
cylinders = choice
type = choice
#Plotly histogram
fig1 = px.histogram(df,x='days_listed',color=choice)
choice=('darkorange','white','red','black')
fig1.update_layout(
title = "<b> split of days_listed".format(list))

st.plotly_chart(fig1)


# In[20]:


fig1.show()


# This histogram graph analyse what influence days_listed the most in the dataset. with the help of the filters, 
# we can check how distribution of days_listed varies depending on transmission, cylinders, type, state.
# 
# in transmission, we have three sides and which is automatic,manual and other. In this stage we can see how the graph 
# move or change due to the distribution concren with the day listed. And also all colors apply to it also.
# 
# Here again we can see, automatic transmission was on high demand and followed by manual and then other.

# In[21]:


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


# In[22]:


fig2.show()


# This histogram graph, it introduce us to model production analysis  in the dataset.Which With the help of the filters,
# we can check how distribution of model production varies depending on condition, odometer, type, state.
# 
# Starting with condition in model production. In this stage we can see how the graph
# move or change due to the distribution concren with the model production and also all colors apply to it also.
# 
# Here all the stages of the conditions where apply to it, which is on the right side bar and they are good,like new,fair,
# 
# execellent,salvage and lastly new. And it all change accordingly to the stage of the condition.

# In[23]:


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

st.plotly_chart (fig3)


# In[24]:


fig3.show()


# This bar chart graph, it introduce us to year model analysis  in the dataset.
# Which With the help of the filters, we can check how distribution of model production varies
# depending on model_year, fuel, is_4wd, date_posted.
# 
# Starting with model year. In this stage we can see how the graph
# move or change due to the distribution concren with the model and the year of production and also all colors
# filter apply to it also.
# 
# Here the bar chart made it little bit differen in a way also clearer as well and self explained in a way. And
# also the demand and the production moved hand in hand, like they say in economic. That if more is demand then 
# more is produced.

# Final Conclusions
# 
# We created a streamlit wab page using the above dataset provider, that a company can use to keep track of his production. 
# Business owners are divided into salesmen and managers. Salesmen and managers work on departments. 
# A salesman's manager is predetermined by on which department he or she works on.
# 
# 
# In our case we have created the wab page according to the dataset for everyone who wishes to enhance his business or as a 
# customer who want to buy a car can use this page to study the market before he or she decide on to do.
# Any car dealer or customer who will choice the page will find it easier to make the right choice in buying or selling.
# 
# This Streamlit project was divided into three part and the first talks about dataset installation and abd data review.
# 
# 
# The second part brings out the dataset cleaning and making sure all is good for work and to work with.
# 
# 
# And lastly the graphs in the work was introduced in this last part and also well explained and why it enter 
# changes by your command. In all i will say it a go experiences for me to do something like this with the help of practicum,
# am glady and confidence too in working as a data scientists.
