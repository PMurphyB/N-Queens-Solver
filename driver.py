from chessboard import ChessBoard

def main() :
    
    userChoice = 0
    
    active = True
    
    myBoard = ChessBoard()
    
    print("Here is the default unsolved board: ")
    myBoard.displayBoard()
    print()
    
    print("Here is the default solved board (where n = 8): ")
    myBoard.solve()
    myBoard.displayBoard()
    print()    
    
    while active :
        print("What N-Queen problem would you like to solve for (must be 4 or greater)?")
        userChoice = input("Enter 'Q' to quit: ")
        print()
        
        if userChoice == "Q" :
            active = False
            print("Thank you for playing!")
            
        elif int(userChoice) < 4 :
            print("That is an invalid value!")
            print("What N-Queen problem would you like to solve for (must be 4 or greater)?")
            userChoice = input(print("Enter 'Q' to quit: "))      
            print()
            
        else :
            
            myBoard.setSize(int(userChoice))
            
            if not myBoard.solve():
                print(f"Sorry, no solution was found for board size {myBoard.getSize()}.")
                print("The final board is:")
                myBoard.displayBoard()
                print()
            else:
                print(f"Size {myBoard.getSize()} solution:")
                myBoard.displayBoard()
                print()
        
        
        
    
if __name__ == "__main__":
    main()
