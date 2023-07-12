class library:
   

    def printbooks(looks):
      num=len(looks)
      print(f"library has {num} books")
      print("They are ",looks)


    def addbooks(string,books):
      books.append(string)
      print(books)
      

    def getnum(name,books):
       for i,boo in enumerate(books):
          if name==boo:
             print(f"the number of {name} is {i}")
       return
    print("this book is not in the library")   
          
books = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "Pride and Prejudice by Jane Austen",
    "The Great Gatsby by F. Scott Fitzgerald",
    "The Catcher in the Rye by J.D. Salinger",
            ]
user_input = int(input("1.would you like to see all the books.\n2.add a book in the collection.\n3. get the number of the book so its easy for you to find.\npress 1 ,2,3 respectivley :"))
if user_input==1:
   library.printbooks(books)
elif (user_input==2):
   ring=input("the name of the book you want to add :")
   library.addbooks(ring,books)
elif(user_input==3):
   name=input("enter the name of the book you want the number of  :")
   library.getnum(name,books) 
