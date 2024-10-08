#Analyse the code below before executing it. What will be the output ? Why ?

class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome==True:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')


foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
# Woow this is an awesome book
foundation.present()
# Title: Asimov 
print(foundation.price)
# 5£
print(foundation.bored)
# False
boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
# I am very bored
print(boring_book.bored)
# True
