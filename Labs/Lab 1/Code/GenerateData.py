import random
numberOfStudents=5494
def students_ID():
    for i in range(numberOfStudents):
        print(i+1000)
        
def student_PASSWORD():
     character= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?"
     passwordLength=8
     for i in range(numberOfStudents):
         password = "".join(random.sample(character,passwordLength))
         print(password)
         
def study_level():
    arr=['YOS3','HONOURS']
    for i in range(numberOfStudents):
        ind=random.randint(0,1)
        print(arr[ind])
