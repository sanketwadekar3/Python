class BookStore:
    NoOfBooks = 0
    def __init__(self, name, author):
        self.name = name
        self.author = author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def display(self):
        print(self.name+" by "+self.author+". "+"No of Books ",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.display()

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.display()

if __name__ == '__main__':
    main()

