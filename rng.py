import random
cat = ""
fulllist = set()
while cat != "!end":
    print("Type in name please.Type !end to finish!" + str(len(fulllist)))
    cat = input()
    if cat != "!end":
        fulllist.add(cat)
# to see the whole list print(fulllist)
#print(len(fulllist))
memberlistlength = len(fulllist)
maximumteamsize = round(memberlistlength/2)
print(maximumteamsize)
teamone = []
teamtwo = []
while len(fulllist) != 0:
    person = fulllist.pop()
    if maximumteamsize == len(teamone):
        teamtwo.append(person)
    elif maximumteamsize == len(teamtwo):
        teamone.append(person)
    else :
        flip = random.randint(0,1)
        if flip == 0:
            teamone.append(person)
        else :
            teamtwo.append(person)
print("Team One is " + str(teamone))
print("Team Two is " + str(teamtwo))
#A Set is an unordered collection. {} or set() 