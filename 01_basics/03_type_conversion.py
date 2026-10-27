#casting is done using construction function
num1=int(32) 
num2=int(32.2) 
num3=int("32") 
print(num1,type(num1))
print(num2,type(num2))
print(num2,type(num3))

#float
f1=float(3)
f2=float(3.5)
f3=float("33")
f4=float("33.09")

print(f1 , type(f1))
print(f2 , type(f2))
print(f3 , type(f3))
print(f4 , type(f4))

#string
s1=str("string 1")
s2=str(32)
s3=str(32.05)

print(s1 , type(s1))
print(s2 , type(s2))
print(s3 , type(s3))


# Invalid conversion example
# int("hello")  # ValueError

# Complex conversion
c1 = complex(5)
c2 = complex(3, 4)

print(c1, type(c1))  # (5+0j)
print(c2, type(c2))  # (3+4j)

# Practical example: age input

age = "20"
age = int(age)

print(age + 5)  # 25