stud=["mahesh","akshay","chits"]
for i in stud:
    s1=int(input("Enter mark of 1st subject for "))
    s2=int(input("Enter mark of 2nd subject for" ))
    s3 = int(input("Enter mark of 3rd subject for"))
    add=s1+s2+s3
    per=(add/300)*100
   # print(i, "\t\t", s1, "\t", s2, "\t", s3, "\t", per)
    

print("Student name\t\tmark1\t\tmark2\t\tmark3\t\tPercentage")
for i in stud:
    print(i)
    for j in mark:
        print(j)

