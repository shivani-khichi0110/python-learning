#variables:This are containers for storing value
#python has no command for declaring variable
x=9 #x is variable and it stores value 
y='john' #y is variable that stores value
print(x) #this will print value stored in variable x
print(y)#this will print value stored in variable y

# and we do not have to declare type of variable
#they can change the type afetr they have been set
a=30
#a store the value integer it is a integer vaiable
a='letter'
#so now the type of varible will be changed to string
print(type(a))

#in above example we  have seen that we have printed the type of variable using type function
# doble quotes and single quotes are same in python
a="hello"
a='hello'

print(a) #this will print hello
#variable names can start with letter or underscore but not with the number
#variable names are case sensative
a=43
A=45
print(a,A) # this will print 43 45
#A will not override a because they are different varible as above mentioned a varible is overide by a=43

#assigning 1 value to multiple variables
x=y=z=10
print(x,y,z) #this will print 10 10 10

#many value to multiple variables in once
x,y,z=10,30,40 # by seprating the values with comma
print(x,y,z) #this will print 10 30 40

#we can create list aur tuple and assign them to multiple variables
#list
fruits=['apple','banana','cherry']
x,y,z= fruits
print(x)#this will print apple
print(z)#this will print cherry

#tuple
colors=('red','green','blue')
x=colors
a,b,c=colors
print(x)#this will print ('red','green','blue')
print(a)#this will print red

#variable overwriting
x=10
x='shivani' 
print(x) # this will print shivani because the value of x is overwritten by 'shivani'

#case sensitivity
word='hello'
Word='world'
print(word) #this will print hello
print(Word) #this will print world

#multiple assignment
x,y,z=10,20,30
print(x,y,z)#this will print 10 20 30

 #swapping two variables
a=5
b=20
a,b=b,a
print("a:",a) #this will print 20
print("b:",b) #this will print 5

#print function often used to display the value of the variable
print(a)

# in print function multiple variable ar mention in one print statement by separating with comma
m=10
n=25
s="hello"
print(m,n,s)


k="python"
print(s,k)

#we can write multiple variable by using + operator
print(s+k)

#on addintion of string we can also add space between them by adding space in between the string
print(s+" "+k) #this will print hello python

#we cant add string and integer using + operator it will give error
#print(s+m) this will give error

print(s+str(m)) #this will print helllo10 because we converted integer to string using str() function
 #or best way to write is to use comma in print function
print(s,m) #print hello 10

#global variables: variables that are defined outside of a function and can be accessed inside the function
x=10 #global variable
def myfunc():
    print(x) #this will print 10 because x is a global variable

myfunc() # this will call the function and print 10

def myfunct():
    global n #declaring n as a global variable
    n=35
    y=20 #local variable
    print(y) #this will print 20 because y is a local variable

#print(y) #this will give error because y is local variable
print(n) # this will print 35 because n is a global variable


#data types: data types are the classification of data items it tells the type of value a varible store
A= "hello world!" #string= text type
B=20 #int= integer type
C=20.5 #float= decimal type
D=1+1j #complex= complex type
E= ["apple","banana","cherry"] #list= ordered and changeable collection
F= ("apple","banana","cherry") #tuple= ordered and unchangeable collection
H= range(6) #range= ordered sequence of numbers
I= {"name":"john","age":36} #dict= it stores key values pairs it is unordered,changeable and indexed collection you can access the value using key
J= {"apple","banana","cherry"} #set= unordered and unindexed collection
K= True #bool= boolean type
 #to know datatype of variable we can use type function
print(A,type(A))
print(B,type(B))
print(C,type(C))
print(D,type(D))
print(E,type(E))
print(F,type(F))
print(list(H),type(H))
print(I,type(I))
print(J,type(J))
print(K,type(K))












