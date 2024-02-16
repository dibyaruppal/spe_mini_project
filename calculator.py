import math

def factorial_function(x):
    if(x<0):
        return 0
    res = 1
    for i in range(2,x+1):
        res *= i
    return res

def square_root_function(x):
    return math.sqrt(x)

def logarithm_function(x):
    return math.log(x)

def power_function(x,y):
    return x**y

def main():
    while(1):
        operation = int(input("Enter any of the following number :\n1. For Square Root\n2. Factorial\n3. Natural logarithm\n4. Power\n5. Exit\n\nEnter you number :"))
        if operation == 1:
            try:
                num = float(input("\nEnter a number :"))
                ans = square_root_function(num)
                print("The square root of the entered number :"+str(ans))
            except:
                print("An exception has been thrown !!")
        elif operation == 2:
            try:
                num = int(input("\nEnter a number :"))
                ans = factorial_function(num)
                print("The factorial of the entered number :"+str(ans))
            except:
                print("An exception has been thrown !!")
        elif operation == 3:
            try:
                num = float(input("\nEnter a number :"))
                ans = logarithm_function(num)
                print("The natural logarithm of the entered number :"+str(ans))
            except:
                print("An exception has been thrown !!")
        elif operation == 4:
            try:
                num = float(input("\nEnter a number :"))
                power = float(input("Enter power to be raised :"))
                ans = power_function(num,power)
                print("The "+str(power)+"th power of the entered number :"+str(ans))
            except:
                print("An exception has been thrown !!")
        else:
            exit(0)

if __name__ =='__main__':
    main()