from .IPiece import IPiece

class Elephant(IPiece):
    def __init__(self, isRed, board, pid, x=-1, y=-1):
        name = '象'
        if isRed:
            name = '相'
        super().__init__(isRed, name, pid, x, y)
        self.board = board
        self.possiblePosition = [
            (0, 2),
            (2, 0),
            (2, 4),
            (4, 2),
            (6, 4),
            (6, 0),
            (8, 2)
        ]
        self.rule = self._LoadRule()
        self.img = name + '.png'

    def GetDirections(self, position, player):
        directions = []
        dists = self.rule[position]
        for dist in dists:
            if self.board.pieces[player.relativePosition(dists[dist])] == None and player.pieces[dist] == None:
                directions.append((dist[0] - position[0], dist[1] - position[1]))
        return directions

    def _LoadRule(self):
        return {
            (0, 2): {
                (2, 0): (1, 1),
                (2, 4): (1, 3)
            },
            (2, 0): {
                (0, 2): (1, 1),
                (4, 2): (3, 1)
            },
            (2, 4): {
                (0, 2): (1, 3),
                (4, 2): (3, 3)
            },
            (4, 2): {
                (2, 0): (3, 1),
                (2, 4): (3, 3),
                (6, 4): (5, 3),
                (6, 0): (5, 1)
            },
            (6, 4): {
                (4, 2): (5, 3),
                (8, 2): (7, 3)
            },
            (6, 0): {
                (4, 2): (5, 1),
                (8, 2): (7, 1)
            },
            (8, 2): {
                (6, 0): (7, 1),
                (6, 4): (7, 3)
            }
        }
