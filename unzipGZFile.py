import gzip
import shutil
import os
# 解压
for subdir, dirs, files in os.walk('/Users/student/Desktop/temp'):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        with gzip.open(filepath, 'rb') as f_in:
            with open(filepath.split('.gz')[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

for subdir, dirs, files in os.walk('/Users/student/Desktop/temp'):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith("FPKM.txt"):
            shutil.move(filepath, '/Users/student/Desktop/tempTXT')
            # shutil.copy2(filepath, '/Users/student/Desktop/tempTXT')  # target filename is /dst/dir/file.ext
