## Basics of Python
'''print() this statement prints the thing inside the paranthases'''
#print("hello world")
##________________________________________________________________________________________________________________________

## NEW LINE & carriage return
'''things in print statement '''
# print("hello\rworld")  #this is default new line in windows
# print("hello \t world")  #this is default new line in linux/mac
#\r is carriage return make cursor to move to starting of the line
#\n is line feed make the cursor to new line


#________________________________________________________________________________________________________________________
'''string is a data type'''
## STRING METHODS

# name = input("Enter your full name:")
# print(len(name))
# print(name.find(input("enter a letter to find#")))
# print(name.rfind(input("enter a letter to find from reverse#")))
# print(name.capitalize())#first letter in capital
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name)
# a=input("enter your name")
# print(f"is upper? {a.isupper()}")
# a=input("enter your name")
# # print(f"is lower? {a.islower()}")
# a="hello"
# print(a.replace("hell","heaven"))

""" once a str is made we can't edit like list """
# a="hello world"
# a[0]='2'
# print(a)

""" find function,finds the index of given input in a value , if not found in the value it prints -1"""

# a="python programmer"
# print(a.find("py ")) #this one give 0 as OP
# print(a.find("java")) #this one give -1 as OP

# a = "hello"
# print(id(a))
# a += " hey"
# print(id(a))

##sep(),replace()
# print("hello","world","welcome")
# print("hello","world","welcome",sep=",")
# print("welcome","all","python","users",sep="/",end=" ")
# print("work","hard","save","life")

# a=input(">")
# a=a.replace(" ","")#this is used if user give extra space behind it will remove
# print(a.replace(" ","."))
##________________________________________________________________________________________________________________________

## INDEXATION
"""-ve step value is reverse"""
# a.[start:end:step]
# a="74979273453462536553"
# print(a[0:6:2]) #only str can be indexed
# print(a[-1]) #print last str in a
# print(a[-7:-4:2]) #direction matters this is from left to right so +ve step value
# print(a[-4:-7:-2]) #direction matters this is from right to left so -ve step value
# print(a[:5]) #5 is excluded
# print(a[::2]) # print everything except 2nd place of str

# credit_number="1234-5678-9012-3456"  #real life usage
# last_digits=credit_number[-4:]
# print (f"XXXX-XXXX-XXXX-{last_digits}" )


# l=[1,2,3,4,5,6,7,8,9]
# print(l[-3:0])#we can only index list from left to right that means from top
# print(l[-3:0:-1])#to index list from right to left we need to use -1 as step value, reverse the matrix
##________________________________________________________________________________________________________________________
'''for loop '''
##for loop
# for x in reversed(range(0,11)):
#     print(x)
                                      ##BOTH are not same,above it exclude 11,but below exclude 0
# for x in range(10, 0, -1):  ##"-1" always use when to read it from last
#     print(x)
#________________________________________________________________________________________________________________________

##if elif else
"""we can use as many as elif statements"""
# a=None
# if a:
#     print(a)
# else:
#     print("None is similar to False")
'''if  statement can exist alone '''
# a=1
# if a.is_integer():
#     print("this is a number")
"""else can be paired with while """
##While loop
"""runs the cmd until the the statement is False"""
# a=None
# while a:
#     print(a)
# else:
#     print("we can use while and else ")
##________________________________________________________________________________________________________________________

# import math
#
# x=-9.1
# print(math.ceil(x))
# print(abs(-10))#this is modulus function
# a=5.8947
# print(round(a,2))
# print(pow(3,5))
# print(max(10,23,898))
# print(min(10,23,898))
# print(max(10,10,10))
# a=20
# a-=10
# print(a)
# a=20
# a*=10
# print(a)
# a=20
# a**=2
# print(a)
# a/=21 #this means that when we divide a group of 21 persons into 4 how many is left reminder
# a%=4 #moduls division
# print(f"reminder is{a}")#fstring
##________________________________________________________________________________________________________________________

##THIS IS KNOWN AS CONDITIONAL EXPRESSION
# num=float(input("Enter a number: "))
# print("positive"if num>0 else "negative")   #OP +/-

# num=float(input("Enter a number: "))
# print("positive"if num>0 else print("negative"))  #OP +/- and none bcz print statement already given.
##________________________________________________________________________________________________________________________

## FORMATE SPECIFIER
"""there of lot of stuff learn it"""
# a=688374.9089
# print(f"{round(a,2)}") #result in float
# print(f'{a:.2f}') #rsult in str FORMAT SPECIFIERS
##________________________________________________________________________________________________________________________

"""if u want to run a loop until u get correct input u should keep incorrect-
   -condition in loop so when u get correct input the loop breaks eg:- below"""
##________________________________________________________________________________________________________________________

##LUMPSUM CALCULATOR EG FOR ABOVE
# principle = 0 #THIS IS CONDITION
# rate = 0
# time =0
# while principle <= 0: #THIS CONDITION IS INCORRECT INPUT,PRINCIPLE CAN'T BE <=0
#     principle =float(input("Enter the principle amount (₹):"))  #loop runs until user gives correct input
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")
# while rate <= 0:
#     rate =float(input("Enter the rate (%):"))
#     if rate <= 0:
#         print("rate can't be less than or equal to zero")
# while time<= 0:
#     time =float(input("Enter the time (Yr):"))
#     if time <= 0:
#         print("time can't be less than or equal to zero")
# print(f"ur principle is {principle} ₹")
# print(f"ur rate is {rate} %")
# print(f"ur time is {time} Yr")
# total = principle*pow((1 +rate/100),time)  # FORMULA TO CALCULATE TOTAL AMOUNT
# print(f"total amount u made {round(total)} ₹")
##________________________________________________________________________________________________________________________

##LUMPSUM CALCULATOR IN ANOTHER WAY
# while True:
#     principle = float(input("Enter the principle amount (₹):"))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")
#         break
#     else:
#         while True:
#             rate = float(input("Enter the rate (%):"))
#             if rate <= 0:
#                 print("rate can't be less than or equal to zero")
#                 break
#             else:
#                 while True:
#                     time = float(input("Enter the time (Yr):"))
#                     if time <= 0:
#                         print("time can't be less than or equal to zero")
#                         break
#                     else:
#                         print(f"ur principle is {principle} ₹")
#                         print(f"ur rate is {rate} %")
#                         print(f"ur time is {time} Yr")
#                         total = principle * pow((1 + rate / 100), time)
#                         print(f"total amount u made {round(total)} ₹")
#                         break
#             break
#         break
##________________________________________________________________________________________________________________________

# import time
# my_time =int(input("Set timer seconds:"))
# for x in range (my_time, 0,-1):
#     print(x)
#     time. sleep(1)
# print("time up")
##________________________________________________________________________________________________________________________

##COUNTDOWN TIMER PROGRAMME
# import time
# my_time =int(input("Enter the time in seconds:"))  #we're dealing t in sec so 60 ,3600 are used
# for x in range (my_time, 0,-1):
#     seconds=x%60               #WHY used '%' by 60,we deal with time
#     minutes=int(x/60)%60
#     hours=x//3600
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time. sleep(1)
# print("time up")
##________________________________________________________________________________________________________________________

##TO UNDERSTAND OPERATIONS DONE IN COUNTDOWN TIMER
# print(1%60)
# print(61%60)
# print(60.3%60)
# print(61/60)
# print(int(61/60))
# print(int(3603/60)%60)
# print(3603/60%60)
# print(3600//60)
# print(3603//60)
# print(0%60)
##________________________________________________________________________________________________________________________

##NESTED LOOP TO PRINT EVEN NUMBERS
# import itertools , time  #used INTER-TOOLS to import and use integer
#
# for x in itertools.count(start=0): # int starts with 0 ends in infinite .
#     if x % 2 == 0 and x<=100:
#         time.sleep(0.5)
#         print(x, end=',')

##range(0,)  in for loop range fn we can't set upto infinite,returns nothing

# for x in range(3):  #actually this line means x in range 0-3,3 excluded once the line read it runs the loop until x=2
#     for x in range(1,10):  #one the 1st line read by python it never again read it back
#         print(x,end=" ") #so even though we gave 'x' in both loop we get no error
#     print() #this line breaks end statement
# print("only after the loop completes") # this line is to say that one a loop starts it never again read it back the 1st line
##________________________________________________________________________________________________________________________

##PRINTING equilateral triangle with even num sym
# row= int(input("Enter # of row: "))
# symbol= input("Enter symbol: ")
# for x in range(1,row+1):
#     width=row*2  #see the with should be even or odd
#     num=2*x      #need to change number of symbol into even or odd,so we get perfect sync
#     sym=symbol*num
#     print(sym.center(width))
"""in odd space odd num can be placed in center vice versa"""
## PRINTING equilateral triangle with odd num sym
# row= int(input("Enter # of row: "))
# symbol= input("Enter symbol: ").replace(" ","") #removing empty space using replace cmd because it affects the structure
# symbol= symbol.upper()
# for x in range(1,row+1):
#     width=row*2 - 1
#     num=2*x - 1
#     sym=symbol*num
#     print(sym.center(width))
##________________________________________________________________________________________________________________________

""""  dir() fun is used to see the methods that can be done with the give data below is eg given str in dir()
       while printing that we see the method that can be done with the give data  """
# print(dir("hello"))
'''help(enter the data type ) to know the methods of the data type with description'''
# print(help(list))

##________________________________________________________________________________________________________________________

## LIST AND OPERATIONS
"""it is iterable means we can use in for loop to return one element at as time"""
# fruits=["apple", "orange", "banana", "coconut","orange","banana"] #duplicates allowed and ordered
# print(len(fruits))
# print("pineapple" in fruits)
# fruits[0]="apple" #list can be modified even after created
# print(fruits)
# fruits.append(" pineapple")
# fruits.remove("apple")
#fruits.insert(2," pineapple")
# fruits.sort() #sort according to ascending
#fruits.reverse() #reverse the list not descending order
"""to descend use sort and reverse"""
# fruits.clear()
# print(fruits.index( "orange" ) )
# print(fruits.count( "banana") )
# print(fruits)
#print("apple" in fruits)
# fruits.clear()   #code to clear all elements in a list
# print(fruits)

"""this is list unpacking"""
# new_list=[("hello","world","code"),("code","with","mosh")]
# for a,b,c in new_list:
#     print(a,b,c)
"""the below code gives error because we need one more variable to unpack the list"""
# new_list=[("hello","world","code"),("code","with","mosh")]
# for a,b in new_list:
#     print(a,b)
"""the below returns every tuple in that list,doesn't unpack bcz of one variable"""
# new_list=[("hello","world","code"),("code","with","mosh")]
# for a in new_list:
#     print(a)

"""this is how we convert list to string"""
# a = ["hello", "boss", "123"]
# s = " ".join(a)      # join with space
# print(s)   # hello boss 123
# print(type(s))

# a=[1,2,3,"hello"]
# s=" ".join(map(str,a)) #here we use map for mapping the elements to a and use str fun make it str then use join to add
# print(s)
# print(type(s))


'''MATRIX MULTIPLICATION nested list '''
# A = [[1, 2, 3],
#      [4, 5, 6]]
#
# B = [[7, 8],
#      [9, 10],
#      [11, 12]]
#
# # Result matrix (2x2)
# result = [[0, 0],
#           [0, 0]]
#
# # Matrix multiplication
# for i in range(len(A)):           # rows of A
#     for j in range(len(B[0])):    # cols of B
#         for k in range(len(B)):   # rows of B
#             result[i][j] += A[i][k] * B[k][j]
#
# print("Result:", result)


# ar=int(input("enter matrix A's row: "))
# ac=int(input("enter matrix A's columns: "))
# a=[]
# for i in range(ar):
#     a.append([])
# for i in range(len(a)):
#     for j in range(ac):
#         a[i].append(int(input(f"enter A{i+1}x{j+1}: ")))
#
#
# br=int(input("enter matrix B's row: "))
# bc=int(input("enter matrix B's columns: "))
# b=[]
# for i in range(br):
#     b.append([])
# for i in range(len(b)):
#     for j in range(bc):
#         b[i].append(int(input(f"enter B{i+1}x{j+1}: ")))
#
# for i in a:
#     print(i)
# print()
# for i in b:
#     print(i)
#
# matrix=[]
# if len(a[0])==len(b):
#     for i in range(len(a)):
#         matrix.append([0]*len(b[0]))
# if ac==br:
#     for i in range(len(a)):
#         for j in range(len(b[0])):
#             for k in range(len(b)):
#                 matrix[i][j]+=a[i][k]*b[k][j]
# else:
#     print()
#     print(f"Matrix multiplication fails as matrix A column is {ac} not equals to matrix B row {br}")
# print()
#print(matrix,sep="\n")

# a=2
# b=344
# print(sum([a,b]))##sum() works for list,tuple so we make a and b as list or tuple
# print(sum((a,b)))

# a=[1,2,3,4,5,6,7]
# b=['a','b','c','d','e','f']
"""zip fun is used to use 2 variable and 2 range in a forloop"""
# for a,b in zip(a,b):   #BY this we can use 2 variable in a single loop
#     print(a," ", b)

##List comprehension
# doubles =[x * 2 for x in range(10)]
# triples =[y * 3 for y in range(10)]
# squares =[z * z for z in range(10)]
# print(doubles)
# print(triples)
# print(squares)

# fruits =["apple", "orange", "banana", "coconut"]
# fruits=[fruit.upper() for fruit in fruits]
# print(fruits)

"""+1 so we get that num too"""
# even_num=[num for num in range(int(input("Enter a num to print even num up to it:"))+1) if num%2==0]
# print(even_num)
# even_num=[num for num in range(int(input("Enter a num to print odd num up to it:"))+1) if num%2!=0]
# print(even_num)

# lst = [1, 2, 3]
# print(lst)
# print(id(lst))
# lst.append(4)
# print(lst)
# print(id(lst))
##________________________________________________________________________________________________________________________

##SETS and operations
"""sets is unordered list so we can't able to use index"""
"""it is iterable(can be used in loop),str is mutable but it's element is immutable(so we can't use mutable objects)"""
# fruits ={"apple", "orange", "banana", "coconut","orange","banana"} #duplicates are not allowed but mutable
# print(fruits)
# print("apple" in fruits)
# fruits.add("grapes") #append in list add in sets
# fruits.remove("orange")
# print(fruits.pop()) #removes an element from the set and print it in print statement

"""no duplicates"""
# print({1,3,4,5,6,7,4,5,4,5,4})
##________________________________________________________________________________________________________________________

##TUPLE and operations
"""immutable and ordered ,duplicates are allowed and faster """
"""it is iterable(can be used in loop) and elements can be mutable like list"""
# a=1,2,3,4,5   #this is Implicit tuple """it is iterable"""
# print(sum(a))

# fruits =("apple", "orange", "banana", "coconut","orange","banana")# it has similar operation like list and sets

# print(help((1,2,3,"a")))

# x = (5)  # Not a tuple — just an int
# print(type(x))
# y = (5,)      # Tuple with one element
# print(type(y))
##________________________________________________________________________________________________________________________

##QUIZ game PROGRAMME using list ,tuple
# questions =    ("How many elements are in the periodic table?",
#             "Which animal lays the largest eggs? ",
#             "What is the most abundant gas in Earth's atmosphere? ",
#             "How many bones are in the human body? ",
#             "Which planet in the solar system is the hottest? ")
# options=(("A.112","B.108","C.118","D.12O"),
#          ("A.Whale", "B.Bee","C.Crocodile", "D.Ostrich "),
#          ("A.Carbon-Dioxide","B.Nitrogen","C.Oxygen","D. Hydrogen"),
#          ("A.206","B.207","C.208","D.209"),
#          ("A.Mercury","B.Venus","C.Earth","D.Mars"))
# answers=["C","D","B","A","B"]
# guesses=[]
# q_no=0
# score=0
# for question in questions:
#     print(question)
#     for option in options[q_no]:
#         print(option)
#     guess=input("Answer:").upper()
#     guesses.append(guess)
#     if guess == answers[q_no]:
#         print("Correct!")
#         score+=1
#     else:
#         print("Incorrect!")
#     print()
#     q_no+=1
# print(f"Total score: {score}/{len(questions)} or {score/len(questions)*100:.2f}%")
##________________________________________________________________________________________________________________________

##DICTIONARY and operations
'''in a dictionary {key:value},mutable , ordered,no duplicates allowed'''
"""it is iterable and keys are immutable"""

# d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
# for num in d:          #returns keys of dict
#     print(num)

capital={"usa":"washington.d.c.","india":"delhi","japan":"tokyo","china":"beijing"}

# print(capital["india"])
# print(capital.get("india")) # .get() is used so if key doesn't exist it won't give error
# print(capital.get("russia")) #if the key doesn't exist in the dict returns None

# capital["china"]="delhi"  #by this value of key can be changed

# del capital["usa"]     #remove key 'usa' and it's value

# capital.clear()   #delete all the elements in the dict

# capital.update({"russia":"moscow"})  #add new key value pair

# print(capital.pop("china")) #it removes china from dict and return the value of 'china' ,atleast 1 argument atmost 2

# capital.pop("Israel","404 not found") #in dict no key named "Israel" it prints the 2nd argument so we don't get error
# capital.pop("Israel") #now we get key not found error

# print(capital.popitem()) #takes no argument,removes last key-value from the dict
# print(capital)

# print(type({})) #this is dict fun

"""using this method can get keys and values of dict"""
# print(capital.keys())
# print(capital.values())
# for key,values in zip(capital.keys(),capital.values()):
#     print(f"capital of {key} is {values}")

'''same as above code but diff method'''
# print(capital.items())  #returns KEYS and VALUES in a list [("key","value")]
# for key,value in capital.items():  #here we use list unpacking
#     print(f"capital of {key} is {value}")
##________________________________________________________________________________________________________________________
## "PROJEST concession" ORDER here

# menu={"idle":20,"dosai":40,"vadai":10,"pongal":50}
# quantities={"idle":0,"dosai":0,"vadai":0,"pongal":0}
# your_cart={"idle":0,"dosai":0,"vadai":0,"pongal":0}
# total =0
#
# for food,price in menu.items():
#     print(f"{BOLD}{food.upper():8}{RESET} Rs{BOLD}{price}{RESET}")
# print()  #used for space in output
# for food in menu.keys():
#     quantities[food]=int(input(f"how many {BOLD}{food.upper()}{RESET} do you want?"))
#
# for quantity,price,food in zip(quantities.values(),menu.values(),menu.keys()):
#     t_price=price*quantity
#     your_cart[food]=t_price
#     total +=t_price
# print(f"\n-------------YOUR CART--------------")
# print("Items   Qty   price")

"""the below code is to remove the item that has 0 quantity so we can avoid displaying it
and to remove that it from the dict we use [key for key, value in your_cart.items() if value == empty]
this work in a way for key,value in your_cart.items() it unpack the list and if value == empty,empty = 0 has been
assigned,if any value in dict has 0 then the key is extracted ['key' for key, value in .........]
                                                                 ↑ by this cmd"""

# empty=0
# keys_to_remove = [key for key, value in your_cart.items() if value == empty]
# for key in keys_to_remove:
#     del your_cart[key]
# keys_to_remove = [key for key, value in quantities.items() if value == empty]
# for key in keys_to_remove:
#     del quantities[key]
#
# for food,quantity,price in zip(your_cart.keys(),quantities.values(),your_cart.values()):
#     print(f"{BOLD}{food:8}{quantity}   Rs{price}{RESET}")
# print(f"\n{BOLD}YOUR TOTAL  Rs{total}{RESET}")
# print(f"\n----YOUR ORDER PLACED SUCCESSFULLY----")
##________________________________________________________________________________________________________________________

##random module
# import random
# low = 1
# high = 100
# options =("rock", "paper", "scissors")
# cards=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# print(random.randint(low, high))
# print(random. random())
# print(random.choice (options))
'''print(random.shuffle(options)) we can shuffle tuple so we get error'''
# random.shuffle(cards)
# print(random.choice (cards))
# print(cards)
##________________________________________________________________________________________________________________________

##FUNCTIONS
"""we can use a func anywhere and avoid repetition of code can been runed for many times"""
# def add(a,b):  #a,b is parameter
#     return a+b  #return statement returns the result to the caller back
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return round(a/b,2)
# operation=input("enter the math operation (+,-,*,/) =")
# if operation == "+":
#     print(add(int(input("num1")), int(input("num2"))))
# elif operation == "-":
#     print(sub(int(input("num1")), int(input("num2"))))
# elif operation == "*":
#     print(mul(int(input("num1")), int(input("num2"))))
# elif operation == "/":
#     print(div(int(input("num1")), int(input("num2"))))
# else:
#     print("error")

# # Function to find HCF (GCD)
# def find_hcf(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


# Function to find LCM using HCF

# def find_lcm(a, b, hcf):
#     return (a * b) // hcf

# # Taking input
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# hcf = find_hcf(a, b)
# lcm = find_lcm(a, b, hcf)

# print("HCF =", hcf)
# print("LCM =", lcm)

"""don't define value in default argument 
    bcz is executed immediately when the function is defined,
    not when it's called"""
# def greet(name=input("Enter your name: ")):
#     print(f"Hello, {name}!")

"""parameter are 4 types positional,default,keyword,arbitrary/Variable-length Positional,Variable-length Keyword"""

"""positional"""
# def add_all(a,b,c,d):
#     return a+b+c+d #retutn sum(a,b,c,d) gives error bcz int cant be performed by sum
# print(add_all(1, 2, 3, 4)) #orders matters

"""default we asign a value in the parameter we can change it by giving value in argument 
    all default parameter should be in last"""
# def add_all(a,b,c,d=10):
#     return a+b+c+d
# print(add_all(1, 2, 3, 4))  #4 is given so it take d=4 if not given d=10

"""keyword argument"""
# def add_all(a,b,c,d):
#     return a+b+c+d
# print(add_all(a=2,c=34,d=56,b=90)) #order doen't matters

"""arbitary/Variable-length Positional"""
# def add_all(*add):
#     print(type(add))    #concider the given positional argument as tuple
#     print(add)
#     return sum(add)
# print(add_all(1, 2, 3, 4))

"""Variable-length Keyword"""
# def add_all(**add):
#     print(type(add))    #concider the given positional argument as dict
#     print(add)
#     return sum(add.values())
# print(add_all(a=1,b= 2,c= 3,d=4))

# from math import pi, pow
# def volume_sphere(r):
#     vol= (4/3) * pi * (pow(r, 3))
#     return round(vol,2)
# print(volume_sphere(r=float(input("enter the radius of sphere:"))))


# def words(s):
#     lis=s.split()
#     l=[x[::-1]  if len(x)>=5 else x for x in lis]
#     print(' '.join(l))
# words(input("ENTER :"))

##________________________________________________________________________________________________________________________
## Learn from error

# import itertools
"""while loop runs infinite time,num=1 so else statement execute,num=2 'while' true so 'if' statement execute, 
while condition doesn't brake bcz still num=2,it won't change it change when the while statement brakes"""
# last = int(input("Enter a num to print even num up to it:"))
# for num in itertools.count(1):
#     while num <= last :
#         if num % 2 == 0:
#             print(num)
#         else:
#             break
#     else:
#         break

# import itertools

"""use break statement in 'if' so after exectution it goes to next num in for loop"""
# last = int(input("Enter a num to print even num up to it:"))
"""no need for itertools just used to remember it"""
# for num in itertools.count(1):
#     while num <= last :
#         if num % 2 == 0:
#             print(num,end=",")
#             break
#         else:
#             break
#     else:
#         break

# last = int(input("Enter a num to print odd num up to it:"))
# for num in itertools.count(1):
#     while num <= last :
#         if num % 2 != 0:
#             print(num,end=",")
#             break
#         else:
#             break
#     else:
#         break

"""for below code u get out put perfectly but the code will run even after o/p bcz of initertool.count(1)
it goes from 1 to infinite even though 'while' is false so use elese and break so when 'while' false hole for loop ends
so u can save ur laptop and then the below codes execute """
# last = int(input("Enter a num to print odd num up to it:"))
# for num in itertools.count(1):
#     while num % 2 != 0 and num < last:
#         print(num, end=',')
#         break

"""right code for the above """
# last = int(input("Enter a num to print odd num up to it:"))
# for num in itertools.count(1):
#     while num % 2 != 0 and num < last:
#         print(num, end=',')
#         break
#     else:
#         break #now after 'while' is false whole for loop ends
"""learnt how while works and where to use break statement understand a language like a friend know abt it
instead of just learning how u can do it by spending time"""
##________________________________________________________________________________________________________________________
##id() is used
# x = (1, 2, 3)  #for immutable data type id() will be same if value is same
# y = (1, 2, 3)
# print(x == y)
# print(id(x))
# print(id(y))
# print(x is y)
# print()

# x = [1, 2, 3]
# y = [1, 2, 3]   #same value , they  are mutable so they give diff id()
# print(x == y)   # True  (values same)
# print(id(x))
# print(id(y))    # different ids
# print(x is y)

##________________________________________________________________________________________________________________________

## BINARY AND IT BIN OPERATIONS
# print(bin(5))
# print(bin(4))
# print(5&4)
# print(bin(5|4))
# print(bin(4|5))
# print(~(2)+(2))
# print(3 and 4)
# print(4 and 3)
# print(6 or 5)
# print(5 or 6)
# print("a" or 5)
# print(bool("a"))
# print("a" and 5)
## AND have more priority than or
# print(2<4 or 5>10 and 2>10)
# print("ejh" and False)
# print(3 or 5)
#print(bin(3)^bin(4))

#>> left shift in bin formula "a<<n=a×(2^n)"

# a=bin(10)
# print(a)
# a=bin(10<<2)
# print(a)
# print(int(a,2))

#>> right shift formula "a>>n=a//(2^n)"

# a=bin(10)
# print(a)
# a=bin(10>>2)
# print(a)
# print(int(a,2))

##________________________________________________________________________________________________________________________

## Match-case statements(switch)__alternative for if,else statement,execute if a value match a "case"
"""maybe this code done simple but made this to understand a new topic"""
"""match case is better than if,elif,else condition for unpacking a tuple"""
# def days(num):
#     match num:
#         case 1: return 'MONDAY'
#         case 2: return 'TUESDAY'
#         case 3: return 'WEDNESDAY'
#         case 4: return 'THURSDAY'
#         case 5: return 'FRIDAY'
#         case 6: return 'SATURDAY'
#         case 7: return 'SUNDAY'
#         case _: return 'ERROR'                    #"_" is like else
# print(days(int(input("enter num 1-7: "))))

# student = (input("enter name: "), int(input("enter age: ")), input("enter ur stream: "))
#this is simple and better in pay to unpack a data
# match student:
#     case (name, age, "cse"):  #if student[2]=="cse" kind of thing
#         print(f"{name} is {age} years old and studies Computer Science")
#     case (name, age, "ece"):
#         print(f"{name} is {age} years old and studies Electronics")
#     case (name, age, branch):
#         print(f"{name} is {age} years old and studies {branch}")


# def transaction(mode):
#     match mode:
#         case "online" | "cod" | "wallet": return "payment accepted"  # "|" is similar to "or" statement
#         case _: return "payment rejected"
# print(transaction(input("enter mode of transaction : ")))

##________________________________________________________________________________________________________________________

## Ways to use modules

# import math
# print(math.pi)
# import math as m
# print(m.pi)
# from math import pi
# from math import * #'*' means import every fun() in math module
# print(pi)

"""concept called variable scope LOCAL ,ENCLOSED ,GLOBAL ,BUILT-IN """
"""computer access variable in this order L-E-G-B 1st go from LOCAL"""

# from math import e '''this is BUILT-IN scope'''
# a,b,c,d,e=1,2,3,4,5 '''this is GLOBAL scope'''
# print(e**a)    #here we get 5 as O/p bcz we gave another value for e and it goes for GLOBAL
# print(e**b)
# print(e**c)
# print(e**d)
# print(e**e)

## '**' exponential have more priority in arithmetic operations
# import math as m
# # a,b,c,d,e=1,2,3,4,5
# # print(m.e**a) #here we get e as O/p bcz we used m.e so computer take e from module
# # print(m.e**b)
# # print(m.e**c)
# # print(m.e**d)
# # print(m.e**e)

##________________________________________________________________________________________________________________________

## Creating own module make a new python file and add some def (functions) to it
# import area as a #area.py file have fun() like circle,square,rectangle so we can use by importing the file
# print(a.circle(2)) #fun call using some arguments
# print(a.rectangle(6,2))

##________________________________________________________________________________________________________________________

## "__name__" dunder(__) '__name__' prints main if executing in the same file
# print(__name__)

'''while using import area,it execute area file,in area file i have written print(__name__) if i execute that
file in revision.py it prints area when i import'''
"""module is .py file which contains fun() & class"""
"""Library is collection of modules"""
# import main
# import area
# print(help(area)) #use help fun() to see fun()and all details in area.py

##________________________________________________________________________________________________________________________

##GAMBLING GAME

# import random,time
# symbol=["💲","#️⃣","😞","😊"]
# result = []
# balance=0

# def start():
#     gambling()

# def topup():
#     pay=int(input("Top up before BETTING: "))
#     global balance
#     balance+=pay
#     gambling()

# def play():
#     # for a in range(3):
#     #     result.append(random.choice(symbol))
#     global result
#     result = [random.choice(symbol) for x in range(3)]
#     return all(x==result[0] for x in result)

# def gambling():
#     global balance
#     while balance>0:
#             bet = input("enter how much u want to bet: ")
#             # why we use input not int bcz if user gives str it will be error to avoid it we use input
#             if not bet.isdigit():
#                 print("not valid")
#             bet = int(bet)
#             if bet>balance:
#                 print("😞SORRY u can't bet more than ur balance")
#             elif bet<=0:
#                 print("😞SORRY u can't bet less than is zero")
#             else:
#                 balance-=bet
#                 print("       Spinning.....      ")
#                 time.sleep(1)
#                 op=play()
#                 if op == True:
#                     print(result)
#                     time.sleep(1)
#                     print("🥳🎉🎉🎉JACKPOT🎉🎉🎉🥳")
#                     balance+=bet*10
#                     print(f"YOUR balance ${balance}")
#                 else:
#                     time.sleep(1)
#                     print(result)
#                     print("💔BETTER LUCK NEXT TIME💔")
#                     print(f"YOUR balance ${balance}")
#             wish=input("do u want to play again (y/n)?").lower()
#             if wish!="y":
#                 print("🧰THANKS FOR PLAYING🧰")
#                 break
#     else:
#         topup()
# globals()[input("enter START to play: ").lower()]()

##________________________________________________________________________________________________________________________
##class and objects(OOPS)


# class Car:  #this is class
#     def __init__(self, brand, color):
#         self.brand = brand   # belongs to THIS object
#         self.color = color
#
#     def show(self):
#         print(f"My car is {self.color} {self.brand}")
#
# car1 = Car("BMW", "Black") #car1 is object and arguments inside Car is attributes
# car2 = Car("Audi", "Red")
#
# car1.show()   # My car is Black BMW
# car2.show()   # My car is Red Audi

"""diff b/w fun and class 
    class can remember the data stored but fun() can't 
    when object is created it store the data until we delete the object"""
# def greet(name):
#     return f"Hello {name}!"
#
# print(greet("Ram"))
# print(greet("Shyam"))
# print(greet("Ram"))   # It doesn't remember Ram, you must pass it again
#
# class Greeter:
#     def __init__(self, name):   # store the name once
#         self.name = name
#
#     def greet(self):
#         return f"Hello {self.name}!"
#
## Create objects
# ram = Greeter("Ram")
# shyam = Greeter("Shyam")
#
# print(ram.greet())
# print(shyam.greet())
# print(ram.greet())  # Ram is remembered without passing name again

##COOLI CLASS

# class Cooli:
#     cooli_info = {}
#     def __init__(self,name, cooli_no ,salary, age):
#         self.Cooli_name=name
#         self.Cooli_no=cooli_no
#         self.Cooli_salary=salary
#         self.Cooli_age=age
#         Cooli.cooli_info[self.Cooli_no]=self
#
#     @classmethod
#     def update(cls,name,cooli_no,salary,age):
#         if cooli_no not in Cooli.cooli_info:
#             Cooli(name, cooli_no, salary, age)
#             return f"Cooli name {name} cooli:no {cooli_no} was added in simon's data  base"
#         else:
#             return "this cooli info already exist "
#
#     def call(cooli_no):
#         if cooli_no in Cooli.cooli_info:
#             return f"Cooli no: {cooli_no} was asked to come to simon's room"
#         else:
#             return "cooli doesn't exist in simon's data"
#
#     @classmethod
#     def hire(cls,name,age,salary,cooli_no):
#         cls.update(name,cooli_no,salary,age)
#
#     @classmethod
#     def fire(cls,cooli_no):
#         name=Cooli.cooli_info.pop(cooli_no).Cooli_name
#         if cooli_no in Cooli.cooli_info:
#             name = Cooli.cooli_info.pop(cooli_no).Cooli_name
#             return f"Cooli {name} was fired by Simon"
#         else:
#             return "Cooli doesn't exist"
#
# print("1-Update cooli info\n2-Call cooli\n3-Hire a cooli\n4-Fire a cooli\n5-Save and Exit")
#
# def cooli_opp(num):
#     match num:
#         case "1":
#             C=Cooli.update(name=input("cooli name: "),
#             cooli_no=input("cooli no: "),
#             salary=input("cooli salary: "),
#             age=input("cooli age: "))
#             print(C)
#         case "2":
#             C=Cooli.call(cooli_no=input("cooli no: "))
#             print(C)
#         case "3":
#             C=Cooli.hire(name=input("cooli name: "),
#             cooli_no=input("cooli no: "),
#             salary=input("cooli salary: "),
#             age=input("cooli age: "))
#             print(C)
#         case "4":
#             C=Cooli.fire(cooli_no=input("cooli no: "))
#             print(C)
#         case "5":
#             print("thank you simon ")
#         case _:
#             print("simon thank you")
#             exit()
#     cooli_opp(num=input("anything else i want to help u: "))
# cooli_opp(num=input("simon how can i help u: "))



##MULTILEVEL INHERITANCE CLASS we create one class, and we inherit the parent class
'''i made this shit to work haa haa i made this shit'''
# class teacher_data:
#     def __init__(self,name,lpu_id,subject=None):
#         self.name=name
#         self.id=lpu_id
#         self.subject=subject
# class student_data:
#     def __init__(self,name,lpu_id):
#         self.name=name
#         self.id=lpu_id

# """Note:here teacher_data have 3 arg and student_data have 2 arg so  u should give teacher_data first
#     or else if u give 3 arg student_data gives error """

# class holiday(teacher_data,student_data):
#     def holiday_over(self):
#         print(f"{self.name} your holiday is over")
#     def holiday_start(self):
#         print(f"{self.name} your holiday is start")
# class classes(holiday):
#     def cls_start(self):
#         print(f"{self.name} your class gonna start")
#     def cls_end(self):
#         print(f"{self.name} your class gonna end, move fast to next class")
#     def leave_clg(self):
#         print(f"{self.name} you can leave the collage, thank you")

# s_t = input("enter student/teacher(s/t): ")
# if s_t == "t":
#     S_name = input("teacher name: ").strip()
#     globals()[S_name] = classes(S_name, int(input("ID: ").strip()), input("Enter subject: ").strip())

# else:
#     S_name = input("student name: ").strip()
#     globals()[S_name] = classes(S_name,int(input("ID: ").strip()))

# while True:
#     exec(input("what u wanna inform: "))
#     if input("do you wanna to inform anything else(Y/N): ").lower() not in ("yes","s","y","1"):
#         break

##super() help in inheritance of class even inheritance is possible without it
# class info:
#     def __init__(self,name=None,phone_num=None,email_id=None,employee_id=None,age=None,marital_status=None):
#         self.name=name
#         self.phone_num=phone_num
#         self.email_id=email_id
#         self.employee_id=employee_id
#         self.age=age
#         self.marital_status=marital_status
# class personal_info(info):
#     store = {}
#     def __init__(self,name,phone_num,age,marital_status):
#         super().__init__(name,phone_num,age=age,marital_status=marital_status)
#         #use keyword arg because age and marital status is not 3rd and 4th argument
#         personal_info.store["name"]=name
#         personal_info.store["Phone num"]=phone_num
#         personal_info.store["age"]=age
#         personal_info.store["marital_status"]=marital_status
#     def ret_info(self):
#         print(f"Name:{self.name}\nPhone_no:{self.phone_num}\nage:{self.age}\nmarital_status:{self.marital_status}")
# class professional_info(info):
#     def __init__(self,name,phone_num,email_id,employee_id,age):
#         super().__init__(name,phone_num,email_id,employee_id,age)
#         personal_info.store["name"] = name
#         personal_info.store["Phone num"] = phone_num
#         personal_info.store["age"] = age
#         personal_info.store["Email id"] = email_id
#         personal_info.store["Employee id"] = employee_id
#     def ret_info(self):
#         print(f"Name:{self.name}\nPhone_no:{self.phone_num}\nemail_id:{self.email_id}\nemployee_id:{self.employee_id}\nage:{self.age}")
# ui=input("(personal/professional): ")
# if ui=="personal":
#     info=personal_info(name=input("enter name:"),
#                 phone_num=input("enter phone number:"),
#                 age=input("enter age:"),
#                 marital_status=input("enter marital status:"))
#     info.ret_info()
# else:
#     info=professional_info(name=input("enter name:"),
#                            phone_num=input("enter phone number:"),
#                            age=input("enter age:"),
#                            email_id=input("enter email_id:"),
#                            employee_id=input("enter employee id:"))
#     info.ret_info()


'''Abstract methods exist to enforce a contract (rule).'''

# from abc import ABC, abstractmethod 
# #helps to make a class where it's bluprint of all sub class
#
# class Animal(ABC): #Animal class is like bluprint class
#     @abstractmethod
#     def sound(self):#it is an abstract method
#         pass
#
#     def food(self): #it is not an abstract method so no need to subclass to create it
#         pass
#
#
# class Dog(Animal): #if animal class is inherited no way it should have the all abstract methods of abc class
#     def sound(self):
#         print("dog ",end='')
#         return "Bark"
#
#     def family(self):# we can also create a fun which is not in abc
#         print("it is lion family")
#
# class Cat(Animal):
#     # def food(self):
#     #     print("cat eat meat ")
#
#     def sound(self):
#         return "Meow"
#
# # class Elephant(Animal):
# #     pass   #gives ERROR because sound() is missing
#
# e = Dog()
# print(e.sound())
# e.family()

"""If a function belongs conceptually to a class,even if it doesn't need the object,we keep it inside that class."""
class MathModule:

    @staticmethod
    def is_even(num):
        return num%2==0


'''DUCK TYPING “If it walks like a duck and quacks like a duck, it’s a duck.” means car doesn't an animal but 
it has a sound function like animals so it will be also treated like animal class until it have sound 
'''
# class Dog:
#     def sound(self):
#         return "Bark"
#
# class Cat:
#     def sound(self):
#         return "Meow"
#
# class Human:
#     def sound(self):
#         return "Hello!"
#
# class car:
#     def sound(self):
#         return "horn"
#
# # Duck typing function
# def make_sound(obj):
#     for sound in obj:
#         print(sound.sound())
#
# sound =[Dog,Cat,Human,car]
# make_sound(sound)



"""magic methods(__init__,__str__,__eq__,__lt__,__gt__,__add__,__contains_,__getitem__)"""
# class Book():
#     def __init__(self, b_name , a_name):
#         self.book=b_name
#         self.author=a_name
#     def __str__(self):
#        return f"{self.book.capitalize()} is written by {self.author.capitalize()}"
#     def __eq__(self,other):
#         return self.author == other.author 
# o1=Book("the lion king","j.k.rowlling")
# o2=Book("Harry Potter","j.k.rowlling")
# print(o1)
# print(o2)
# if o1==o2:
#     print(f"{o1.book} and {o2.book} is written by same author {o1.author}")
# else:
#     print(f"{o1.book} and {o2.book} is written by different authors")


'''A decorator is just a function that adds extra features to another function without changing its actual code.'''
# class Student:
#     def __init__(self, id):
#         self._id = id

#     @property #this is decorator this make this function as a property object variable 
#     def id(self):
#         return self._id
    
#     @id.setter
#     def id(self,val):
#         self._id = val
# s = Student(101)
# s.id = 200 #this works because we have use setter 
# print(s.id)
##________________________________________________________________________________________________________________________

## Error handling  we handle runtime error 
'''3 types of Error {compile time error} like wrong syntax , 
    {runtime error} when it get error while runing not while compiling
    syntax is right but some interruption while  running, 
    {logical} when user use wrong logic in place of + - like user side logic mistake
'''

# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Not enough balance")
#     print(balance - amount)
# a=int(input("Balance >"))
# b=int(input("Amount >"))
# withdraw(a,b)

# try:
#     x = int(input("input >"))
# except ValueError as e: # e is exception object
#     print("Error:", e)

# file = None
# try:
#     file = open("password.txt", "r")

# except Exception as e:
#     print("Handled error:", e)

# finally:
#     if file:
#         file.close()  # always runs


##________________________________________________________________________________________________________________________

## File Handling

## Opening Files - Different Modes
# 'r'  - Read (default) 
# 'w'  - Write (overwrites existing)
# 'a'  - Append
# 'x'  - Exclusive creation (fails if exists)
# 'r+' - Read and Write
# 'w+' - Write and Read (overwrites)
# 'a+' - Append and Read
# 'b'  - Binary mode (rb, wb, ab)
# 't'  - Text mode (default)

'''w,a,x,w+,a+ these are the mood create new file if it doesn't exist'''


## Read mode ##

# f = open('example.txt', 'r')
# content = f.read()
# print(content)
# f.close()
'''if file is not colsed at the end we can't open the file again pops error '''


''' with open method close the file automatically '''
# with open('example.txt', 'r') as f:
#     content = f.read()
#     print(content)


''' Different operations done in read '''
# with open('example.txt', 'r') as f: 
    
    # content = f.read(10) #read first ten characters 
    # print(content)

    # line1 = f.readline() # read one line at a time
    # line2 = f.readline()
    # print(line1, line2)

    # lines = f.readlines() #read all and make all line in list one element in that is one line 
    # for i in lines:
    #     print(i.strip()) # strip() remove extra space before and after a string 

## Write mode ##

# f = open('example.txt', 'w') #creates a new file if doesn't exist
# f.write('Hello World\n')
# f.write('Second line')
# f.close()

# with open('output.txt', 'w') as f:

    # f.write('First line\n') # '\n' creates a new line or else everything will be written in same line 
    # f.write('Second line\n')

    # lines = ['Line 1\n', 'Line 2\n', 'Line 3\n','Line 4\n']
    # f.writelines(lines) # take lsit a input write elements 

## Append mode ##

# with open('output.txt', 'a') as f:
#     f.write('Appended line\n') # it write the data in the file without rewritting the entire file

## seek() , tell()

# with open('example.txt', 'r') as f:
#     print(f"Position: {f.tell()}") # tell's the position of the cursor in the file 
#     f.seek(5) # change the cursor position
#     print(f"Position: {f.tell()}")

##________________________________________________________________________________________________________________________
print("Revision Completed")
