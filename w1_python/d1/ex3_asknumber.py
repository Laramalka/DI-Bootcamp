# Ask the user for a number between 1 and 100
#If the number is a multiple of three, print "Fizz"
#If the number is a multiple of five, print "Buzz".
#If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

number = int(input('Give me a nunber between 1 and 100: '))
if number % 3 == 0 and number %5 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print(number)