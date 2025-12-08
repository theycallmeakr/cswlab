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
    f.write("Python is awesome!\n")'''




'''
def filter_emails(lst):
    valid = []
    for email in lst:
        if email.count('@') != 1:
            continue
        username, domain_part = email.split('@')
        if not username:
            continue
        if not(username[0].isalnum()):  
            continue
        for ch in username:
            if not (ch.isalnum() or ch in ['.', '_']):
                break
        else:
            if domain_part.count('.') != 1:
                continue

            domain, tld = domain_part.split('.')
            if not domain.isalpha():
                continue

            if not (2 <= len(tld) <= 4 and tld.isalpha()):
                continue

            valid.append(email)

    return valid


emails = ["student123@gmail.com", "teacher.name@soa.edu", "abc.xyz@abc.in",
          "xyz#12@abc.com", "bad@1n.com"]

print(filter_emails(emails))


'''

'''
import re

def verify_passwd(s):
    rule1 = re.match(r'.{8,}$', s)
    rule2 = re.match(r'^[A-Za-z0-9@#$%^&*!]+$', s)
    rule3 = re.search(r'[0-9]', s)
    rule4 = re.search(r'[A-Za-z]', s)
    rule5 = re.search(r'[@#$%^&*!]', s)

    return bool(rule1 and rule2 and rule3 and rule4 and rule5)
passwords = [
    "abc123!!",
    "pass1234",
    "PASSWORD@1",
    "short1!",
    "Valid@123",
    "NoSpecial123",
    "NoDigit!!!",
]
verify_passwd("Test@123")
for p in passwords:
    print(p, "-", verify_passwd(p))


'''


'''
import re

def normalize_phones(s):
    pattern = r'(?:\+91-|\(91\)\s*|0091\s*|91\s*)(\d[\d\s]{9})'

    def repl(m):
        digits = re.sub(r'\s+', '', m.group(1))
        return "+91-" + digits

    return re.sub(pattern, repl, s)


text = "Contact: +91-9876543210, Office: (91) 98765 43210, Home: 0091 9876543210"
print(normalize_phones(text))

'''
#q4

import re

s = "1 set of 23 owls, 999 doves."
m = re.search(r'\d{2,}', s)

print(f'"{m.group()}" found at {m.span()}')