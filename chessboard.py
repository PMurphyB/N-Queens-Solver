class ChessBoard() :
    """
    ChessBoard is able to store a square board from 4 to 12 spaces in length,
and use this board to solve N-Queens Problem where n is the length of the board.

    Member variables: 
    
    boardSize (int): The length of one side of the square board.  boardSize of n
indicates an n x n board.

    board (string[][]): A 2-dimensional list that stores the board and placed 
queens.  
    """
    
    
    def __init__(self, boardSize = 8) :
        
        self.setSize(boardSize)
        
    def placeQueens(self, column) :
        """
        A recursive function to find placements for the queens on the baord.  
    Each call of queens will attempt to place a queen in the given column.  
    
        Parameters:
            column (int): The column the queen is to be placed into.
            
        Returns:
            bool: Returns True if a queen is successfully placed in column and 
        recursively in all columns to the right of column.  Otherwise, it
        returns False.  
        """
        
        row = 0
        
        # If True, the board is filled and the problem is solved.
        if column >= (self.__boardSize) :
            return True
        
        else :
            
            while (row < (self.__boardSize)) :
                
                if self.isAttacked(row, column) == False :
                    self.__board[row][column] = "Q"
                    
                    if self.placeQueens(column + 1) == False :
                        self.__board[row][column] = "*"
                        row += 1
                        
                    else :
                        return True
                    
                else :
                    row += 1
                    
            return False
                
    def setSize(self, boardSize) :
        """
        Replaces the existing board with a new board of the size given, with 
    a minimum of 4 and a maximum of 12.  
    
        Parameters:
            boardSize (int): The size of the board to create.
        """
        
        # Create a new empty board
        self.__board = []
        
        self.__boardSize = boardSize
        
        if self.__boardSize < 4 :
            self.__boardSize = 4
            
        elif self.__boardSize > 12 :
            self.__boardSize = 12
            
        # Create a 2-Dimensional list to represent the board.  
        for i in range(self.__boardSize) :
            tempList = []
            
            for j in range(self.__boardSize) :
                tempList.append("*")
            
            self.__board.append(tempList)
            
    def getSize(self) :
        """
        Returns the size of the current board.
        
        Returns:
            int: The size of the current board.
        """
        return self.__boardSize
            
    def solve(self) :
        """
        Non-recursive function that calls the recursive placeQueens() at column
    0.  
    
        Returns:
            bool: Returns True if the problem was successfully solved.
        """
        
        if self.placeQueens(0) == True :
            return True
    
    def displayBoard(self) :
        """
        Displays the board to the screen.  Queens are displayed as "Q", and
    empty spaces as "*".
        """
        
        for i in range(len(self.__board)) :
            
            for j in range(len(self.__board[i])) :
                
                print(self.__board[i][j], end = " ")
                
            print()
                
            
    def isAttacked(self, row, column) :
        """
        Checks to see if the queen being placed is being attacked by a
    previously placed queen.  
    
        Parameters:
            row (int): The current row being checked.
            column (int): The current column being checked.  
            
        Returns:
            bool: Returns True if the queen is being attacked, returns False if
        the Queen is safe.  
        """
        
        # Test to see if the queen is being attacked horizontally.
        for i in range(len(self.__board)) :
            
            if (self.__board[row][i] == "Q") :
                return True

        # Set test values.
        testRow = row
        testColumn = column
        
        # Test to see if the queen is being attacked diagonally upwards.
        while testRow > 0 and testColumn > 0 :
            testRow -= 1
            testColumn -= 1
            
            if self.__board[testRow][testColumn] == "Q" :
                return True
        
        # Reset test values.
        testRow = row
        testColumn = column
        
        # Test to see if the queen is being attacked diagonally downwards.  
        while testRow < (self.__boardSize - 1) and testColumn >= 0 :
            testRow += 1
            testColumn -= 1
            
            # Check for invalid values
            if testColumn < 0 :
                testColumn = 0
            
            if self.__board[testRow][testColumn] == "Q" :
                return True
        
        # If all of these tests are passed, the queen is not being attacked.    
        return False