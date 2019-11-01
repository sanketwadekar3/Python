import Arithmetic

print("Enter first number")
num1 = int(input())

print("Enter second number")
num2 = int(input())

add = Arithmetic.Add(num1,num2)

sub = Arithmetic.Sub(num1,num2)

mul = Arithmetic.Mul(num1,num2)

div = Arithmetic.Div(num1,num2)

print("Addition is ",add)

print("Subtraction is ",sub)

print("Multiplication is ",mul)

print("Division is ",div)