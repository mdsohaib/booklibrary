


class library:

    def __init__(self,list,name):
        self.booklist = list
        self.name  = name
        self.lendDict={}

    def displaybooks(self):
        print(f"we have following books {list} in our library {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,book,user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('you can take the book')
        else:
            print(f"the book is already taken by{self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print('Book has been added')

    def returnbook(self,book):
        self.lendDict.pop(book)


if __name__== '__main__':
    sohaib=library(['Python','Rich dad poor dad','Million dreams', 'Tom and Jerry','Hydraulics','Fluid dynamics','MEchanical engineering'], 'SohaibLibrary')

while(True):
    print(f"Welcome to {sohaib.name}. Enter your choice")

    print('1. Diplays books available')
    print('2. Lend a book')
    print('3. Add a book')
    print('4. Return a book')

    user_choice= input()
    if user_choice not in ['1','2','3','4']:
        continue
    else:
        user_choice= int(user_choice)

    if user_choice==1:
        sohaib.displaybooks()

    elif user_choice==2:
        book = input("enter the name of a book")
        user = input("enter your name")
        sohaib.lendbook(book,user)

    elif user_choice==3:
        book = input('enter the name of book')
        sohaib.addbook(book)

    elif user_choice==4:
        book = input('enter name of book which you want to return')
        sohaib.returnbook(book)

    else:
        print('not a valid option')

    print("type 'q' to quit and 'c' to continue")
    user_choice2 =""
    while(user_choice2 !='c' and user_choice2 != 'q'):
        user_choice2 = input()
        if user_choice2=='q':
            exit()
        elif user_choice2=='c':
            continue