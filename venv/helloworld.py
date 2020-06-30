from math import *
from moduletest import reading

def say(something):
    print(something)

def animal(type):
    if(type=="dog"): print("bark bark")
    elif(type=="cat"): print("mew mew")
    else: print("i am no animal")

def loremislum(name, age):
    print("my name is "+name)
    print("and i am "+ str(age) + " year olds")

def counting(words):
    print(len(words))

def getindex(somestring, index_char):
    print(somestring.index(index_char))

def getreplace(somestring,old_char,replace_char):
    print(somestring.replace(old_char,replace_char))

def numberUp(number):
    print(ceil(number))

def numberDown(number):
    print(floor(number))

def inputst():
    name = input(" Insert your age here: ")
    print(age + 19)

def caculator():
    number1 = input(" Type in number 1: ")
    number2 = input(" Type in number 2: ")
    result = float(number1) + float(number2)
    print(result)

def madword():
    object = input("object:")
    color = input("color:")
    person = input("person:")
    print("my " +object+ " has bad smell")
    print("today, my "+color+" candy is stinky")
    print("i think "+person+" love me")

def getallchar(char):
    for a in char: print(a)

def getalllist():
    a = ["cuong","anh","duyen","nam"]
    # for index in a: print (index)
    for index in range(len(a)): print (a[index])

def getprimarynumber():
    for number in range(1,50):
        for primary in range(2,number):
            if(number % primary == 0):
                othernumer = number/primary
                print("%d = %d*%d" %(number,primary,othernumer))
                break
            else:
                print(str(number) + " is a primary number")
                break

def list():
    a = ["leduccuong",1998,"bacgiang"]
    print(a)
    a[2] = "hanoi"
    print(a)
    a[2] = [99,88,77]
    print(a)

def tuples():
    a = ("leduccuong",1998,"bacgiang")
    b = ("lethuyduyen",)
    print(a)
    print(a[1])
    print(a+b)

def dictionary():
    a = {'leduccuong':1998, 'lethuyduyen':1997, 'ngongocanh':1998}
    print("a[1]:"+ str(a['lethuyduyen']))

    a[(99,88,99)]=1996
    a[1998]='sinh nhat'
    print(a)
    a['lethuyduyen']= [1998,1997,23/8]
    print(a)

def changeme(mylist):
    print(mylist)

def usemodule():
    reading("kekeke")

def bubblesort(list):
    max = len(list)
    for a in range(0, max-1):
        for b in range(0,max-a-1):
            if(list[b]>list[b+1]):
                list[b],list[b+1] = list[b+1],list[b]
                print(list)
    print(list)

def tuple():
    p =('a','b')
    print(3*p)

bubblesort(list = [999,6,7,2,15,99,21])
tuple()