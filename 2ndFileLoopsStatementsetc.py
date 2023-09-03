"""
inputting and outputting:
    
########input:######################################################
        variable=input("string for user understanding")


"""
a=input()
a=input("Enter your name:-")
a=input("Enter a number:-")

#by defualt type of input is string

# when we input a number we requires it to be in integer format.

#type casting ()

#variable=type(vairbale to transform)

#type: int,float,str

c=int(a)

a=int(input("Enter a number:-"))


a,b=20,40

#############outputting########################################

print("string to print",varibale,"add more string")

print(a,"the output of a and b is.",a,b)


Examples to do:
    addition of five number
    multiplication of two number
    divide two numbers and print the solution.    
    degree into farenhiet
    km into miles,feet,meter,cm
    rectangle breadth/height  area.

find average  of 5 number:
    
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
e=int(input("enter fifth number"))

res=a+b+c+d+e

res=res/5

print("the average of five number is: ",res)

    



#these are the methods in print ::::use of end and sep
print("hello")
print("world")

print("hello",end=' ')
print("world")

print("hello","world")

print("hello","world",sep='*')

      
#for writing something in between a string.
a=10
b=20
print("the value of a is", a," and the value of b is",b)


#format / %(%d,%s,%f)    (Place holders)

print("the value of a is {0} and the value of b is {1}".format(a,b))

print("the value of a is %d and the value of b is %d"%(a,b))


#if we wants to make a list by having the values from user.


a=[]
a.append([])
a[0].append(int(input("Enter first value")))
a[0].append(int(input("Enter second value")))
a.append([])
a[1].append(int(input("Enter third value")))
a[1].append(int(input("Enter fourth value")))


#Write down a program to take two metrics from the user and make them add/subtract
#write down a program to take two metrics from the user and make them multiply.

################loops#########################################

#we use it to repeat a task
#finite(Brush your teeth) & infinite(ATM machine process)

#finite:
for loop:    #Countable loop.
    
    Syntax: 
        
    for variable in groupOfelements:
        body of loop
    loop ended
    
a=[4,54,6,6,44,53,434,46]
for i in a:
    print(i)

a=[4,54,6,6,44,53,434,46]

for i in a:
    print(i)
    if(i==44):
        break #to take our program execution from inner most loop

a=[4,44,6,6,44,53,434,46]
for i in a:
    if(i==44):
        continue #if continue statement execute program will left this iteration and start with the next one
    print(i)

for i in enumerate(a):
    print(i)
    
###########################countable loop: 


for i in range(10):
    print(i)

for i in range(2,10):
    print(i)
    
for i in range(3,31,3):
    print(i)

#using above method make a program for writing the table of anything. Trust: 6 lines.

while loop: conditional loop
    
    while(condition):
        body of while loop
        
a=0
while(a<5):
    print("hello")
    a=a+1
    
    
#infinite loop:
    while(1):
        print("hello")

    while(True):
        print("hello")


#2D list a and b. You have to add them both.        
#any of the process every process normally contain two parts one part which will going to execute for one time and one part which will going to execute infinite times.


a=[]
count=1
for j in range(5):
    a.append([])
    for i in range(5):
        a[j].append(int(input("Enter {0} value".format(count))))
        count+=1


a=[]
count=0
number=['first','second','third','fourth']
for j in range(2):
    a.append([])
    for i in range(2):
        a[j].append(int(input("Enter {0} value".format(number[count]))))
        count+=1



#loops:

a=[]
for j in range(2):
    a.append([])
    for i in range(2):
        a[j].append(int(input("Enter row value:-")))
        
        

##################conditional statments#########################################
#whenever we have to write something according to a defined condition then we can use statements.

if(condition):
    body of if
elif(condition):
    body of else if
else:
    body of else
statewments ended


a=int(input("enter a number "))
if(a==0):
    print("the value of a is 0")
elif(a==20):
    print("the value of a is 20")
elif(a==30):
    print("the vlaue of a is 30")
else:
    print("wrong value entered")


nested part:
    if(condition):
        if(condition):
            nested if body inner if
        outer if body
    both if statmenet ended.

a=20
b=40
if(a==20):
    if(b==40):
        print("both value satisfied") #task which you want to perform

# check weather a number is even or odd.
# Create a password authentication system.
# Check leap year
# Finding the largest number among three numbers.
# checking number whether it is prime or not
# Find a prime number from a series. Loops/Condition statement.
# Check number if it is positive or negative
# Program to create a calculator.
# Project: Office management system. different employee of the company if needs to enter they have to put their login credentials. welcome name. In into the office.
        
        
##########################string###################################

a="hello world" #'hello world'
len(a)
type(a)
a[1]
a[1:4]

#special methods in string
a.capitalize()
a.count('l')
a.index('w')
a.upper()
a.lower()
a.islower()
a.isnumeric()

a=[5,3,5,67,4,3,5,6]
b=[]
for i in a:
    b.append(str(i))

c=' '.join(b)

c.split()

#######################function####################################
#these are the building block of a program which reduces it length and complexity and makes error detection easy.
#program: 10 task. task wise program split

Parts of a function:
    Function declaration where we declare our function by giving its name
    Function defination here we write the body of a function
    Function call we call our function


def function_name(variable):     #declaration part of a function
    body of the function         #defination part of a function

function_name(argument)          #function call

Program: 
    
    1000 lines
    
    1
    
    
    
    
    
    
    
    
    1000


fine : in future I have to make some modification in task4 (complexity is high)



    t1 250
    t2 100  
    t3  50
    t4     task of machine
    t5
    t6



length?


30 lines are repoeating in t1,t2,t3,t4

    t1 250       30
    t2 100       30
    t3  50       30
    t4           30
    t5
    t6

120 lines

function t10 (30 lines)

    t1  call 1 line
    t2  call 1 line 
    t3  call 1 line
    t4  call 1 line 
    t5
    t6


30+1+1+1+1=34


error detection easy???


complete code without functions
    1
    
    modification in line 400:::::linked with other lines of the program.
    
    1000


    t1 250       
    t2 100       
    t3  50       
    t4            200 lines modification:::::::t4 is indirectly related to other task.
    t5
    t6




syntax:

def functionName(variables):    #declaration of function
    body of function    #defination of function
 
functionName(argument)  #calling of function


#function without argument
def fun():
    print("this is the part of a function")

fun()


#function with argument.
def fun(a,b):
    print("this is the part of a function",a,b)    # 3 times: 15 lines:   5+1+1+1=8

fun(35,23) 


def fun(a=None,b=None):
    print("this is the part of a function",a,b)    # 3 times: 15 lines:   5+1+1+1=8

fun() 
fun(10)
fun(10,20)

def fun(a=None,b=None):
    print("this is the part of a function",a,b)    # 3 times: 15 lines:   5+1+1+1=8
    return 321

var=fun(23) 


def fun(a):
    print("this is the part of a function",a)
    return 20,12

c,b=fun(20)



def fun():
    a=int(input("Enter 1 no")) #defining a variable  in a function so it will be a local variable. So we cannot access this variable outside the function
    b=int(input("Enter 2 no"))
    c=int(input("Enter 3 no"))  
    d=int(input("Enter 4 no"))
    e=int(input("Enter 5 no"))
    f=int(input("Enter 6 no"))
    return a,b,c,d,e,f


a1,b1,c1,d1,e1,f1=fun() 
avg=(a1+b1+c1+d1+f1+e1)/6
print("the average of six number is:-",avg)



def fun():
    global i
    i+=1
    return(int(input("Enter {0} no ".format(i))))
i=0
num=[]
for dd in range(6):
    num.append(fun()) 
avg=(num[0]+num[1]+num[2]+num[3]+num[4]+num[5])/6   #not a good method.
print("the average of six number is:-",avg)



lambda function: when we have to write very small defination of a program its best to use lambda

syntaX:
   object=lambda variables: operation to perform
    
    
    
def addition(x,y):
    z=x+y
    return z
op=addition(10,20)


obj=lambda x,y:x+y
res=obj(10,20)


a=0
b=[]
while(a<5):
    b.append(int(input("Enter a number ")))
    a=a+1


#Practice matrix operations. Additiion/multiplication/subtaction

a=[]
count=1
for j in range(5):
    a.append([])
    for i in range(5):
        a[j].append(int(input("Enter {0} number ".format(count))))    
        count+=1



    
*5 by 5 matrix
a=[]
a.append([])
a[0].append(int(input("Enter 1 number ")))    
a[0].append(int(input("Enter 2 number ")))    
a[0].append(int(input("Enter 3 number ")))    
a[0].append(int(input("Enter 4 number ")))    
a[0].append(int(input("Enter 5 number ")))    
a.append([])
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a.append([])
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a.append([])
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a.append([])
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
a[1].append(int(input("Enter 4 number ")))    
a[1].append(int(input("Enter 3 number ")))    
 





a=[]
for j in range(6):
    a.append([])
    for i in range(6):
        a[j].append(int(input("Enter {0} number ".format(i+1))))    

