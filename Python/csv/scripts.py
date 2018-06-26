import os, csv

f=open("/path/to/csv/test.csv",'r+')
w=csv.writer(f)
for path, dirs, files in os.walk("/path/to/folder"):
    for filename in files:
        newname = filename.replace('.old-extension', '.new-extension')
        w.writerow([filename, newname])
