# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:56:31 2020

@author: turkm
"""

import numpy as np

#Numpy n boyutlu dizilerde işlem için
#Döngü kullanmadan numerical işlemler yapmak
np.__version__

#Bir boyutlu 4 elamanlı dizi
data1B = np.array([1,2,3,4])
print(data1B)
print("Matris Boyutu",np.ndim(data1B))
print("------------------------------")

#ilk köşeli parantez matris boyutu ikincisi satırlar
#İki boyutlu 8 elamanlı dizi
data2B = np.array([[1,2,3,4],[5,6,7,8]])
print(data2B)
print("Matris Boyutu",np.ndim(data2B))
print("------------------------------")

#matris satır sutun belirleme
#shapeSize = np.shape((4,3))
#print(shapeSize())

# 4 * 3 lük bir matirisi
birMatrix= np.ones((4,3))
print(birMatrix)
print("------------------------------")

# 4 * 3 lük sıfır matirisi
sifirMatrix = np.zeros((4,3))
print(sifirMatrix)
print("------------------------------")

#sabit değerli matrix
sabit = np.full(((4,3)),7)
print(sabit)
print("------------------------------")

#Birim matris
birim = np.eye(3)
print(birim)
print("------------------------------")

emt = np.empty((4,4),dtype=int)
print(emt.dtype)

#tüm satır ve sutunları
emt[:,:]
#2 satırdan itibarentüm sutunlar
emt[2:,:]
#son satır ilk sutunlar
emt[3:,0:]
print("------------------------------")

#artışmkarı
aralik = np.arange(1,11,2)
print(aralik)
print("------------------------------")

#Belirli bi aralıkta belirli bir sayı üretme
d =np.linspace(1, 10)
print(d)

print("------------------------------")


oneMatrix = np.array([[1,2,3,4]])
twoMatrix= np.array([[5,6,7,8]])

print(oneMatrix + twoMatrix)
print(oneMatrix - twoMatrix)
print(oneMatrix * twoMatrix)
print(oneMatrix / twoMatrix)

carpim = oneMatrix.dot(2)
print(carpim)
print("------------------------------")
threeMatris=np.array([[1,2,3],[4,5,6],[7,8,9]])
satirToplam = threeMatris.sum(axis=0)
print(satirToplam)
print("------------------------------")
sutunToplam = threeMatris.sum(axis=1)
print(sutunToplam)
