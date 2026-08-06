# Assignment - 5, on loops---

# -1-print the while loop output in the same line--

num = 1
while num < 11:
    print(num, end = " ")
    num += 1

#---or---

num = 1
while num < 11:
    print(f"{num}", end = "*")
    num += 1

#-2- print star patterns using loop---Right traingle--

#--using loop---Right traingle--
n = 5
for i in range(1, n + 1):
    print("*" * i)

#-2- print star patterns using  loop---Reverse Right traingle--
n = 5
for i in range(5, 0, -1):
    print("*" * i)


#--using nested loop---Right traingle--
rows = 5 # no of rows--
for i in range(1, rows + 1): #, how many rows you want # no of rows--
    for j in range(i): # how many stars want to print--
        print("*", end="")
    print()

#--using nested loop---Reverse Right traingle--
rows = 5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#--using loop---normal traingle--
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i -1))
#--or--
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i -1) + " " * (rows - i))

#--using nested loop---normal traingle--
rows = 5
for i in range(1, rows + 1):
    # print spaces first
    for j in range(rows - i):
        print(" ", end = "")
    # then print star (*) 
    for k in range(2 * i - 1):
        print("*", end = "")
    # for next line    
    print()
# --or---
rows = 5
for i in range(1, rows + 1):
    # print spaces first
    for j in range(rows - i):
        print(" ", end = "")
    # then print star (*) 
    for k in range(2 * i - 1):
        print("*", end = "")
    # print the spaces after star--
    for l in range(rows - 1):
        print(" ", end = "")
    print()

# Factorial of a number--- with function--
# reverse while loop-- 
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
print(factorial(5))

#--for loop --
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial(5))

# Factorial of a number--- without function--
# for loop ----#same as reverse while loop---
n = 5
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print(factorial)

# while loop--
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i = i + 1
    print(factorial) 

# count the number of vowels in a string---
#--for loop--
count = 0
string = "education"
for char in string:
    if char in 'aeiou':
        count += 1
print(count)
# --or---
count = 0
string = "EducAtion"
for char in string:
    if char in 'aeiouAEIOU':
        count += 1
print(count)

# while loop--
string = "education"
count = 0
i = 0 # index
while i < len(string):
    if string[i] in 'aeiou':
         count += 1
    i += 1
print(count)

    
# find the longest word in a sentence using for loop---
sentence = "Python is a high level programming language"
longest_word = ""
for word in sentence.split():
    if len(word) > len(longest_word):
        longest_word = (word)
    else:
        longest_word = len(word)
print(longest_word)

# print first n numbers in the fibonacci sequence using while loop--
num = 5
a = 0
b = 1
count = 0
while count < num:
    print(a, end = "")
    next_num = a + b
    a = b
    b = next_num
count += 1 # cause while don't know , how many many times needs to run

# for loop--
num = 5
a = 0
b = 1
for i in range(num):
    print(a, end = " ")
    next_num = a + b
    a = b
    b = next_num











