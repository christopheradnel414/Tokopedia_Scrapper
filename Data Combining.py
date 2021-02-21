# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:35:15 2021

@author: chris
"""

filename = "Scraping Result/tokopedia_bluetooth speaker light.txt"
f = open(filename,"r", encoding="utf-8")
lines1 = f.readlines()
f.close()

filename = "Scraping Result/tokopedia_bluetooth speaker lamp.txt"
f = open(filename,"r", encoding="utf-8")
lines2 = f.readlines()
f.close()

# =============================================================================
# filename = "Scraping Result/tokopedia_night lamp.txt"
# f = open(filename,"r", encoding="utf-8")
# lines3 = f.readlines()
# f.close()
# 
# filename = "Scraping Result/tokopedia_night light.txt"
# f = open(filename,"r", encoding="utf-8")
# lines4 = f.readlines()
# f.close()
# =============================================================================

lines = []
lines1.pop(0)
lines2.pop(0)
lines.extend(lines1)
lines.extend(lines2)
# =============================================================================
# lines.extend(lines3)
# lines.extend(lines4)
# =============================================================================

filename = "Processed Result/combined result.txt"
f = open(filename,"w", encoding="utf-8")

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
    tempi = lines[i].split("\t")
    name_i = tempi[2]
    price_i = int(tempi[3])
    sold_i = int(tempi[4])

    for j in range(i+1,len(lines)):
        tempj = lines[j].split("\t")
        name_j = tempj[2]
        price_j = int(tempj[3])
        sold_j = int(tempj[4])
        if price_i == price_j and sold_i == sold_j:
            if j not in del_index:
                del_index.append(j)

counter = 0
for i in range(len(del_index)):
    lines.pop(del_index[i]-counter)
    counter = counter + 1

# =============================================================================
# lines = list(dict.fromkeys(lines))
#     
# print(f"Duplicate Data: {len(del_index)}")
# 
# for i in range(len(lines)):
#     f.write(lines[i])
# f.close()
# =============================================================================

#%%

import numpy as np

Price = np.zeros(len(lines)-1)
Sold = np.zeros(len(lines)-1)
Revenue = np.zeros(len(lines)-1)

for i in range(len(lines)-1):
    temp = lines[i+1].split("\t")
    Price[i] = temp[4]
    Sold[i] = temp[3]
    Revenue[i] = Price[i]*Sold[i]

Revenue, Price, Sold = zip(*sorted(zip(Revenue, Price, Sold)))
