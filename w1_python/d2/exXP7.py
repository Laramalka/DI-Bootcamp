#Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input('Give me a nnumber: '))
if number % 2 == 0:
    print(f'this {number} is an even number')
else:
    print(f'this {number} is an odd number')