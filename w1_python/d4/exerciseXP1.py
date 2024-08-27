#Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = [3,7,9,18]
my_fav_numbers.append(17)
my_fav_numbers.append(36)
print(my_fav_numbers)

#Remove the last number.
my_fav_numbers.pop(-1)
print(my_fav_numbers)

#Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = [5, 78, 54]

#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

#Add two new numbers to the set.
our_fav_numbers.append(108)
our_fav_numbers.append(26)

print(our_fav_numbers)

