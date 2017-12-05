import re

patterns=['term1','term2']
text="this is a string with term1, not the other"

for pattern in patterns:
    print("Iam searching for ",pattern)
    if re.search(pattern,text):
        print("match!")
    else:
        print("unmatch!")