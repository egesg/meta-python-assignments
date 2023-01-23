class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book) 

whodunnit = MyFirstClass()

whodunnit.hand_list("Sun Tzu", "The Art of War")
whodunnit.hand_list("Plato", "Republic")

# Who wrote this?

# Author-Book
# Sun Tzu wrote the book: The Art of War
# 
# Author-Book
# Plato wrote the book: Republic