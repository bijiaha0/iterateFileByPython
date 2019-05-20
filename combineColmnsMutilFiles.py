import csv
import os
import pandas as pd
import string
def operation(filename1,filename2,filename3,filename4):
    os.chdir(filename1)
    data1=pd.read_table(filename2,decimal=' ',header=0)
    # print(data1.index)
    # print(data1.columns)
    # print(data1.values)
    # 遍历所有的文件名字到file_names
    file_names = []

    f = open(filename1 + filename)
    iter_f = iter(f)
    lines = 0
    for line in iter_f:
        lines += 1

    for i in range(lines-1):
        file_names.append(data1['fileName'][i])
    print(file_names)
    os.chdir(filename3)
    # Output list of generator objects
    o_data = []

    # Open files in the succession and
    # store the file_name as the first
    # element followed by the elements of
    # the third column.
    ii =0
    for afile in file_names:
        if os.path.exists(afile):
            file_h = open(afile)
            a_list = []
            a_list.append(data1['sampleID'][ii])
            csv_reader = csv.reader(file_h, delimiter=' ')
            for row in csv_reader:
                temp = row[0].split('\t')[1]
                num = round(float(temp), 6)
                a_list.append(str(num))
            # Convert the list to a generator object
            o_data.append((n for n in a_list))
            file_h.close()
        ii = ii + 1
    print(o_data)
    # Use zip and csv writer to iterate
    # through the generator objects and
    # write out to the output file

    os.chdir('/Users/BJH/Desktop/combineColumnsFiles/')
    with open(filename4, 'w') as op_file:
        csv_writer = csv.writer(op_file, delimiter=' ')
        for row in list(zip(*o_data)):
            csv_writer.writerow(row)
    op_file.close()

root = "/Users/BJH/Desktop/FILE_SAMPLEID_MAP/EXP/"

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if str(filename).__contains__("txt"):
            print(filename)
            filenametemp1 = "/Users/BJH/Desktop/desData/data/expData/"
            filenametemp2 = "/CNS/"
            operation("/Users/BJH/Desktop/FILE_SAMPLEID_MAP/EXP/",filename,filenametemp1+str(filename[:-6])+filenametemp2,filename)