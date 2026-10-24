num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 <= num2 <= num3 or num2 <= num1 <= num3:
    print(num3)

elif num3 <= num2 <= num1 or num2 <= num3 <= num1:
    print(num1)
