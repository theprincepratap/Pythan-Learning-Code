student_list = input("Enter a list of student scores : ").split(" ")
for n in range(0,len(student_list)):
    student_list[n]=int(student_list[n])
heighest_score =0
for h in student_list:
    if h > heighest_score:
        heighest_score = h 
print(f"The highest score in the class is: {heighest_score}")