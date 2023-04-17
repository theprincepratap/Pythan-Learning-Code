hisName = input("Enter Your name : ")
herName = input("Enter Her Name : ")
combined_string = hisName + herName
lowerCase_string = combined_string.lower()

t = lowerCase_string.count("t")
r = lowerCase_string.count("r")
u = lowerCase_string.count("u")
e = lowerCase_string.count("e")

true = t + r + u + e 

l = lowerCase_string.count("l")
o = lowerCase_string.count("o")
v = lowerCase_string.count("v")
e = lowerCase_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
print(love_score)


