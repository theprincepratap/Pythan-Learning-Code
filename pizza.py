# 🚨 Don't change the code below 👇
bill = 0 
S=15
M=20
L=25
PS=2
PLM=3
EC=1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y":
    pepperoni = input("Pepperoni for small pizza or pepperoni for medium or large (type PSP or PML)  ")
    if pepperoni == "PSP":
        bill += PS 
    elif pepperoni == "PML":
        bill += PLM 
    else:
        print("Chosse one ")
else:
    print("That's ok ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "L":
    bill += L 
elif size == "M":
    bill += M 
elif bill == "S":
    bill +=  S 
else :
    print("Worng Order ")

if extra_cheese == "Y":
    bill += EC 
else:
    print("Thnaku ")

print("Total bill is ", bill)

