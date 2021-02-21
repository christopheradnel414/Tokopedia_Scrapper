# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:35:15 2021

@author: chris
"""
keyword = "gtx 1660 super"

filename = "Scraping Result/tokopedia_" + keyword +".txt"
f = open(filename,"r", encoding="utf-8")
lines = f.readlines()
f.close()

filename = "Processed Result/tokopedia_" + keyword +".txt"
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

for i in range(len(lines)):
    f.write(lines[i])
f.close()
