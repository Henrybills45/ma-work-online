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
# 3. Graphs
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

# In[33]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# In[34]:


df = pd.read_csv("vehicles_us.csv",sep =',')
df = df.drop(df.columns[0], axis = 1)


# In[35]:


df.head()


# Conclusions
# 
# Data on user behavior is stored in the file 'vehicles_us.csv.' There is no information about
# the quality of the data and all is loader n working fine.

# In[36]:


df.paint_color.fillna(value = 'no_info', inplace = True)


# In[37]:


df['state'] = 'owned'
df.head()


# In[38]:


df.is_4wd.fillna(value = 'False', inplace = True)


# In[39]:


df.head()


# In[40]:


df.shape


# In[41]:


df.duplicated().sum()


# In[42]:


# Removing duplicate 
df.drop_duplicates()


# In[43]:


df. describe()


# In[44]:


df['model_year'].fillna(df['model_year'].median(),inplace = True)


# In[45]:


df['cylinders'].fillna(df['cylinders'].median(),inplace = True)


# In[46]:


df['odometer'].fillna(df['odometer'].mean(),inplace = True)


# In[47]:


df.head()


# In[48]:


st.header('market of used of cars. Original data')
st.write(""""
#### Filter the data below to see ads by model
""")
show_new_cars = st.checkbox("Include new cars from the dealers")


# In[49]:


show_new_cars


# In[50]:


if not show_new_cars:
    df = df[df.state!='new']


# In[51]:


model_choice = df['model'].unique()
man_made_choice = st.selectbox('select_model:', model_choice)


# In[52]:


man_made_choice


# In[53]:


#creating min and max year as limits sliders
min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

#creating slider
year_range = st.slider( 
    'choose_years',
     value = (min_year,max_year),min_value = min_year,max_value = max_year)


# In[54]:


year_range


# In[55]:


range(year_range[0],year_range[1]+1)


# In[56]:


#creating actual range base on the slider that will be used to filfter the dataset
actual_range=(range(year_range[0],year_range[1]+1))


# In[57]:


filtered_type = df[(df.model==man_made_choice) & (df.model_year.isin(actual_range))]

#showing  the finaltable in streamlit
st.table(filtered_type)


# Conclusions
# 
# In this chapter, i did data processing and all have been check. All duplicate have been check 
# and solutions haven apply to it also. Missing valus have been clear and treated. To go further, this
# data is cleared and ready to be use to work. One more column was added to the dataset
# which is State and st.hearder and st.selectbox was also introduce in this section.

# In[58]:


st.header('Analysis the days and date')
st.write(""""
###### let's analyse what influence days_listed and the date posted. We will check how distribution of days_listed varies
from the date posted by transmission,cylinders,type,state
""")

import plotly.express as px

#creating list of options to choose from
list_for_hist = ['transmission','cylinders','type','state']

choice_for_hist = st.selectbox('split for days_listed distribution', list_for_hist)

choice_for_hist = st.selectbox('split for date_posted distribution', list_for_hist)

#Plotly histogram
fig1 = px.histogram(df,x='days_listed',color=choice_for_hist)

fig1.update_layout(
title = "<b> Comparing the distribution days and date the cars were posted".format(list_for_hist))

st.plotly_chart(fig1)


# In[59]:


fig1.show()


# This histogram graph analyse what influence days_listed and the date posted in the market for sales. With the help of the filters, we can check how distribution of days_listed and date posted varies depending on transmission, cylinders, type, state.
# 
# In transmission, we have three sides and which is automatic,manual and other. In this stage we can see how the graph 
# move or change due to the distribution concren with the day listed or date posted. And also all colors apply to it also.
# 
# Here again we can see, automatic transmission was on high demand and followed by manual and then other.

# In[67]:


st.header('model production and model production analysis')
st.write(""""
###### let's analyse what influence model production and model year. we will check how distribution of model
production varies depending on condition,cylinder,model_year,state
""")

import plotly.express as px

#creating list of options to choose from
list_for_scatter = ['condition','odometer','model_year','state']

choice_for_scatter = st.selectbox('split for model_year production', list_for_scatter)

choice_for_scatter = st.selectbox('split for model production', list_for_scatter)

#Plotly histogram
fig2 = px.scatter(df, x = 'odometer', color = choice_for_scatter)

fig2.update_layout(
title = '<b> Comparing the model and year the cars were produced by {}</b>'. format(choice_for_scatter))

st.plotly_chart(fig2)


# In[68]:


fig2.show()


# Again this scatter graph, it introduce us to model production and year model analysis in the dataset.
# Which With the help of the filters, we can check how distribution of model production varies depending on condition,
# odometer, type, state and same applys to year model production.
# 
# Starting with condition in both production. In this stage we can see how the graph
# move or change due to the distribution concren with the production and also all colors apply to it also.
# 
# Here all the stages of the conditions where apply to it, which is on the right side bar and they are good,like new,fair,
# 
# execellent,salvage and lastly new. And it all change accordingly to the stage of the condition.

# In[62]:


st.header('Analysis type production and 4wd production')
st.write(""""
###### let's analyse what influence type production and 4wd production. we will check how distribution of how the two 
prodtction varies depending on type,fuel,is_4wd,condition
""")

import plotly.express as px

#creating list of options to choose from
list_for_bar = ['type','fuel','is_4wd','condition']

choice_for_bar = st.selectbox('split for type production', list_for_bar)

choice_for_bar = st.selectbox('split for is_4wd production', list_for_bar)


#Plotly histogram
fig3 = px.bar(df, x = 'condition', color = choice_for_bar)

fig3.update_layout(
title = '<b> Comparing type and 4wd cars production  by {}</b>'. format(choice_for_bar))

st.plotly_chart (fig3)


# In[63]:


fig3.show()


# This histogram graph, compare the type production and 4wd production in this work.
# 
# Starting with type in both production. In this stage we can see how the graph
# move or change due to the distribution concren with the production and also all colors apply to it also.
# 
# Here all the stages of the conditions where apply to it, which is on the right side bar and they are good,like bus,van,
# 
# hatchack,mini-van and offroad. And it all change accordingly to the stage of the condition.

# In[65]:


st.header('Comparing the use of fuel of the Product')
st.write(""""
###### let's analyse the use of fuel of the Product. we will check for the prodct that uses more fuel in working depending on 
transmission,cylinders,type,state
""")

import plotly.express as px

#creating list of options to choose from
list = ['transmission','cylinders','type','state']

choice = st.selectbox('split for fuel',list)


choice = st.selectbox('split for condition',list)


#Plotly histogram
fig4 = px.histogram(df,x='fuel',color=choice)

fig4.update_layout(
title = "<b>Comparing the use of fuel".format(list))

st.plotly_chart(fig4)


# In[66]:


fig4.show()


# This bar chart graph, Comparing the use of fuel of the Product in the dataset.
# Which With the help of the filters, we can check how distribution of fuel production varies
# depending on prodtuct.
# 
# Starting with transmission. In this stage we can see how the graph
# move or change due to the distribution concren with the type and the year of production and also all colors
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
