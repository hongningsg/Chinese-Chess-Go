from ..Piece import Soldier, IPiece, Chariot, Cannon

class Player:
    def __init__(self, isRed, board, debug=False):
        self.isRed = isRed
        self.debug = debug
        self.Max_X = board.num_x - 1
        self.Max_y = board.num_y - 1
        self.first = False
        self.invert = -1
        self.color = '黑色'
        if isRed:
            self.first = True
            self.invert = 1
            self.color = '红色'
        self.board = board
        self.pieces = self._Initial_board()
        self.positions = []
        self.piecesLeft = 16
        self._Reset()
        self.enemy = None

    def _Initial_board(self):
        pieces = {}
        for y in range(self.board.num_y):
            for x in range(self.board.num_x):
                pieces[(x, y)] = None
        return pieces

    def SetEnemy(self, player):
        self.enemy = player
 
    def _Reset(self):
        self._Initial_Soldier()
        self._Initial_Soldier()
        self._Inital_Cannon()

    def _register_to_board(self, positions, pieces):
        if not self.isRed:
            for i in range(len(positions)):
                positions[i] = self._Invert_Position(positions[i])
        for i, position in enumerate(positions):
            x, y = position[0], position[1]
            pieces[i].SetPosition(x, y)
            self.board.AddPiece(x, y, pieces[i])

    def _Initial_Soldier(self):
        positions = [(0, 3), (2, 3), (4, 3), (6, 3), (8, 3)]
        soldiers = []
        for position in positions:
            self.positions.append(position)
            x, y = position[0], position[1]
            soldier = Soldier.Soldier(self.isRed, self.board)
            self.pieces[(x, y)] = soldier
            soldiers.append(soldier)
        self._register_to_board(positions, soldiers)

    def _Initial_Chariot(self):
        positions = [(0, 0), (8, 0)]
        chariots = []
        for position in positions:
            self.positions.append(position)
            x, y = position[0], position[1]
            chariot = Chariot.Chariot(self.isRed, self.board)
            self.pieces[(x, y)] = chariot
            chariots.append(chariot)
        self._register_to_board(positions, chariots)

    def _Inital_Cannon(self):
        positions = [(1, 2), (7, 2)]
        cannons = []
        for position in positions:
            self.positions.append(position)
            x, y = position[0], position[1]
            cannon = Cannon.Cannon(self.isRed, self.board)
            self.pieces[(x, y)] = cannon
            cannons.append(cannon)
        self._register_to_board(positions, cannons)
    
    def MoveDirection(self, x, y):
        piece = self.pieces[(x, y)]
        return piece.GetDirections((x, y), self)

    def Move(self, x, y, new_x, new_y):      
        self._Update_Position(x, y, new_x, new_y)
        self._Update_Piece(x, y, new_x, new_y)
        if not self.isRed:
            x, y = self._Invert_Position((x, y))
            new_x, new_y = self._Invert_Position((new_x, new_y))
        piece = self.board.MovePiece(x, y, new_x, new_y)
        if not piece is None:
            if piece.isRed:
                return (piece.x, piece.y)
            else:
                return self._Invert_Position((piece.x, piece.y))
        else:
            return (-1, -1)
            
    def _Update_Piece(self, x, y, new_x, new_y):
        piece = self.pieces[(x, y)]
        self.pieces[(x, y)] = None
        self.pieces[(new_x, new_y)] = piece

    def _Update_Position(self, x, y, new_x, new_y):
        for i in range(len(self.positions)):
            p = self.positions[i]
            if p[0] == x and p[1] == y:
                self.positions[i] = (new_x, new_y)
                return

    def Terminate(self, x, y):
        self.positions.remove((x, y))
        piece = self.pieces[(x, y)] 
        self.pieces[(x, y)] = None
        self.piecesLeft -= 1
        self.DeadCry(x, y, piece)

    def FriendlyObstruct(self, x, y, direction=(0, 0)):
        d_x, d_y = direction[0], direction[1]
        if d_x == 0 and d_y == 0:
            return (not self.pieces[(x, y)] == None), (x, y)
        if d_x == 0:
            if d_y > 0:
                for i in range(y, self.board.num_y, 1):
                    if not self.pieces[(x, i)] == None:
                        return True, (x, i)
                return False, (x, self.Max_y)
            if d_y < 0:
                for i in range(y, -1, -1):
                    if not self.pieces[(x, i)] == None:
                        return True, (x, i)
                return False, (x, 0)
        if d_y == 0:
            if d_x > 0:
                for i in range(x, self.board.num_x, 1):
                    if not self.pieces[(i, y)] == None:
                        return True, (i, y)
                return False, (self.Max_X, y)
            if d_x < 0:
                for i in range(x, -1, -1):
                    if not self.pieces[(i, y)] == None:
                        return True, (i, y)
                return False, (0, y)
    
    def EnemyObstruct(self, x, y, direction=(0, 0)):
        inverted_position = self._Invert_Position((x, y))
        inverted_direction = self._Invert_Direction(direction)
        status, position = self.enemy.FriendlyObstruct(inverted_position[0], inverted_position[1], inverted_direction)
        return status, self._Invert_Position(position)

    def DeadCry(self, x, y, piece):
        if self.debug:
            print(f'{self.color}: 草了,吃老子在({x}, {y})的{piece.name}, 剩下{self.piecesLeft}个棋子啦!')            

    def _Invert_Position(self, position):
        x, y = position[0], position[1]
        return (self.Max_X - x, self.Max_y - y)

    def _Invert_Direction(self, direction):
        return (direction[0] * -1, direction[1] * -1)

    def relativePosition(self, position):
        if self.isRed:
            return position
        else:
            return self._Invert_Position(position)

    def relativeDirection(self, direction):
        if self.isRed:
            return direction
        else:
            return self._Invert_Direction(direction)

    def __str__(self):
        represent = f"Pieces left: {self.piecesLeft}\n"
        for position in self.positions:
            x, y = position[0], position[1]
            represent += f"\t{self.pieces[position].name} - x:{x}, y:{y}\n"
        return represent