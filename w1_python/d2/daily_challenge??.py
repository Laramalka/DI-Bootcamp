import random #although it's for the last question, we import on top

#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

string = input('Give me a word: ')
if len (string) < 10:
    print('string too short')
elif len (string) > 10:
    print('string too long')
else:
    print('perfect sting')

#Then, print the first and last characters of the given text.

print(string[0])
print(string[-1])

#Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

word = string
begin_word = ''## This variable will begin empty and store the progressively built string
for char in (word):
    begin_word += char
    print(begin_word)

#Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
# 1. convert our string to a list
string_list = list(string)
print(string_list)

# 2. Shuffle the list
random.shuffle(string_list)
print(string_list)

# 3. turn it back into a string
shuffled = ''.join(string_list)
print(shuffled)




