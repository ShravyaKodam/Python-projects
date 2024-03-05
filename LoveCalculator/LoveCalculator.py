print("Love calculator")
firstPerson=input("Enter the first person name: ")
secondPerson=input("Enter the second person name: ")
firstPersonName=firstPerson.lower()
secondPersonName=secondPerson.lower()
# combinedName= firstPersonName+secondPersonName
# lowerCaseCombinedName=combinedName.lower()
T=firstPersonName.count("t")+secondPersonName.count("t")
print(f"T occurs {T} times")
R=firstPersonName.count("r")+secondPersonName.count("r")
print(f"R occurs {R} times")
U=firstPersonName.count("u")+secondPersonName.count("u")
print(f"U occurs {U} times")
E=firstPersonName.count("e")+secondPersonName.count("e")
print(f"E occurs {E} times")

L=firstPersonName.count("l")+secondPersonName.count("l")
O=firstPersonName.count("o")+secondPersonName.count("o")
V=firstPersonName.count("v")+secondPersonName.count("v")
e=firstPersonName.count("e")+secondPersonName.count("e")
print(f"L occurs {L} times")
print(f"O occurs {O} times")
print(f"V occurs {V} times")
print(f"E occurs {e} times")

trueSum=str(T+R+U+E)
loveSum=str(L+O+V+E)

total=int(trueSum+loveSum)
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
