from ..Model.Player.Player import Player
from ..Model.Board.Board import Board
from .GameController import GameController

class BoardController(GameController):
    def __init__(self, debug=False):
        super().__init__(debug)

    def MovePiece(self, x, y, new_x, new_y):
        piece = self.GetPiece((x, y))
        player = self.GetPlayer(piece)
        if player is None:
            return False
        x, y = player.relativePosition((x, y))
        new_x, new_y = player.relativePosition((new_x, new_y))
        if player.isRed:
            return self.Red_Move(x, y, new_x , new_y)
        else:
            return self.Black_Move(x, y, new_x , new_y)

    def Select(self, position):
        """返回：是否可走 + 所有可行进的路径"""
        if not self.alive:
            return False, []
        piece = self.GetPiece(position)
        if piece is None:
            return False, []
        x, y = position[0], position[1]
        if piece.isRed == self.redNext:
            relativePosition = self.GetRelativePosition(piece)
            player = self.GetPlayer(piece)
            r_x, r_y = relativePosition[0], relativePosition[1]
            success, moveDirections = self.GetMoveOption(r_x, r_y, player)
            if success:
                distinations = []
                for direction in moveDirections:
                    d_x, d_y = player.relativeDirection(direction)
                    distinations.append((x + d_x, y + d_y))
                return True, distinations
        return False, []
    
    def PrintDistinations(self, distinations):
        if self.debug:
            board = self.board
            represent = ''
            for y in range(board.num_y - 1, -1, -1):
                for x in range(board.num_x):
                    if (x, y) in distinations:
                        represent += 'O'
                    elif board.pieces[(x, y)] is None:
                        represent += '+'
                    else:
                        represent += board.pieces[(x, y)].name
                    represent += '\t'
                represent += '\n\n'
            print(represent)
