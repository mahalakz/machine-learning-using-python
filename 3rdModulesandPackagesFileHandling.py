"""
###############file handling######################################

#methods: open: open with a permission r,w,x,a

obj=open("file name with path with extension",'permission')

#to accesss a file through an object: 
variable=obj.read()
obj.write("content to write in the file")
obj.close()


obj=open("D:/Artificial Intelligence Batch/file.txt","w")
obj.write("This is the data which I am passing just to test my file handling")
obj.close()

obj=open("D:/Artificial Intelligence Batch/file.txt","r")
aa=obj.read()
obj.close()

############modules and packages#####################################
modules: libraries  files.py
packages: directory (folder)

types:
    userdefined
    predefined


userdefined:
"""
import mod
print(mod.a)
print(mod.b)
print(mod.c)
print(mod.fun())
"""

import mod as m
print(m.a)
print(m.b)
print(m.c)
print(m.fun())

from mod import *     
print(a)
print(b)
print(c)
print(fun())

from pkg import mod
print(mod.a)
print(mod.b)
print(mod.c)
print(mod.fun())

from pkg.mod import *
print(a)
print(b)
print(c)
print(fun())

import pkg.mod as m
print(m.a)
print(m.b)
print(m.c)
print(m.fun())


predefined modules and packages:
    1)re
    2)pandas: data manupulation
    3)matplotlib
    4)numpy
    5)sklearn(scikit-learn)


1) re:regular expression matching: search something from a document

import re
a="a hello how, are you Mr 1. 34 is the no i have. this string is written for testing. my contact no is +91-9887340701."
re.findall(r'how',a) #r is actually the raw string.
re.findall(r'h..',a)
re.findall(r'h.+',a)
re.findall(r'\d',a)
re.findall(r'\D',a)
re.findall(r'\w',a)
re.findall(r'\W',a)
re.findall(r'\s',a)
re.findall(r'\S',a)
re.findall(r'\d\d-\d\d\d\d\d\d\d\d\d\d',a)
re.findall(r'\d\d-\d{10}',a)
re.findall(r'\d\d',a)

    
import pandas as pd  #data manupulation
#df=pd.read_csv(open("filepath and extention","permission")) #r,w,rb(read in binary)
#df=pd.read_excel(open("filepath and extention","permission"))   

#the return type of pandas series is dataframe

df=pd.read_excel(open("D:/Artificial Intelligence Batch/adult_salary_dataset.xlsx","rb")) 

df.Age

#how to split my dataset. we have to extract inputs and outputs.

#returnVariable=df.iloc[row,column]
ip=df.iloc[:,:-1]
op=df.iloc[:,-1]

x=df.iloc[:,[1,4,7,5]]


#use of numpy package: this package is use for making computation more effectively.

import numpy as np
ip=np.array(ip)
op=np.array(op)
ip[:,0]
ip[0,:]

#if we have a csv file
df=pd.read_csv(open("D:/Artificial Intelligence Batch/Churn_Modelling.csv","rb")) 


3) numpy: this package is use for computation purpose
    
import numpy as np
np.add(4,3)
np.subtract(4,2)
np.multiply(5,2)
np.divide(6,3)
np.sqrt(7)
np.exp(4)
np.log(2)
a=[5,3,45,6,7,7,5,434,35,7,3]
np.sum(a)



a=[]
for i in range(5):
    a.append(int(input("enter {0} number".format(i+1))))

import numpy as np
res=np.sum(a)

res=res/5

print("the average of five number is: ",res)



a=[2,5,7,4,6,9,0,1,3,4]
b=np.reshape(a,(5,2))
np.ravel(b)

np.shape(b)

a=[2,5,7,4,6,9,0,1,3,4]
b=[6,3,5,8,9,3,2,5,6,8]
x,y=np.meshgrid(a,b)

np.linspace(1,30,10)

np.arange(1,10,0.1)


np.max(a)

np.min(a)

np.abs(-4)


#################################Matplotlib######################################

a=[2,5,7,9,6,9,0,1,3,4]  #x axis
b=[6,3,5,8,9,3,2,5,6,8]  #y axis
z=[1,1,1,1,1,0,0,2,2,2]
import matplotlib.pyplot as plt
plt.title("this is time and distance graph")
plt.xlabel("time")
plt.ylabel("distance")
plt.plot(a,b)
plt.plot(a,b,'o')
plt.plot(a,b,color='red')
plt.plot(a,b,'or')
plt.show()

plt.scatter(a,b)
plt.scatter(a,b,c=z)
plt.scatter(a,b,c=z,cmap='spring')  #autumn
plt.show()

plt.pie(a,labels=b,autopct='%0.1f')

b=[1,2,3,4,5,6,7,8,9,10]
plt.hist(a,b)   #frequency plot

plt.bar(a,b)


################################Sklearn#########################################
#this is the library we will going to use for machine learning algorithm as this library contains a 
#number of predefined modules for machine learning in python.


##############################exception handling################################
#how to deal with errors at run time.

a=int(input("Enter a number to add"))
b=int(input("enter another number to add"))
c=a+b
print("the addition of two no is:",c)


types:
    1) user defined (whose situation we will create and process)
    2) predefined (already defined in the programming)
    

    user defined:

a=10
if(a==10):
    pass
        
        Syntax:
            
class exceptionName(Exception):
    pass

try:
    write the code because of which exception requires to raise
except exceptionName:
    write down the msg which you wants to send
finally:
    this line always execute if exception occour or not occour
    

class gameMine(Exception):
    pass
try:
    a=int(input("Please enter the value less than 100 "))
    if(a>=100):
        raise gameMine
except gameMine:
    print("why you are not writing value less than 100")



class gameMine(Exception):
    pass
i=0
while(i==0):
    try:
        a=int(input("Please enter the value less than 100"))
        if(a>=100):
            raise gameMine
        i=1
    except gameMine:
        print("why you are not writing value less than 100")


   #################################### predefined:################################

        NameError
        ValueError
        ZeroDivisionError
        IOError
        EOFError
        AttributeError
        SyntaxError
        IndexError
        TypeError and many more

try:
    write the lines wqhich can create an error
except typeofException:
    print your message
finally:
    it will execute either exception occour or not.


try:
    a=int(input("Enter the number:-"))
except ValueError:
    print("please enter only number")
finally:
    print("This is the line which prints either exception occour or  nor")


aa=0
while(aa==0):
    try:
        a=int(input("Enter the number:-"))
        aa=1 #program will skip this line if exception occor.
    except ValueError:
        print("please enter only integer value")


try:
    a=int(input("Enter the number:-"))
except:
    print("Oops!!!  Something went wrong!!!!!!!")


a=[5,3,54,6,67,4]
try:
    b=int(input("Enter the index number of a from 0 to 5."))
    print("selected value from list by user is",a[b])
except IndexError:
    print("choose only the available block")
    
    
try:
    a=int(input("enter a number:-"))
except:
    print("Oops something went wrong!!!!!!!")


print(z) #give name error if a is not defined

10/0

a=int(input("Enter first number to divide "))
b=int(input("Enter second number to divide "))
try:
    c=a/b
    print("The division of two number is ",c)
except ZeroDivisionError:
    print("Enter non zero value of second varible")


Task: Addition of two number program you need to make.
Use exceptional handling if required.

You have to design a scientific calculator. (using numpy, mathematics).
"""
 
"""
a=0
b=0
c=None   
cc=0
while(cc==0):
    try:
        a=int(input("Enter first number"))
        cc=1
    except ValueError:
        print("Please enter only numbers.")
cc=0
while(cc==0):
    try:
        b=int(input("Enter second number"))
        cc=1
    except ValueError:
        print("Please enter only numbers.")
c=a+b
print("The addition of two number is :-",c)

"""


10000

100
50




