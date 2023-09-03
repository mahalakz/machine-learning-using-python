"""
Programming tools   Turboc   Devc
Pycharm.
Anaconda.  Spyder(IPY environment), Jupyter
Python Idle (not recc)


To write a program we require some concepts like:
    1 virtualization of things.
    2 sequence based concept splitting. Non technical.
    3 Understand the syntax of programming and write code 
      for each module and then test and then write another module and test
    4 application should be user friendly
      
    
Add of two no:
    Module 1 Collect two numbers     scanf   c++ cin  java listner python input r readline
    Module 2 Make them add
    Module 3 Display the result on the screen.
    
"""
"""
Programming: to transfer the thoughts into a machine

    Language:
        High level ( user friendly)
        Low level  (machine friendly)
        Assembly   (mix of h+l)
        
    convertors:
        interpreter  H+L    Python, R  1,2,3(lines having error) 1 error solve  2 error solve 3 error solve it first
        compiler     H+L    C          1,2,3   1,2,3 error solve it
        assembler    A+L

    standard of conversion:
        ASCII (American standard of code and information interchange)
        a=0x61   0110 0001     0x hexadecimal, 6: 0110     8421 
        
Why Python???
    1) Syntax free language (Very easy to use)
    2) Huge number of libraries and packages. (perform any task in the simplest way)
    3) It a reference{address} based language. (c pointers)       for values updation is require.
    4) It is possible to integrate python with many hardwares and technology.(Raspberry pi)
    5) It is having a support of algorithms.
    
    
Topics:
    1) Constant
    2) Variables
    3) Operators
    4) Data Structures
    5) Input and output
    6) Loops and statements
    7) Functions
    8) Modules and packages
    9) Strings
    10) File handling
    11) Exception handling
    12) Predefined modules (pandas,matplotlib,re,webscrapping,numpy)
    
1) constant: it attains a single value.
    integers,floating numbers. 10,10.20

2) Variables: these are the memory locations where we can store our values.
    types:
        local: a=20    (defined locally in the program and this variable scope is limited.)
        global: global a       not possible to initialize it
        
a=20  #press F9   (F9+function key)      
c=40.43
b='string' 


type(b)

global a


def fun1():
    global a
    print(a)   #this line is giving this error
    a=30

a=20  #local variable
fun1()  #function calling


#Features:
    1) comment: '''multi line comment 
    for comment'''     """ """
    #single line comment
    2) scope of something: 
    c programming: 
        if(a==20)
        { 
            from here if body start
        }   if body ends
         
        in python it is done using indent block
     
         if(a==20):
             automatically tab space
             dfd
             fdg
             ffg
         start writing it means if body is ended now
    
    3) End of the line: c programs: we use semicoln(;)     
        Going to the next line automatically endup the previous one.
    4) Run: F5 you can run the complete program otherwise you can press F9 for line by line execution
    
    
3) Operators of python: These are the symbolss in the programming use for computation purpose
    a) Arithmetic operator: +,-,*,/,//,%,**    a//b=quotient
    b) Logical operator: and, or,
    c) Relational: <,>,<=,>=,==,!=
    d) Assignment operator: +=,-=,*=,&=,|=,<<=,>>=,=
    a+=1           a=a+1 
    e) Special Operators: Returns in true and false.
        1) identity operator: is, is not
        a=25
        print(a is 25)
        2) membership operator: in, not in
        a=[5,23,4,56,7,5,3,67]
        print(56 in a)
    
    
4) Data Structures:
    string: contains integer, characters and special characters (text)
    float : contains of floating numbers/decimal values.
    integer: contains integers/normal numbers without decimal
    bool
    
    Collection: (like in c we have array)
        list: ordered, indexed,duplicate are allowed, changeable             normaly
        tuple: ordered, indexed, duplicate are allowed, non changeable        
        set: unordered, unindexed, duplicate not allowed, non changeable     
        dictionary: unordered, unindexed, duplicate not allowed, changeable  big data
        array    libraries only.

list: 
    1D,2D,3D,...
    
    1D:
        listName=[elements of list]
        
        a=[4,2,54,6,8,9,6,34,56,8,9,23]
        a[2] #0 is the index position
        a[0]=234
        a[:]
        a[2:]
        a[2:5]
        a[:5]
        len(a)
        a[-1]
    2D:
        listName=[[c1,c2,c3...],[c1,c2,c3...],[c1,c2,c3...],...]
        
    5 3
    7 4
        a=[[5,3],[7,4]]
        a[1][0] #a[row][column]
        a[0][0]=45

Special methods of list:

a=[6,4,5,6,8,7,4,3,2,3,4,56,7,8,9]
a.append(123)
b=a.copy()
b.clear()
b=[8,9,0]
a.extend(b)
a.count(7)
a.index(56)
a.insert(3,123)
a.pop()
a.remove(123)
a.reverse()
a.sort()

making a list using predefined type:

name=list((elements of list))

a=list((5,32,5,6,3,2,4))
type(a)
len(a) #return the length of  your list


2) Tuple:
    1D,2D......
    
    tupleName=(elements of tuple)

a=(3,2,4,56,6,3,2,4)
type(a)    
len(a)
a[0]
a[0]=34

    tupleName=((c1,c2...),(c1,c2...),(c1,c2...),...)

a=((3,2),(5,3))
a[0][0]
a[0][0]=123


special methods of tupple:
    
a=(4,2,45,6,3,4,6,5,3,3)
a.count(4)
a.index(6)

making a tuple using predefined type:

name=tuple((elements of tuple))

a=tuple((4,2,4,56,6,3,23))


3) Set:
    setName={elements of set}
    
a={5,3,45,6,5,323,4,56,67,3}
type(a)

a[0]
a[0]=34

special methods of set:

a={5,3,5,67,2,5,32,4,5,6,3}
b={6,3,5,67,8,89,65,43,2,23}
a.add(9)
a
c=a.copy()
c.clear()
a.difference(b)
a.difference_update(b)
a.discard(5)
a.intersection(b)
a.intersection_update(b)
a.isdisjoint(b)
a.issubset(b)
a.issuperset(b)
a.pop()
a.remove(67)
a.symmetric_difference(b)
a.symmetric_difference_update(b)
a.union(b)
a.update()


writing a set using predefined type:
    
name=set((elements of set))

a=set((4,2,4,6,6,43,23))


4) Dict
    dictName={unique key:value}
    
a={'car':'audi','year':2021,'color':'white','engine':'3000cc'}
type(a)
len(a)

a['car']
a['car']='bentley'

special methods in dict

b=a.copy()
b.clear()
c=a.copy()
c.get('car')
c.values()
d=c.fromkeys('abcd')
c.keys()
c.pop('car')
c.popitem()
c.setdefault('color')
c.update()


making dict using predefined type

dictName=dict(({key:values}))

a=dict(({"car":"audi","color":"white"}))

"""




a=10
a=20.40
a="strgin"   #local variable

a=[]
a=()
a={}
a={key:value}

global variableName


def fun():
    print(a) #this line is giving an error because you have defined a local variable a with value 10.
    a=20



a=10
fun()



def fun():
    global a
    print(a) #this line is giving an error because you have defined a local variable a with value 10.
    a=20

a=10
fun()


dict:
    
sequence=[1,2,3]

data=[[10000 values],[10000 values],[10000 values]] 


data={1:[10000 values],2:[10000 values],3:[10000 values]} 


   
data[2]


application interface: windows: applicationName.exe

.py





