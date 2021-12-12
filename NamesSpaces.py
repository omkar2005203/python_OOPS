class Student:
    # class vars/static vars
    x=10

# this modification in class name space
print('in class name space')
print(Student.x)
Student.x+=1
print(Student.x)

# veiw in instance space
print('in instance name space')
s1=Student()
s2=Student()
print(s1.x)
print(s2.x)

# trying to modify in instance name space
print('modification in instance name space')
print(s1.x+2)
print(s2.x)
