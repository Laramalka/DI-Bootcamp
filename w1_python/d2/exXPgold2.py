#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

month = int(input('Give me a a month by its number 1-12: '))

if month == 3 or month == 4 or month == 5:
    print('This is spring')
elif month == 6 or month == 7 or month == 8:
    print('this is summer')
elif month == 9 or month == 10 or month == 11:
    print('this is autumn')
else:
    print('this is winter')