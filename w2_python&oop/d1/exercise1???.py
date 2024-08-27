#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call

def sum_and_subst(num1, num2):
    sum1 = num1 + num2
    subst = num1 - num2
    return sum1, subst

result = sum_and_subst(10,5)
print(result)
