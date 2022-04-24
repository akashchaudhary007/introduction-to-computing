
print("question no.1")
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
print("average =",(num1+num2+num3)//3)


print("question no.2")
income = int(input("Enter your income in $:"))
dependents_in_family = int(input("Enter number of dependents in your family:"))
dependent_tax_deduction = 3000
standard_deduction = 10000
tax_rate = 0.2
income_after_deduction = income - standard_deduction - (dependents_in_family * dependent_tax_deduction)
tax = income_after_deduction * tax_rate
print("tax on your income is:", tax)


print("question no.3")
a = int(input("Enter number of seconds : "))
print("It has", a // 60, "minutes and ", a % 60, "seconds")


print("question no.4")
number1 = 25
number2 = '25'
number3 = 25.0
sum = number1 + int(number2) + number3
string_sum = str(sum)
print(string_sum, type(string_sum))


print("question no.5")
import math

for i in range(0, 360, 15):
    cosine = math.cos(math.radians(i))

    sine = math.sin(math.radians(i))
    print("cosine(", i, ") is", round(cosine, 4), "           sine(", i, ") is", round(sine, 4))





