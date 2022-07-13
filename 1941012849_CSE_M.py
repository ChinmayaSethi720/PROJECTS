# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:46:44 2022

@author: chinm
"""
import csv
from matplotlib import pyplot as plt
from collections import Counter
import math
from typing import List
def bucketing(a:list,b:int,c:int)->list or int:
    si=(((max(a)-min(a))/30))   
    if(b==1):
        return si
    
    list1=[]
    list1.append(min(a))
    a1=min(a)
    for i in range(30):
        list1.append((a1+si))
        a1=(a1+si)
    if(c==1):
        list1.remove(list1[30])
    return list1
   
        
def bucketing1(a:list,b:list)->list:
    list2=[0 for i in range(30)]
    sorted(b)
    for i in range(0,30,1):
        for j in b:
            if j>=a[i] and j<a[i+1]:
                list2[i]+=1
   
    return list2
def mean(lst: list) -> float:
    return sum(lst) / len(lst)

def median(lst: list) -> float:
    sorted(lst)
    if len(lst) % 2 == 0:
        mid=len(lst)//2
        return (lst[mid - 1] +lst[mid]) / 2
    else:
        return lst[len(lst)//2]

def mode(x: list) -> list:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
    if count == max_count]

def dot(v: list, w: list) -> float:
    assert len(v) == len(w)
    return sum(vi * wi for vi, wi in zip(v, w))

def covariance(xs: list, ys: list) -> float:
    assert len(xs) == len(ys)
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def sum_of_squares(v: list) -> float:
    return dot(v, v)

def de_mean(xs: list) -> list:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: list) -> float:
    assert len(xs) >= 2
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(xs: list) -> float:
    return math.sqrt(variance(xs))

def correlation(xs: list, ys:list ) -> float:
    stdev_x= standard_deviation(xs)
    stdev_y= standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0

       
fixed_acidity=[];volatile_acidity=[];citric_acid=[];residual_sugar=[];chlorides=[];
free_sulfur_dioxide=[];total_sulfur_dioxide=[];density=[];pH=[];sulphates=[];alcohol=[];quality=[];
list1=[]

with open('winequality-white.csv') as csv_file:
    
    colonreader=csv.DictReader(csv_file,delimiter=';')
    for dict_row in colonreader:
        fixed_acidity.append(float(dict_row['fixed_acidity']))
        volatile_acidity.append(float(dict_row['volatile_acidity']))
        citric_acid.append(float(dict_row['citric_acid']))
        residual_sugar.append(float(dict_row['residual_sugar']))
        chlorides.append(float(dict_row['chlorides']))
        free_sulfur_dioxide.append(float(dict_row['free_sulfur_dioxide']))
        total_sulfur_dioxide.append(float(dict_row['total_sulfur_dioxide']))
        density.append(float(dict_row['density']))
        pH.append(float(dict_row['pH']))
        sulphates.append(float(dict_row['sulphates']))
        alcohol.append(float(dict_row['alcohol']))
        quality.append(float(dict_row['quality']))
list2=List[list]        
list2=[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,
       free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
list3=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides',
'free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']

j=0
for i in list2:
    plt.bar(bucketing(i,0,1),bucketing1(bucketing(i,0,0),i),
    bucketing(i,1,0),edgecolor=(0,0,0))
    plt.xlabel(list3[j])
    plt.ylabel("no. of samples")
    plt.title("Dist. of samples")
    plt.show()
    j+=1
   
print("TASK 2: Mean Median Mode\n-------------------------")
k=0 
for i in list2:
    print(list3[k],':')
    print('Mean:',mean(i),'\nMedian',median(i),'\nMode: ',mode(i),'\n')
    k+=1
    
print('TASK 3: COVARIANCE:\n------------------------------\n')   
list4=[]
for i in list2:
    list4.append(covariance(i,quality))
k=0
for i in list3:
    print(i,"=",list4[k])
    k+=1
print()

k=0
print("Attributes with same directionional relationship with output label")    
for i in list3:
    if(list4[k]>0):
        print(i,"=",list4[k])
    k+=1  
print()  

print('TASK 4-a: CORRELATION:\n---------------------------')
k=0
correlation_matrix=[]             #correlation-matrix
for i in list2:
    cor=[]
    for j in list2:
        cor.append(correlation(i, j))
    correlation_matrix.append(cor)   
    k+=1
    
for j in range(0, len(list3)):
    print('\n-----------Correlation of', list3[j],'-------------')
    print(correlation_matrix[j])
print()
    
print('TASK 4-b: CORRELATION: between attribute and output label\n-----------------------------------------------\n')    
k=0
list5=[]
for i in list2:
    list5.append(correlation(i,quality))
    print(list3[k],":",correlation(i,quality))
    k+=1
    
print('\nTASK 5-a: \n-----------------------------------------------\n') 
temp1=correlation_matrix[0][0]
value1=0
index1=0

#maximum similarity
for i in range(0, len(correlation_matrix)):
    for j in range(0, len(correlation_matrix[i])):
        if i==j:
            continue 
        if correlation_matrix[i][j]<temp1:
            temp1=correlation_matrix[i][j]
            value1=i
            index1=j
#maximum dis-similarity
temp2=min(correlation_matrix[0])  
value2=0
index2=0    
for i in range(0, len(correlation_matrix)):
    for j in range(0, len(correlation_matrix[i])):
        if i==j:
            continue
        elif correlation_matrix[i][j]>temp2:
            temp2=correlation_matrix[i][j]
            value2=i
            index2=j     
print('attributes with maximum similarity: ',list3[value1],'and',list3[index1])
print('attributes with maximum dis-similarity: ',list3[value2],'and',list3[index2])
            
print('\nTASK 5-b: \n-----------------------------------------------\n')         
index_max=list5.index(min(list5))
index_min=list5.index(max(list5))

print('attributes with maximum similarity: ',list3[index_min])
print('attributes with maximum dis-similarity: ',list3[index_max])    




second=0
check=0
for i in range(0, 11):
    diff=0    
    first=0
    count=0
    fig, axs = plt.subplots(5, 2)
    fig.suptitle(list3[i])
    for j in range(0,11):
        if i==j:
            continue     
        if(count-diff==2):
            first+=1
            diff=count
        #print(first, second, i,j)       
        if check==0:
            second=1
            check=1
        else:
            second=0
            check=0
        count+=1
        axs[first, second].scatter(list2[i],list2[j], marker='.')
       
        
