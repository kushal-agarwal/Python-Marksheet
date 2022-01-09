
rollno=int(input("enter your roll no.:"))
name=(input("enter your name: "))
standard=int(input("enter class: "))
english=int(input("enter english marks: "))
physics=int(input("enter physics marks: "))
chemistry=int(input("enter chemistry marks: "))
computerscience=int(input("enter computer science marks: "))
maths=int(input("enter maths marks: "))
obtained_marks=english+physics+chemistry+computerscience+maths
print(obtained_marks)
percentage=obtained_marks/500*100
print(percentage)

print("--------------------STUDENTS MARKSHEET---------------------")
print("YOUR ROLL NO. IS: "+str(rollno))
print("YOUR NAME IS: "+name)
print("YOUR CLASS IS: "+str(standard))
print("TOTAL MARKS ARE: 500")
print("OBTAINED MARKS ARE: "+str(obtained_marks))
print("YOUR PERCENTAGE IS: "+str(percentage))

if percentage>=80:
    print("GRADE: A1")
    print("REMARKS: EXCELLENT")
elif percentage>=70:
    print("GRADE: A")
    print("REMARKS: VERY GOOOD")
elif percentage>=60:
    print("GRADE: B")
    print("REMARKS: GOOOD")
elif percentage>=50:
    print("GRADE: C")
    print("REMARKS: FAIR")
elif percentage>=40:
    print("GRADE: D")
    print("REMARKS: POOR")
elif percentage>=33:
    print("GRADE: E")
    print("REMARKS: NEEDS IMPROVEMENT")
else:
    print("GRADE: FAIL...")
    print("REMARKS: AUR KHELO FREE FIRE")
i=0
subjects_name=""
if english<33:
    i+=1
    subjects_name+= "ENGLISH, "
if physics<33:
    i+=1
    subjects_name+= "PHYSICS, "
if chemistry<33:
    i+=1
    subjects_name+= "CHEMISTRY, "
if computerscience<33:
    i+=1
    subjects_name+= "COMPUTER SCIENCE, "
if maths<33:
    i+=1
    subjects_name+= "MATHS, "

print("FAILED SUBJECTS ARE: " +str(i))
print("FAILED SUBJECTS NAME: " +subjects_name)








