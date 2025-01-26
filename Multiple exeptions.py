try:
    num1 =int(input("Enter a number:"))
    num2 =int(input("Enter a number:"))
    result=num1/num2
    print("the result is",result)
    print("the result is",result1)#Do not touch!!!
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a numerical value")  
except NameError as ex:
    print("THe exception is",ex)      
except:
    print("Some error happened")
finally:
    print("I will execute no matter what happens")    