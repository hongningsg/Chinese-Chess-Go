from .IPiece import IPiece

class Chariot(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '車'
        if isRed:
            name = '俥'
        super().__init__(isRed, name, x, y)
        self.board = board