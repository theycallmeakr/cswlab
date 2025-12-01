# f=open('sample',"w+")
# print(f.read())
# f.write("writing in r+ mode")
# print(f.read())
# f.close()


# f=open("sample","a")
# f.write("\nappending new line")
# f.close()

# f=open("sample","a+")
# print(f.read())
# f.write("\nappending new line") 
# f.seek(0)
# print(f.read())
# f.close()

f=open("sample","x")
f.write("creating file using x mode")
f.close()

f=open("sample","x+")
print(f.read())
f.write("creating file using x+ mode")
f.seek(0)
print(f.read())
f.close()