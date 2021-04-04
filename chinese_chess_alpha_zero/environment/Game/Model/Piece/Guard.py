from .IPiece import IPiece

class Guard(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '士'
        if isRed:
            name = '仕'
        super().__init__(isRed, name, x, y)
        self.board = board

    def GetDirections(self, position, player):
        x, y = position[0], position[1]
        directions = []
        if y > 0:
            if x > 3 and player.pieces[(x-1, y-1)] == None:
                directions.append((-1, -1))
            if x < 5 and player.pieces[(x+1, y-1)] == None:
                directions.append((1, -1))
        if y < 2:
            if x > 3 and player.pieces[(x-1, y+1)] == None:
                directions.append((-1, 1))
            if x < 5 and player.pieces[(x+1, y+1)] == None:
                directions.append((1, 1))
        return directions
        