from .IPiece import IPiece

class Chariot(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '車'
        if isRed:
            name = '俥'
        super().__init__(isRed, name, x, y)
        self.board = board

    def GetDirections(self, position, player):
        max_X, max_Y = self.board.num_x - 1, self.board.num_y - 1
        x, y = position[0], position[1] 
        directions = []
        directions.append([(0, i) for i in range(-1, -y-1, -1)])
        directions.append([(0, i) for i in range(1, max_Y - y - 1)])
        directions.append([(i, 0) for i in range(0, -x-1, -1)])
        directions.append([(i, 0) for i in range(1, max_X - x - 1)])
        return self._filter(x, y, directions, player)

    def _filter(self, x, y, directions, player):
        pass