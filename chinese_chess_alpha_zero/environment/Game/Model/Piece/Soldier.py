from .IPiece import IPiece

class Soldier(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '卒'
        if isRed:
            name = '兵'
        super().__init__(isRed, name, x, y)
        self.board = board
        self.img = name + '.png'

    def GetDirections(self, position, player):
        directions = []
        max_X, max_Y = self.board.num_x - 1, self.board.num_y - 1
        x, y = position[0], position[1] 
        if y < max_Y:
            directions.append((0, 1))
        if y > self.board.bank:
            if x > 0:
                directions.append((-1, 0))
            if x < max_X:
                directions.append((1, 0))
        return self._filter(x, y, directions, player)

    def _filter(self, x, y, directions, player):
        for direction in directions:
            obstruct, _ = player.FriendlyObstruct(x + direction[0], y + direction[1])
            if obstruct:
                directions.remove(direction)
        return directions
