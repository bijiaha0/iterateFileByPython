import os
import shutil
# 将原始文件中以FPKM.txt.gz结尾的文件，全部拖到temp文件下
for subdir, dirs, files in os.walk('/Users/student/Desktop/data/expData/acc'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith("FPKM.txt.gz"):
            shutil.copy2(filepath, '/Users/student/Desktop/temp')
