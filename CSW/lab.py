'''print("hello world")
i=1
for i in range(0,5):
     print("Hello")
   '''
'''                 
a=1200
print(type(a))
print("iterview\nyoyo")
b=232
x=123
print(2)
name="ayush"
b,n,m='iter',234,789
print(name)
print(b,n,m)    
print(type(b))
h=1
y=float(h)
print(y)
print(type(y))
k=int(y)
print(k)
print(type(k))

#function
def ak(a,k):
 
 print(a)
 print(k)
ak(a,k)#function called 

print(a==b)
print(bool(-2))

print(a%232)
j=100
print(j==0|k==0)

'''
'''#Q2
name = "ayush"
email="ayush@apple.com"
print(name)
print(email)
#Q1
a=12
b=45
c=a+b
d=a-b
e=a*b
f=a**b
g=a/b
h=a%b
i=a//b
print(c,d,e,f,g,h,i)

a,b=b,a'''
'''
a=5
b=6
c=8

if a>b and b>c:
    print("a is greater")
elif a<b and b>c:
    print("b is greater")
else:
    print("c is greater")


#print("b is greater") if a>b else  print("a is greater")

qty= int(input("enter no"))
price= int(input("enter no"))
print(qty)
if qty>1000:
      dis=10
else:
      dis=0
total = qty*price-dis*qty*price/100


sum=qty+5
print(sum)

'''


'''
salary=input("enter salary :")
print("first salary =",salary)
if salary<=1500:
    hra=0
    da=
else:
    hra=0.10*salary
    da=0.90*salary

gross=salary+hra+da  
'''
'''day=5
match day:
    case 1|2|3|4|5:
        print("monday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("enter the no between 1 to 7 bitch")'''


'''a = 12
b = 45

op=int(input("enter operation 1 to 7"))
match op:
    case 1:
        c = a + b
        print("Add:", c)
    case 2:
        d = a - b
        print("Sub:", d)
    case 3:
        e = a * b
        print("Multiply:", e)
    case 4:
        f = a ** b
        print("Power:", f)
    case 5:
        g = a / b
        print("Div:", g)
    case 6:
        h = a % b
        print("Mod:", h)
    case 7:
        i = a // b
        print("Floor Division:", i)
'''
'''a=3
i=10
while(i>0):
    i=i-1
    a=a+a
    print(a)
    if i==2:
        continue
'''

'''for i in range(1,20,2):
    print(i)
a=0  
while a>20:
    a=a+2           
    print(a)   
'''
s = "bbsr-751030"
alp = 0
dig = 0

for i in s:
    if i.isalpha():
        alp += 1
    elif i.isdigit():
        dig += 1

print("Alphabets:", alp)
print("Digits:", dig)

