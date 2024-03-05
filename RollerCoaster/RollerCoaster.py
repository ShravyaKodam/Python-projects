print("Rollercoaster")
height=int(input("enter height:"))
age=int(input("enter age: "))
bill=0
if height>120:
    if age<12:
        print("Can ride and pay $5")
        bill=5
    elif age<=18:
        print("can ride and pay $7")
        bill=7
    elif age>=45 and age<=55:
        print("free ride")
    else:
        print("pay $12")
        bill=5
else:
    print("cant ride")
want_photo=input("Yes or no? ")
if want_photo=="Yes".lower():
    bill=bill+3
print(f"Total bill is {bill}")
