import math 
operation=input("What operation would you like to do?(+,-,*,/,power,radical,sin,cos)")
if operation in ("+","-","*","/","power","radical","sin","cos"):
    #-------------------------------------------------------
    if operation=="+":
        num1=input("What is your first number?")
        try:
            float(num1)
        except:
            print("Your first number is not valid")
            exit()
        num2=input("What is your secound number?")
        try:
            float(num2)
        except:
            print("Your secound number is not valid")
            exit()
        print(float(num1)+float(num2))
    #-------------------------------------------------------
    if operation=="-":
        num1=input("What is your first number?")
        try:
            float(num1)
        except:
            print("Your first number is not valid")
            exit()
        num2=input("What is your secound number?")
        try:
            float(num2)
        except:
            print("Your secound number is not valid")
            exit()
        print(float(num1)-float(num2))
    #-------------------------------------------------------
    if operation=="*":
        num1=input("What is your first number?")
        try:
            float(num1)
        except:
            print("Your first number is not valid")
            exit()
        num2=input("What is your secound number?")
        try:
            float(num2)
        except:
            print("Your secound number is not valid")
            exit()
        print(float(num1)*float(num2))
    #-------------------------------------------------------
    if operation=="/":
        num1=input("What is your first number?")
        try:
            float(num1)
        except:
            print("Your first number is not valid")
            exit()
        num2=input("What is your secound number?")
        try:
            float(num2)
        except:
            print("Your secound number is not valid")
            exit()
        print(float(num1)/float(num2))
    #-------------------------------------------------------
    if operation=="power":
        num1=input("What is your number?")
        try:
            float(num1)
        except:
            print("Your number is not valid")
            exit()
        num2=input("To the power of?")
        try:
            float(num2)
        except:
            print("Your secound number is not valid")
            exit()
        print(math.pow(float(num1),float(num2)))
    #-------------------------------------------------------
    if operation=="radical":
        num1=input("What is your number?")
        try:
            float(num1)
        except:
            print("Your number is not valid")
            exit()

        num2=input("What is your index?")
        try:
            float(num2)
        except:
            print("Your secound number is not valid")
            exit()
        if float(num1)<0 :
            if (float(num2) % 2==0):
                print("ERROR:You cant put a negetive number in a radical when the index is even.")   
                exit()         
        print(float(num1)**(1/float(num2)))        
    #-------------------------------------------------------
    if operation=="sin":
        num=input("What is your number?")
        try:
            float(num)
        except:
            print("Your first number is not valid")
            exit()
        print(math.sin(math.radians(float(num))))
    #-------------------------------------------------------
    if operation=="cos":
        num=input("What is your number?")
        try:
            float(num)
        except:
            print("Your first number is not valid")
            exit()
        x = math.cos(math.radians(float(num)))   
        if abs(x) < 1e-15 :
            x = 0
        print(x)       
    #-------------------------------------------------------     
else:
    print("ERROR:The operation is not valid.")    