password=input ()
l=len(password)
if l<8:
    print("invalid")
digit=False
upper=False
lower=False
for i in password:
    if i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i.isdigit():
        digit=True
if digit and upper and lower:
    print("valid password")
else:
    print("invalid password ")
