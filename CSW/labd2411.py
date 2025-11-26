import re
txt="hello world"
print(txt)
# x = re.findall("he...lo", txt)
# y = re.findall("^he", txt)
y = re.findall("world$", txt)
print(y)
if y:
    print("yes, there is a match")
else:
    print("no match")

# import re

# pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

# s = input('Enter tel. number: ')
# if re.match(pattern, s):
#     print('Number accepted.')
# else:
#     print('Incorrect format.')


#q2
import re

pin = input("Enter PIN code: ")

pattern = r'^[1-9][0-9]{5}$'

if re.match(pattern, pin):
    print("Valid PIN code")
else:
    print("Invalid PIN code")
#q1
import re

s = input("Enter a string: ")


result = re.findall(r'^[A-Za-z$]', s)

if result:
    print("Valid: First character is alphabet or $")
else:
    print("Invalid: First character is NOT alphabet or $")
