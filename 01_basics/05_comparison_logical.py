#comparision operators return true or false based on comparision
x=5
y=3
print(x==y) #equal
print(x!=y) #not equal
print(x>y) #greater than
print(x<y) #less than
print(x>=y) #greater than or equal
print(x<=y) #less than or equal

#python allows you to chain the comparision operators
print(1 < x < 10)
print( 1 < x and x <10)

#logical operators are used to combine conditional statement
#and return true if both statement are true
print(x>4 and x<5)
#or return true if both statement are true
print(x<5 or x<10)
#not reverse the resultreturn the true if result is false
print(not(x<4 and x>5))