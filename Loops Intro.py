#--Loops in python---For and While loop----

#---While loop----, ---use while when you don't know the iteration ---
#-print num from 0 to 5---
count = 0
while count < 6:
    print(count)
    count += 1

#---print num from 1 to 5-- usinf while loop
count = 1
while count < 6:
    print(count)
    count += 1
    #---OR---
    count = count + 1

#---print num from 5 to 1-- usinf while loop

count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("while loop ended")

#--why intialize a variable---check condition to avoid infinite loop---
while True:
    print("again and again")

# for loop---  #--use for loop when you know the iteration
language = 'python' #-language is sequence--
for char in language:
    print(char)

#--range function ---in for loop---
#(start,stop,step)-----
#--if you are giving only one value than its just for stop value--
for i in range(5):
    print(i)
# ptin from 5 to 10-----start and atop
for i in range(5,11):
    print(i)

for i in range(5,11,2): #--start,stop,step = index
    print(i)


for i in range(5):
    print(i)
else:
    print("loop ended")

#--loop control statments----
#-1-pass statement---
for i in range(5):
    #man nhi kr rha hai
    pass

count = 5
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -= 1

#--break statement---
for i in range (3):
    if i ==3:
        break
    print(i)

for i in range (10):
    if i ==3:
        break
    print(i)

    #continue statement---
for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range (5):
    if i ==3:
        break
    print(i)


count = 5  # diifernce between pass and continue stmt
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -= 1


count = 5  #-diifernce between pass and continue stmt
while count > 0:
    if count == 3: #--skip whole iteration 
        continue #
    else: #
        print(count) #
    count -= 1 #

while True:yt
    user_input = input("enter 'exit' to stop: ")
    if user_input == 'exit':
        print("congrats! you gussed it right!")
        break
    print("sorry, you entered:", user_input)

# Nested loops ------
# print number from 1 to 3--
for num in range(1,4):
    print(num)

# now i want 3 times this (print number from 1 to 3--)
for num in range(1,4):
    print(num)
for num in range(1,4):
    print(num)
for num in range(1,4):
    print(num)
#--OR-------
for i in range(3):
    for j in range (1,4):
        print(j)
    print('- - -')

i = 1  #--infinite loop---
j = 1
while i < 4:
    while j < 4:
        print(j)
   


i = 1
while i < 4:
    for j in range(1,4):
        print(j)
    print("- - -")
    i += 1

#--print prime numbers between range of 2 to 10 use nested loop--
for num in range(2,20):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)

a = int(input("enter your first value: "))
b = int(input("enter your second value: "))
for num in range(a,b):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)

#--infinite iteration---
while True: 
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

    for num in range(a, b):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# do while loop--
while True:
    num = int (input("Enter a num grater than 10: "))
    if num > 10:
        print(f"Number is valid:, {num}")
        break
    else:
        print("Number is not greater then 10, try again!")
