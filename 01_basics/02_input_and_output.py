#print function used to display text or output value on the screen
print("hello world") #this will print hello world on screen

#wecan use print function as many time we want to display the output on the screen
print('heello world')
print("32")
print("64")

#each print will print the output on new line by default
print("this is first line")
print("this is second line")

#double quotes and single quotes are same in python
print("hello world")
print('hello world')

#if you want to use multiple words on same line then we can use end parameter in print function
print("this is first line",end=" ")
print("this is second line")

#we can display number in print funtion and we dont need to use quotes for number unlike string
print(31)
print(56)

#we can do calculation in print function
print(3+2)
print(7*5)

#we can combine text and no by seperating it by comma
print("welcome to day",2)

#we can combine string and no. or variable using format method
print(f"this is my line {31}")
s=53
print(f"this is line no {s}")

# a placeholder can contain operation ,fuction amd modifiers to format the value
price=32
r=f"the price of the object is {price}"
print(r)
#if we have to print value till 2 decimal we can use : by followed by legal formatting in modifier 
s=f"the price of the object is {price:.2f}"
print(s)

#we can use math function in it
t=f"the price of object is mrp-20 is {200-20}"
print(t)

#we can take input from user
print("Enter your name ")
name=input()
print(f"hello {name}")

#input function as prompt function
name1=input("enter your name ")
print(f"hello {name1}")
#you can add as many input you want from user
name2=input("enter your name")
print(f"hello name {name2}")
fav1= input("enter your 1st preference :")
fav2= input("enter your 2nd preference :")
fav3= input("enter your 3rd preference :")
print(f"list of preference of {name2} are {fav1} {fav2} {fav3}")

#if you take input from user a integer it will treat it as string
num=input("enter the no")
print(type(num))

#we can convert it no. using int function
num2=int(num)
print(type(num2))