import os

os.chdir(r"C:\Users\tan\Documents\python learning")
a = open("output.txt", "w")
for path, subdirs, files in os.walk(r'C:\Users\tan\Documents\python learning'):
   for filename in files:
     f = os.path.join(path, filename)
     a.write(str(f) + os.linesep)
     print file.readline()
a.close()
