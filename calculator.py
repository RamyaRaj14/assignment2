while True:
    print("MY CALC")
    print("====")
    print("1. To find Add")
    print("2. To find Sub")
    print("3. To find Mul")
    print("4. To find Div")
    print("0. To Exit")
    operation=int(input("Please Choose Operation:"))

    if operation==1:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        add=num1+num2;
        print("Result:",add)
    elif operation==2:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        sub=num1-num2;
        print("Result:",sub)
    elif operation==3:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        mul=num1*num2;
        print("Result:",mul)
    elif operation==4:
        num1=int(input("Enter 1st Number:"))
        num2=int(input("Enter 2nd Number:"))
        div=num1/num2;
        print("Result:",div)
    elif operation==0:
        print("Exit")
        break
    else:
        print("Please choose correct operation")
    x=input("Do you want to continue yes or no")
    if x!='yes':
        print("exit")
        break