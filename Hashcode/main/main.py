days = 0

class Book(object):
    books = []

    def __init__(self, score):
        Book.books.append(self)
        self.id = len(Book.books) - 1
        self.score = score
        self.shipped = False
    



class Library(object):
    libraries = []
    
    def __init__(self, signupTime, shipMax):
        Library.libraries.append(self)
        self.id = len(Library.libraries) - 1
        self.books = []
        self.signupTime = signupTime
        self.shipMax = shipMax
        self.signedUp = False
        self.scannedBooks = []
        self.libraryScore = 0
        self.startSending = -1
        self.sendOrder = -1
    
    def addBook(self, id):
        self.books.append(Book.books[id])
    
    def calculateScore(self):
        """

            Total score of unique books in library
            How many books can be processed at the same time
            Result logged as "points per day"
        """
        self.books = sorted(self.books, key = lambda x : x.score, reverse=True)
        daysRemaining = days - self.signupTime
        totalBooksCanShip = min(daysRemaining * self.shipMax, len(self.books))
        
        count = 0
        while (totalBooksCanShip > count):
            currentBook = self.books[count]
            if (currentBook.shipped):
                count = count + 1
                continue
            self.libraryScore = self.libraryScore + currentBook.score
            count = count + 1
        
    def signup(self, sendOrder, currentDay):
        self.sendOrder = sendOrder
        self.startSending = currentDay + self.signupTime
    
    def sendBooks(self):
        for i in range(self.shipMax):
            if (len(self.scannedBooks) >= len(self.books)):
                break
            
            bookNum = len(self.scannedBooks)
            bookToSend = self.books[bookNum]
            while (bookToSend.shipped):
                bookNum = bookNum + 1
                if (bookNum >= len(self.books)):
                    return
                bookToSend = self.books[bookNum]
            self.scannedBooks.append(bookToSend)
            bookToSend.shipped = True
    



def loadData(fileName):
    global days

    f = open(fileName, "r")
    
    # Processing metadata at the top
    metaData = f.readline()
    days = int(metaData.split(" ")[2])
    libraries = int(metaData.split(" ")[1])

    # Processing book creation
    bookScores = f.readline()
    for bookScore in bookScores.split(" "):
        Book(int(bookScore))
    print("Loaded", len(Book.books), "books")

    # Processing library creation

    for i in range(libraries):
        libraryMeta = f.readline().strip("\n").split(" ")
        libraryBooks = f.readline().strip("\n").split(" ")

        currentLibrary = Library(int(libraryMeta[1]), int(libraryMeta[2]))
        for x in libraryBooks:
            currentLibrary.addBook(int(x))
        currentLibrary.calculateScore()
    
    Library.libraries = sorted(Library.libraries, key = lambda x : x.libraryScore, reverse = True)
    print("Loaded", libraries, "libraries")

    return None


def updateScore():
    return None

def printoutput():
    pass

def execute(outputName):
    global days

    librarySigningUp = False
    librarySigningUpDayDone = 0
    signedUpLibraries = []
    currentDay = 0
    while (currentDay < days):
        if (currentDay == librarySigningUpDayDone):
            librarySigningUp = False
        
        if (len(signedUpLibraries) != len(Library.libraries)):
            if (not librarySigningUp):
                nextLibrary = 0
                optimalLibraryToSignup = Library.libraries[nextLibrary]
                while (optimalLibraryToSignup.signedUp):
                    nextLibrary = nextLibrary + 1
                    optimalLibraryToSignup = Library.libraries[nextLibrary]
                optimalLibraryToSignup.signup(len(signedUpLibraries), currentDay)
                signedUpLibraries.append(optimalLibraryToSignup)
                Library.libraries.remove(optimalLibraryToSignup)
                updateScore()
                librarySigningUp = True
                librarySigningUpDayDone = currentDay + optimalLibraryToSignup.signupTime
        for library in signedUpLibraries:
            if (library.startSending <= currentDay):
                 library.sendBooks()  

        # Recalculate score of each library
        for library in Library.libraries:
            library.calculateScore()
        Library.libraries = sorted(Library.libraries, key = lambda x : x.libraryScore, reverse = True)
        currentDay = currentDay + 1


        print(currentDay, "/", days)
    
    f = open("output_" + outputName + ".txt", "w")
    
    numOfLibraries = 0
    for library in signedUpLibraries:
        if (len(library.scannedBooks) > 0):
            numOfLibraries = numOfLibraries + 1
    f.write(str(numOfLibraries))
    
    for library in signedUpLibraries:
        if (len(library.scannedBooks) <= 0):
            continue
        f.write("\n" + str(library.id) + " " + str(len(library.scannedBooks)) + "\n")
        for book in library.scannedBooks:
            f.write(str(book.id) + " ")

    f.close()
    

    


files = ["e_so_many_books.txt"]  

for i in files:
    loadData(i)
    print(f"Days: {days}")
    execute(i[:-4])
    