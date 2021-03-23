class Board:
    def __init__(self, board = None):
        if not board is None:
            self = board
        self.num_x = 9
        self.num_y = 10
        self.bank = 4
        self.pieces = self._initial_board()

    def _initial_board(self):
        pieces = {}
        for y in range(self.num_y):
            for x in range(self.num_x):
                pieces[(x, y)] = None
        return pieces

    def Reset(self):
        self.pieces = self._initial_board()
    
    def MovePiece(self, x, y, new_x, new_y):
        currentPiece = self.GetPieceByPosition(new_x, new_y)
        self.pieces[(new_x, new_y)] = self.pieces[(x, y)]
        self.pieces[(new_x, new_y)].x = new_x
        self.pieces[(new_x, new_y)].y = new_y
        self.pieces[(x, y)] = None
        return currentPiece

    def isEmptyPosition(self, x, y):
        return self.GetPieceByPosition(x, y) == None

    def GetPieceByPosition(self, x, y):
        return self.pieces[(x, y)]

    def AddPiece(self, x, y, piece):
        self.pieces[(x, y)] = piece

    def __str__(self):
        represent = ''
        for y in range(self.num_y - 1, -1, -1):
            for x in range(self.num_x):
                if self.pieces[(x, y)] is None:
                    represent += '+'
                else:
                    represent += self.pieces[(x, y)].name
                represent += '\t'
            represent += '\n\n'
        return represent