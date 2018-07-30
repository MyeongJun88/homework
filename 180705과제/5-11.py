def print_grade(midterm, final):
    total = midterm + final
    if total>=90:
        print ("A")
    elif 80<=total <90:
        print ("B")
    elif 70<=total <80:
        print ("C")
    elif 60<=total < 70:
        print ("D")
    else :
        total <60
        print ("F")

print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)