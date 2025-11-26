# f=open("f1.txt","r")
# data=f.read()
# print("Text file data:",data)
# f.close()
# f1=open("f1.txt","rb")
# data1=f1.read()
# print("Binary file data:",data1)
# f1.close()
'''
f=open("f1.txt","r")
# data=f.read()
# data=f.read(7)
data=f.readline()
print("Text file data:",data)
data1=f.readline()
print("Text file data:",data1)
f.close()'''

#create a new file sample .txt write the following content(we are learning file i/o using java \n i like programng in java )  replace all occurances of java with python and seacrch if the word learning exist in the file or not  )
open("sample.txt", "w").write("we are learning file i/o\nusing java\ni like prgraming in java")

text = open("sample.txt").read().replace("java", "python")

open("sample.txt", "w").write(text)

print("learning exists" if "learning" in text else "not exists")

#q2)wap to find no of words , characters and lines in a file
f = open("sample.txt", "r")
lines = f.readlines()
word_count = 0
char_count = 0
for line in lines:
    word_count += len(line.split())
    char_count += len(line)

print("Number of lines:", len(lines))
print("Number of words:", word_count)
print("Number of characters:", char_count)
f.close()       