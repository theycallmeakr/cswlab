file=open("myfile.txt","w")
lines_to_write=[
"Hello, this is the first line.\n",
"This is the second line.\n",
"his is the thrd line.\n"
]
'''
file.writelines(lines_to_write)

with open("my_file.txt","r") as file:
    content=file.read()
    print(content)
    '''

f=open("myfile.txt","r")
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(4))
print(f.seekable())
f.seek(8)
print(f.read())

with open('sample.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.seek(0)
    f.write("Python is awesome!\n")