# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:35:15 2021

@author: chris
"""
#%%

import numpy as np
import matplotlib.pyplot as plt

#%%

filename = "Scraping Result/tokopedia_bluetooth speaker light.txt"
f = open(filename,"r", encoding="utf-8")
lines1 = f.readlines()
f.close()

filename = "Scraping Result/tokopedia_bluetooth speaker lamp.txt"
f = open(filename,"r", encoding="utf-8")
lines2 = f.readlines()
f.close()

lines = []
lines.extend(lines1)
lines.extend(lines2)

# Removing Incomplete Data
del_index = []
for i in range(len(lines)):
    temp = lines[i].split("\t")
    if len(temp) != 5:
        del_index.append(i)

counter = 0
for i in range(len(del_index)):
    lines.pop(del_index[i]-counter)
    counter = counter + 1
    
print(f"Incomplete Data: {len(del_index)}")

# Removing Duplicate Products
del_index = []
for i in range(len(lines)-1):
    temp = lines[i].split("\t")
    name_i = temp[2]
    price_i = temp[3]
    sold_i = temp[4]
    for j in range(i+1,len(lines)):
        temp = lines[j].split("\t")
        name_j = temp[2]
        price_j = temp[3]
        sold_j = temp[4]
        if name_i == name_j and price_i == price_j and sold_i == sold_j:
            if j not in del_index:
                del_index.append(j)

counter = 0
for i in range(len(del_index)):
    lines.pop(del_index[i]-counter)
    counter = counter + 1
    
print(f"Duplicate Data: {len(del_index)}")

#%%

Price = np.zeros(len(lines)-1)
Sold = np.zeros(len(lines)-1)
Revenue = np.zeros(len(lines)-1)
Data = []

for i in range(len(lines)-1):
    temp = lines[i+1].split("\t")
    Price[i] = temp[4]
    Sold[i] = temp[3]
    Revenue[i] = Price[i]*Sold[i]
    Data.append(Price[i]*Sold[i])
    
# =============================================================================
#     for j in range(int(Sold[i])):
#         if Price[i] > 200000 and Price[i] < 600000:
#             Data.append(Revenue[i])
# =============================================================================

#%%
# =============================================================================
# plt.hist(Data,bins=100)
# =============================================================================
# =============================================================================
# plt.bar(Price,Sold)
# =============================================================================
Price, Sold = zip(*sorted(zip(Price, Sold)))
plt.plot(Price,Sold)
plt.xlabel("Product Pricing IDR")
plt.ylabel("Yearly Product Sales Units")
