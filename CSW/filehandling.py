f=open("f1.txt","r")
data=f.read()
print("Text file data:",data)
f.close()
f1=open("f1.txt","rb")
data1=f1.read()
print("Binary file data:",data1)
f1.close()

