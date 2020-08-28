#to find largest among three numbers
num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))
num3 = int(input("Enter a number :"))
if num1 > num2 :
    print(" {} is largest ".format(num1))
if num2 > num3 :
    print("{} is largest ".format(num2))
elif num3 > num1 :
    print("{} is largest".format(num3))


