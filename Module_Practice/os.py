import os 
print(os.getcwd())
#os.rmdir("Leetcode2")
k = open("t1.py","r")
os.chdir("Leetcode")
f = open("#1_hello", "a")
for line in k.read():
  f.writelines(line)
f.close()
k.close()