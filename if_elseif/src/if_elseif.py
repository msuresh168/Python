'''
Created on 30-Jul-2017

@author: Suresh
'''
from builtins import input


print("Hello World!\n")

while True: 
    
    print("Enter 'x' for Exit. ")
    print("Enter any number: ")
    value = input()

    if (value=='x') : 
        print("Value of expression is x")
        print(value)
        print("Exit\n")
        break 

    print("if-else Condition")
    print("--------------------")
    if(int(value)==1):
        print("Value of expression is 1")
        print(value) 
    elif(int(value)==2):
        print("Value of expression is 2")
        print(value)
    elif(int(value)==3):
        print("Value of expression is 3")
        print(value)
    print("Thank you\n")


    print("Nested if-else Condition")
    print("---------------------------")
    if(int(value)<=3):
        if(int(value)==1):
            print("Value of expression is 1")
            print(value)
        elif(int(value)==2):
            print("Value of expression is 2")
            print(value)
        elif(int(value)==3):
            print("Value of expression is 3")
            print(value)    
    else:
        print("Value of expression is not less than 3")
        print(value)
    print("Thank you\n")
    
