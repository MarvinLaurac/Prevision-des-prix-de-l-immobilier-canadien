#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource, HoverTool

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

from bokeh.plotting import figure
from bokeh.io import  push_notebook,output_notebook, show
output_notebook() 


# In[65]:


#je commence par importer le DataFrame
df = pd.read_csv('/Users/octoberone/Desktop/DataFrame GitHub/DataFrame/Prévision des prix de immobilier canadien.csv', encoding='ISO-8859-1')


# In[66]:


#affichage des 5 premières lignes
df.head()


# In[67]:


#voici le nombre de lignes et de colonnes sans le détail
df.shape


# In[68]:


#voici les détails des colonnes avec beaucoup plus d'informations (variables, types, le nombre de valeurs nulles)

df.info()


# In[69]:


#j'ai utilisé cette commande pour être sûr qu'il n'y a pas de valeurs manquantes
df.isnull().sum()
#par conséquent, j'en déduis que ce DataFrame est plutôt agréable à utiliser dans un premier temps


# In[70]:


#Afin d'avoir plus de détails statistiques, j'affiche les colonnes numériques

#count%:nombre de valeurs nulles
#mean%:la moyenne des valeurs
#std%:l'écart type (dispersion valeurs)
#min%:le min de la colonne 
#25%:1er quatile à moins de 25
#50%:2er quatile à moins de 25
#75%:3er quatile à moins de 25
#max:le maxi de la colonne 

print(df.describe())


# In[80]:


#je commence par ce premier affichage
#je regroupe les provinces dans la variable province 
#Ppuis grâce à une visualisation interactive, j'affiche le prix des villes regroupées dans les provinces
#pa visualisation n'est la plus agréable par rapport aux données variées et volumineuses du DataFrame
#mais je trouve intéressant de réaliser cet affichage interactif

plt.figure(figsize=(10,15))
unique_provinces = list(set(df['Province']))
source = ColumnDataSource(data=df)
 
hover = HoverTool(
        tooltips=[
            ("City", "@City"),
            ("Price", "@Price")])

p = figure(width=950, height = 400, title ="Prévision des prix de l'immobilier canadien", 
           x_axis_label = "Province",
           y_axis_label = "Paliers de prix",
           x_range = unique_provinces)
p.circle(x="Province", y="Price", source = source, size = 5, color ="navy", alpha = 0.5)
p.add_tools(hover)


show(p)


# In[58]:


#dans cette histogramme plutot classic verticale
#je peux observer une tendance plus sinificative sur le prix de l'immobiler en fonction des ville au canada 
top_city = df.sort_values(by="Price", ascending=False)

plt.figure(figsize=(10,15))

plt.barh(top_city["City"], top_city["Price"], label="Prix (price)", color= "g") 
plt.title("Affichage des prix croissant de l’immobilier au Canada")
plt.xlabel("Prix de l'immobiler")
plt.ylabel("Ville")
plt.legend(title="Légende")

plt.show()


# In[62]:


top_city = df.sort_values(by='Price', ascending=False).head(13)


plt.figure(figsize=(10,5))
plt.barh(top_city['City'], top_city['Price'], label="Price") 
plt.legend()
plt.title('Top des prix de l’immobilier au Canada')
plt.show()

