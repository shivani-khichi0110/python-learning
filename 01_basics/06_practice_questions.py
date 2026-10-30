#1. Create 5 variables to store:
#- Your name
name="shivani"
#- Your age
age= 34
#- Your CGPA
CGPA=8.5
#- Your college name
college_name="vit bhopal"
#- Whether you are a student (True/False)
student=True
#Print each variable with its data type using type().
print(name, type(name))
print(age , type(age))
print(CGPA ,type(CGPA))
print(college_name  ,type (college_name))
print(student , type(student))

#2. Create three variables a = 10, b = 20, c = 30. Print their sum.
a,b,c= 10,20,30
print(a+b+c)

#3. Create a variable name = "Python" and print:
#Complete string
name= "python"
#First character
print(name[0])
#Last character
print(name[-1])
#Length of string
print(len(name))

#4.Create variables using different data types: int, float, str, bool. Print their types.
num1=35
num2=35.5
name="today is monday"
number=True
print(type(num1))
print(type(num2))
print(type(name))
print(type(number))

#5.Create three variables in a single line and print their values.
a,b,c=25,65,90
print(a,b,c)

#6.Ask the user for their name and print:
Name=input("enter your name")
print(f"Hello {Name}, welcome to Python!")

#7.Ask the user for their age and print their age after 5 years.
Age=int(input("enter your Age"))
print(f"Age after 5 years {Age+5}")

#8.Ask the user for two numbers and print their sum.
a=int(input("enter the 1st no."))
b=int(input("enter the 2nd no."))
print(a+b)

#9.Ask the user for:
#- Name
Name=input("enter the name")
#- Age
Age=int(input("enter the age"))
#- College name
college_name=input("enter the college name")
#Print all details in a properly formatted output.
print(f"student name is{Name} age is {Age} and college is {college_name}")

#10.Ask the user for length and width of a rectangle. Print both values and their product (area).
length=int(input("enter the length"))
width=int(input("enter the width"))
print(f"area of rectangle of length {length} and width {width} is {length*width} ")

#11.area and perimeter
length = int(input("Enter length: "))
width = int(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

#12.Convert "100" into an integer and print its type.
x="100"
x=int(x)
print(x , type(x))

#13.Convert 25 into a float and print its type.
y=25
y=float(y)
print(y , type(y))

#14.Convert 45.89 into an integer. Observe the output.
a=45.89
a=int(a)
print(a , type(a) )

#15.Ask the user for two numbers and calculate their sum. Make sure the inputs are converted into integers.
number1=int(input("enter the 1st no."))
number2=int(input("enter the 2nd no."))
total=number1+number2
print(total)

#16.Convert both into integers and calculate their:
a = "50"
b = "25"
a=int(a)
b=int(b)
print(f"sum is {a+b}")
print(f"product is {a*b}")
print(f"difference is {a-b}")

#17.Ask the user for two numbers and perform all arithmetic operations:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Floor Division:", a//b)
print("Exponentiation:", a**b)

#18.Ask the user for marks in 5 subjects. Calculate total marks and percentage (assuming each subject is out of 100).
sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))
sub4 = int(input("Enter subject 4 marks: "))
sub5 = int(input("Enter subject 5 marks: "))

total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500)*100
print(f"total marks is {total_marks} and percentage is {percentage}")

#19.Ask the user for a number and print its square and cube using the exponentiation operator.
n=int(input("enter the no. to square and cube"))
square=n**2
cube=n**3
print(f"square of no. {square} and cube of no. is {cube}")

a = 25
b = 15

print(f"Is a greater than b? {a>b}")
print(f"Is a smaller than b? {a<b}")
print(f"Are both equal? {a==b}")
print(f"Are they not equal? {a!=b}")

#20.Ask the user for their age. Check whether they are eligible to vote (age 18 or above).
Age=int(input("enter your age"))
print(f" you are eligible to vote : {Age>=18}")

# 21.Ask the user for marks. Check whether:
marks=int(input("enter your number"))
#- Marks are greater than or equal to 40.
print(marks>=40)
#- Marks are less than 100.
print(marks<100)
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
result = age >= 18 and nationality == "Indian"
print("Eligible:", result)


#22. number check
num = int(input("Enter a number: "))
result = num >= 10 and num <= 50
print("Number is in range:", result)