from ..Model.Player.Player import Player
from ..Model.Board.Board import Board
from .GameController import GameController
from .BoardState import BoardState
from .Memory import GameMemory


class BoardController(GameController):
    def __init__(self, debug=False):
        super().__init__(debug)
        window = 5
        maxNoProgress = 50
        maxRepetition = 6
        self.memory = GameMemory(window, maxNoProgress, maxRepetition)
        self.memory.initialState(True, self.board)
        self.memory.getMoves(self.getMoves())

    def MovePiece(self, x, y, new_x, new_y):
        piece = self.GetPiece((x, y))
        player = self.GetPlayer(piece)
        if player is None:
            return False
        x, y = player.relativePosition((x, y))
        new_x, new_y = player.relativePosition((new_x, new_y))
        if player.isRed:
            valid = self.Red_Move(x, y, new_x, new_y)
        else:
            valid = self.Black_Move(x, y, new_x, new_y)
        if valid:
            direction = (new_x - x, new_y - y)
            pieceCount = self.red.piecesLeft + self.black.piecesLeft
            if self.memory.record(player.isRed, self.board, piece.name + str(piece.id), direction, pieceCount):
                self.GameOver(None, True)
            self.memory.getMoves(self.getMoves())
        return valid

    def getMoves(self):
        select_y = []
        for y in range(10):
            select_x = []
            for x in range(9):
                hasPiece, options = self.Select((x, y))
                if hasPiece:
                    placeHolder = self.CreatePlaceHolder(0)
                    for position in options:
                        i, j = position[0], position[1]
                        placeHolder[j][i] = 1
                    select_x.append(placeHolder)
                else:
                    select_x.append(self.CreatePlaceHolder(0))
            select_y.append(select_x)
        return select_y

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

    @staticmethod
    def CreatePlaceHolder(value):
        placeHolder = []
        for i in range(10):
            placeHolder.append([value for _ in range(9)])
        return placeHolder
