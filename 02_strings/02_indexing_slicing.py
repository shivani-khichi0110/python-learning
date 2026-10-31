#you can range the characters using the slice notationgit
#specify the start index and the end index separate it by colon,to return part of string
b="hello world!!"
print(b[1:6])

#slice from the start by leaving start index
print(b[:8])

#slice till end by leaving end index
print(b[4:])

#use negative index to start the slice from ending
print(b[-5:-2])


#positive indexing
print(b[0])
print(b[2])
print(b[8])

#negative indexing
print(b[-0])
print(b[-2])
print(b[-8])

#skip the characters using step
print(b[::2])

#reverse the string
print(b[::-1])

#start end and step
print(b[1:10:2])

word = "PYTHON"

# 1. Print P
print(word[0])
# 2. Print N using negative indexing
print(word[-1])
# 3. Print PYT
print(word[0:3])
# 4. Print HON
print(word[3:6])
# 5. Reverse the complete string
print(word[::-1])
