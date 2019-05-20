import os
import pandas as pd
# os.chdir('/Users/student/Desktop/')
# data1=pd.read_table('textN.txt',decimal=' ',header=0)
# sampleID = []
# for i in range(72):
#     sampleID.append(data1['sampleID'][i])
os.chdir('/Users/student/Desktop/tempTXT')
data1=pd.read_table('output.txt',decimal=' ',header=0)
# print(data1.index)
# print(data1.columns[0].split(' '))
# print(type(data1.columns[0]))
index=[]
columns=data1.columns[0].split(' ')

for i in range(60483):
    index.append(data1.index[i])
# print(index)

# for i in range(60483):
#     for ii in range(72):
print(data1['TCGA-B0-5701-11A-01R-1541-07'])