import os
cwd=os.getcwd
cat = ""
while cat != "ling":
    print("enter a key?")
    cat = input()
    print(cat)
exec(open(cwd+"\ling2.py").read())
