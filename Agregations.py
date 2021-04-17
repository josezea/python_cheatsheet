# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:58:42 2021

@author: Stats
"""

import numpy as np
import pandas as pd


data = {'house':['A', 'B', 'A', 'A', 'B', 'B', 'B'], 'var1':[3, 0, 1, 3,4,5,3], 
       'var2':[2, 0, 5, 1,4,1,3],'var3':[4, 2, 3, 3,0,5,1]}
df = pd.DataFrame(data) 
df


# Calcular la suma y el promedio de la variable 1 


(df.groupby(['house']).agg({'var1': np.mean , 'var2': 'sum',}))


# Desviación estándar 
np.std(np.array([3,4,6,7,8]), ddof = 1)


# Calcular el promedio y el coeficiente de variación estándar de la variable 1

def CV(x):
    cv=100*np.std(x, ddof = 1) / np.mean(x)
    return cv

(df.groupby(['house']).agg({'var1': np.mean, 'var2': CV})) # Puede usarse una función


df.groupby(['house']).agg({'var1': np.mean, 'var2': lambda x: 100 * np.std(x, ddof = 1) / np.mean(x)}) # Puede usarse una expresión lambda



# Calcular el promedio y el coeficiente de variación para la variable uno y colocarle nombres
consulta = df.groupby(['house']).agg({'var1': np.mean, 'var2': lambda x: 100 * np.std(x, ddof = 1) / np.mean(x)}) # Puede usarse una expresión lambda
consulta =  consulta.reset_index().rename(columns={"var1": "prom_var1", "var2": "prom_cv_var2"})
consulta                                     

 


# Calcular el promedio y el coeficiente de variación de la variable 1,
# El conteo y la suma de la variable dos
# Calcular los valores mayores a 3 de la variable 3, y  calcular los cuartiles de la variable 3
# lambda x: 100 * np.std(x, ddof = 1) / np.mean(x)
consulta2 = df.groupby('house').agg({'var1':[np.mean,  lambda x: 100 * np.std(x, ddof = 1) / np.mean(x)],
                         'var2':[np.mean, 'size'],
                         'var3':[lambda x: np.sum(x > 3), np.min, lambda x: np.quantile(x, 0.25), 
                                 lambda x: np.quantile(x, 0.5), 
                                 lambda x: np.quantile(x, 0.75), np.max]})# size es un método

consulta2.columns

consulta2.columns = ['prom1', 'cv1', 'prom2', 'n2', 'mayores3_v3', 'min3', 'p25_3', 'p50_3', 'p75_3', 'max3']
consulta2 = consulta2.reset_index()  
consulta2

