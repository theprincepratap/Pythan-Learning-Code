# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
sum = 0
for n in range(0,len(student_heights)):
    sum = sum + student_heights[n] 
average = sum/len(student_heights)
print(round(average))