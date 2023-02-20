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

# In[132]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# In[133]:


df = pd.read_csv("vehicles_us.csv",sep =',')


# In[134]:


df.head(10)


# Conclusions
# 
# Data on user behavior is stored in the file 'vehicles_us.csv.' There is no information about
# the quality of the data and all is loader n working fine.

# In[135]:


#extracting the names of the manufacturer
split = df['model'].str.split(pat=' ', n=1, expand=True)


# In[136]:


df.paint_color.fillna(value = 'no_info', inplace = True)


# In[137]:


df['state'] = 'owned'
df.head()


# In[138]:


df.is_4wd.fillna(0, inplace=True)


# In[139]:


df.head()


# In[140]:


df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median'),inplace = True)


# In[141]:


df.head()


# In[142]:


df['odometer'].fillna(df.groupby(['model_year'])['odometer'].transform('mean'),inplace = True)
df.head()


# In[143]:


df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform('median'),inplace = True)
df.head()


# In[144]:


# Removing duplicate 
df.drop_duplicates()


# In[145]:


df. describe()


# In[146]:


df.head()


# In[147]:


st.header('market of used of cars. Original data')
st.write(""""
#### Filter the data below to see ads by model
""")
show_new_cars = st.checkbox("Include new cars from the dealers")


# In[148]:


show_new_cars


# In[149]:


if not show_new_cars:
    df = df[df.state!='new']


# In[150]:


model_choice = df['model'].unique()
man_made_choice = st.selectbox('select_model:', model_choice)


# In[151]:


man_made_choice


# In[152]:


#creating min and max year as limits sliders
min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

#creating slider
year_range = st.slider( 
    'choose_years',
     value = (min_year,max_year),min_value = min_year,max_value = max_year)


# In[153]:


year_range


# In[154]:


range(year_range[0],year_range[1]+1)


# In[155]:


#creating actual range base on the slider that will be used to filfter the dataset
actual_range=(range(year_range[0],year_range[1]+1))


# In[156]:


filtered_type = df[(df.model==man_made_choice) & (df.model_year.isin(actual_range))]

#showing  the finaltable in streamlit
st.table(filtered_type)


# In[157]:


df['manufacturer'] = split[0]
df['model_name'] = split[1]
df.drop('model', axis=1, inplace=True)
df.head(10)


# In[158]:


st.header('Compare days listed between manufacturers')
list_for_hist = df['manufacturer'].unique()
selection1 = st.selectbox('manufacturer 1', list_for_hist )
selection2 = st.selectbox('manufacturer 2', list_for_hist )
df_filtered = df[(df['manufacturer'] == selection1) | (df['manufacturer'] == selection2)]
fig = px.histogram(df_filtered , x='days_listed', color = 'manufacturer')

# display the figure with streamlit
st.write(fig)


# Conclusions
# 
# In this chapter, i did data processing and all have been check. All duplicate have been check 
# and solutions haven apply to it also. Missing valus have been clear and treated. To go further, this
# data is cleared and ready to be use to work. One more column was added to the dataset
# which is State and st.hearder and st.selectbox was also introduce in this section.

# In[159]:


st.header('manufacturer production and model production analysis')
st.write(""""
###### let's analyse what influence manufacturer production and model year. we will check how distribution of model
production varies depending on model,condition,cylinder,model_year,state
""")

import plotly.express as px

#creating list of options to choose from
list_for_scatter = ['manufacturer','cylinder','model_year','state']

choice_for_scatter = st.selectbox('split for model_year production', list_for_scatter)

choice_for_scatter = st.selectbox('split for manufacturer production', list_for_scatter)

#Plotly histogram
fig2 = px.scatter(df, x = 'odometer', color = choice_for_scatter)

fig2.update_layout(
title = '<b> Comparing the model and year the cars were produced by {}</b>'. format(choice_for_scatter))

st.plotly_chart(fig2)


# In[160]:


fig2.show()


# Again this scatter graph, it introduce us to model production and year model analysis in the dataset.
# Which With the help of the filters, we can check how distribution of model production varies depending on condition,
# odometer, type, state and same applys to year model production.
# 
# Starting with condition in both production. In this stage we can see how the graph
# move or change due to the distribution concren with the production and also all colors apply to it also.
# 
# Here all the stages of the conditions where apply to it, we have all the model cars at the side of the graph And it all change accordingly to the stage of the condition.

# In[161]:


st.header('Analysis type production and 4wd production')
st.write(""""
###### let's analyse what influence type production and 4wd production. we will check how distribution of how the two 
prodtction varies depending on manufacturer,type,fuel,is_4wd,condition
""")

import plotly.express as px

#creating list of options to choose from
list_for_bar = ['manufacturer','type','fuel','is_4wd','condition']

choice_for_bar = st.selectbox('split for type production', list_for_bar)

choice_for_bar = st.selectbox('split for is_4wd production', list_for_bar)


#Plotly histogram
fig3 = px.bar(df, x = 'condition', color = choice_for_bar)

fig3.update_layout(
title = '<b> Comparing type and 4wd cars production  by {}</b>'. format(choice_for_bar))

st.plotly_chart (fig3)


# In[162]:


fig3.show()


# This histogram graph, compare the type production and 4wd production in this work.
# 
# Starting with type in both production. In this stage we can see how the graph
# move or change due to the distribution concren with the production and also all colors apply to it also.
# 
# Here all the stages of the conditions where apply to it, we have all the model cars at the side of the graph. And it all change accordingly to the stage of the condition.

# In[163]:


st.header('Comparing the use of fuel of the Product')
st.write(""""
###### let's analyse the use of fuel of the Product. we will check for the prodct that uses more fuel in working depending on 
model,transmission,cylinders,type
""")

import plotly.express as px

#creating list of options to choose from
list = ['manufacturer','transmission','cylinders','type']

choice = st.selectbox('split for fuel',list)


choice = st.selectbox('split for condition',list)


#Plotly histogram
fig4 = px.histogram(df,x='fuel',color=choice)

fig4.update_layout(
title = "<b>Comparing the use of fuel".format(list))

st.plotly_chart(fig4)


# In[164]:


fig4.show()


# In[165]:


# Plot a histogram of the numerical columns
df.hist(bins=30, figsize=(10,15))


# In[166]:


# histogram of the price column
px.histogram(df, x='price', nbins=50)


# In[167]:


#scatterplot of price vs odometer
px.scatter(df, x='odometer', y='price', color='fuel')


# In[168]:


#histogram of the cylinders column
px.histogram(df, x='cylinders', nbins=8)


# In[169]:


#scatterplot of price vs model_year
px.scatter(df, x='model_year', y='price', color='fuel')


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

# In[ ]:





# In[ ]:





# In[ ]:



