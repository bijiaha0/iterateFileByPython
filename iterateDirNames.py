import os
root = "/Users/BJH/Desktop/FILE_SAMPLEID_MAP/EXP/"

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if str(filename).__contains__("txt"):
            # print(filename[:-6])
            f = open(dirpath+filename)
            iter_f = iter(f)
            lines = 0
            for line in iter_f:
                lines+=1

            print(lines)


