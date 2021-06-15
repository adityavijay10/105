# import csv
# from collections import Counter

# with open('./data.csv',newline='') as f:
#     reader=csv.reader(f)
#     file_data=list(reader)
    
# file_data.pop(0)
# new_data=[]
# for i in range(len(file_data)):
#     n_nun=file_data[i][1]
#     new_data.append(float(n_nun))

# n=len(new_data)
# total=0
# for x in new_data:
#     total+=x

# mean=total/n
# print('mean: ',str(mean))


import csv
import math

with open('./data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)


data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data :
        total+=int(x)
    mean=total/n
    print('mean ',str(mean))
    return(mean)


squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

sum =0
for i in squared_list:
    sum=sum+i

result=sum/(len(data)-1)

standardDeviation=math.sqrt(result)
print('standardDeviation',str(standardDeviation))
