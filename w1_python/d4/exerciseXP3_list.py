#Using this list;
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

#Remove “Banana” from the list.
basket.pop(0)
print(basket)

#Remove “Blueberries” from the list.
basket.pop(-1)
print(basket)

#Add “Kiwi” to the end of the list.
basket.append('kiwi')
print(basket)

#Add “Apples” to the beginning of the list.
basket.insert(0, 'Apples') #The insert() method is a built-in list method in Python that allows you to add an item at a specific index
print(basket)

#Count how many apples are in the basket.
count_apples = basket.count('Apples')
print(count_apples)

#Empty the basket.
basket.clear()
#Print(basket)
print(basket)