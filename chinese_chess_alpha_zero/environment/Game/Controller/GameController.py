from ..Model.Player.Player import Player
from ..Model.Board.Board import Board

class GameController:
    def __init__(self, debug=False):
        self.board = Board()
        self.red = Player(True, self.board, debug)
        self.black = Player(False, self.board, debug)
        self.redNext = True
        self.debug = debug
    
    def GetMoveOption(self, x, y, player):
        if player.pieces[(x, y)] is None:
            return False, []
        else:
            return True, player.MoveDirection(x, y)

    def Red_Move(self, x, y, new_x, new_y):
        if self.redNext:
            valid, directions = self.GetMoveOption(x, y, self.red)
            if valid and (new_x - x, new_y - y) in directions:
                if self.debug:
                    self.Shout(x, y, new_x, new_y, self.red)
                x, y = self.red.Move(x, y, new_x, new_y)
                if not x == -1:
                    self.black.Terminate(x, y)
                self.redNext = False
                return True
            else:
                return False
        else:
            return False

    def Black_Move(self, x, y, new_x, new_y):
        if not self.redNext:
            valid, directions = self.GetMoveOption(x, y, self.black)
            if valid and (new_x - x, new_y - y) in directions:
                if self.debug:
                    self.Shout(x, y, new_x, new_y, self.black)
                x, y = self.black.Move(x, y, new_x, new_y)
                if not x == -1:
                    self.red.Terminate(x, y)
                self.redNext = True
                return True
            else:
                return False
        else:
            return False

    def Shout(self, x, y, new_x, new_y, player):
        piece = player.pieces[(x, y)]
        print(f'{player.color}: {piece.name} 从 ({x}, {y}) 移动到 ({new_x}, {new_y})')

    def GetNextPlayer(self):
        if self.redNext:
            self.redNext = False
            return self.red
        else:
            self.redNext = True
            return self.black
    
    def PrintBoard(self):
        print(self.board)