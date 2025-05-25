import os
import wikipedia

class library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.books = self.loadBooks()

    def loadBooks(self):
        if not os.path.exists(self.file_name):
            default_books = ["DSA", "Python", "C", "DAA", "DBMS"]
            with open(self.file_name, "w") as f:
                for book in default_books:
                    f.write(book + "\n")
            return default_books
        else:
            with open(self.file_name, "r") as f:
                return [line.strip() for line in f.readlines()]

    def saveBooks(self):
        with open("book.txt", "w") as f:
            for book in self.books:
                f.write(book + "\n")

    def bookSummary(self, name):
        if name in self.books:
            # Mapping short names to proper Wikipedia titles
            topic_map = {
                "DAA": "Design and analysis of algorithms",
                "DSA": "Data structure and algorithm",
                "DBMS": "Database management system",
                "OOP": "Object-oriented programming"
                # Add more if needed
            }

            # Use mapped topic if exists, else use user input directly
            search_topic = topic_map.get(name, name)

            try:
                summary = wikipedia.summary(search_topic, sentences=4)
                print(f"\n📚 Summary for '{search_topic}/{name}':\n{summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"⚠️ Topic '{search_topic}' is ambiguous. Try one of these: {e.options[:3]}")
            except wikipedia.exceptions.PageError:
                print(f"❌ No Wikipedia page found for '{search_topic}'.")
        else:
            print("The Book is currently unavailable in Library.")


    def displayAllBooks(self):
        print("The list of books available here is:")
        for book in self.books:
            print("*",book)
        
    def borrowBook(self,name):
        if name in self.books:
            print(f"The Book name {name} has been issued to you")
            self.books.remove(name)
            self.saveBooks()
            return True
        else:
            print("This Book is not available right now!")
            return False

    def returnBook(self,name):
        self.books.append(name)
        self.saveBooks()
        print("Thanks! For returning the book")

class student:
    def requestBook(self):
        self.books = input("Enter the book name you want:")
        return self.books
    
    def sreturnBook(self):
        self.books = input("Enter the name of book you want to return:")
        return self.books

if __name__=="__main__":
    centralLibrary = library("book.txt")
student = student()


while(True):
    welcomeMsg = '''------ Welcome To Ansh Library -------
    Please Make You Choice:
    1.List of Books.
    2.Request Book.
    3.Return Book.
    4.Book Summary.
    5.To Exit.
    '''

    print(welcomeMsg)
    a = int(input("Enter your choice:"))

    if a==1:
        centralLibrary.displayAllBooks()
    elif a==2:
        centralLibrary.borrowBook(student.requestBook())
    elif a==3:
        centralLibrary.returnBook(student.sreturnBook())
    elif a==4:
        user_reply = input("Enter the Book name :")
        centralLibrary.bookSummary(user_reply)
    elif a==5:
        print("Thanks for choosing Ansh Library")
        break
    else:
        print("Invalid choice")
        