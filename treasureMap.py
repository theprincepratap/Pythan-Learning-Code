# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_person = len(names)
random_person = random.randint(0,total_person)
pay_bill = names[random_person]
print(f"{pay_bill} is going to buy the meal today!")