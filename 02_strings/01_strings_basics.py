#string are surrounded by single quotation or double quotation  marks.
x="hello"
y="hello"
print(x,y)

#you can use quotes inside the string as long as they dont match the quotes surrounding the string
a="it' my pen"
b='he is called "johny"'
c="he is callled 'johny'"
print(a,b,c)

#assign a string to a variable
k="khichi"
print(k)

#multiple string to variable by using three quotes
A="""lormnjjfkv ksuisus sjkvois hdvk
mhfsughfkjshkuhdgkygjnvkshh
jhreiuhfkjvnfdkjhg
"""
print(A)

 #or three single quotes
a='''djfhvjhkcn
 cksbjfdk
 jvnkdnflkvm'''

print(a)

#strings in python are array of unicode
#square brackets are used to access the elements of string
a="hello world!!"
print(a[1])

#looping through string
#string are arrays , we can loop through string using for loop
for x in "banana":
    print(x)

#to get a string length you can use len()
a="saloni khichi"
print(len(a))    

#to check phrase or character is present in string we use in keyword
A="they are playing cricket"
print('playing' in A)

#use it in free statement
if "cricket" in A:
    print("yes cricket is in A")

#check if not present in string using keyword not in
print("swimming" not in A)

#use it in if statement
if "swimming" not in A:
    print("it is not there")