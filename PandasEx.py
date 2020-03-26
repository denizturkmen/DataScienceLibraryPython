# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:25:17 2020

@author: turkm
"""

import numpy as np
import pandas as pd

dataframe = pd.read_csv("googleplaystore.csv")
#dosyanın satır ve sutunu sayısını öğrenme
print(dataframe.shape)

#sutunların veri tiplerini 
print(dataframe.columns)

#typleri öğrenmek
print(dataframe.dtypes)

#dataframe ilk 5 satırı head ve son 5 satırı tail
print(dataframe.head())
print(dataframe.tail())
print(dataframe.head(12))

#dataframe hakkında genel bilgi eksik sutun bilgileri null belirlemek için
dataframe.info()
print()

#dataframe eksik bilgilerin sayısını öğrenmek
print(dataframe.isnull().sum().sort_values(ascending=False))
print()

#Sutunların istatiksel oranları saısal verilerin olani verir ama string alanı
#da yapailirsin describe["alan_ismi].describe()
print(dataframe.describe())
print()
print(dataframe["Category"].describe())
print()

#Sayisal olmayan tüm sutunların bilgisi için
print(dataframe.describe(include=['O']))
print()

# Her bir değerin sutunda bulunma sayisi
print(dataframe["Category"].value_counts())
print()
print(dataframe[dataframe["Category"]=="1.9"])
