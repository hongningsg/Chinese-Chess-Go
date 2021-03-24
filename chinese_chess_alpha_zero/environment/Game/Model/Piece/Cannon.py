from .IPiece import IPiece

class Cannon(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '砲'
        if isRed:
            name = '炮'
        super().__init__(isRed, name, x, y)
        self.board = board

    def GetDirections(self, position, player):
        x, y = position[0], position[1] 
        directions = []
        for ix, iy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            obstructs = self._firstTwoPieces(position, (ix, iy), player)
            if len(obstructs) == 0:
                max_X, max_Y = self.board.num_x - 1, self.board.num_y - 1
                directions.extend(self._slotsInDirection(ix, iy, x, y, max_X, max_Y))
            elif len(obstructs) == 1:
                obstructPosition = obstructs[0]
                max_X, max_Y = obstructPosition[0] - 1, obstructPosition[1] - 1
                directions.extend(self._slotsInDirection(ix, iy, x, y, max_X, max_Y))
            else:
                pivot = obstructs[0]
                max_X, max_Y = pivot[0] - 1, pivot[1] - 1
                directions.extend(self._slotsInDirection(ix, iy, x, y, max_X, max_Y))
                if not obstructs[1][1].isRed == player.isRed:
                    enemy = obstructs[1][0]
                    directions.extend([(enemy[0] - x, enemy[1] - y)])
        return directions

    def _firstTwoPieces(self, position, direction, player):
        x, y = position[0], position[1] 
        d_x, d_y = direction[0], direction[1]
        max_X, max_Y = self.board.num_x - 1, self.board.num_y - 1
        obstructs = []
        piecesCount = 0
        if d_y > 0 and d_x == 0:   
            while y < max_Y or piecesCount < 2:
                if not self.board.pieces[(x, y)] is None:
                    obstructs.append((player.relativePosition((x, y)), self.board.pieces[(x, y)]))
                    piecesCount += 1
                y += 1
        elif d_y < 0 and d_x == 0:
            while y > 0 or piecesCount < 2:
                if not self.board.pieces[(x, y)] is None:
                    obstructs.append((player.relativePosition((x, y)), self.board.pieces[(x, y)]))
                    piecesCount += 1
                y -= 1
        elif d_x > 0 and d_y == 0:
            while x < max_X or piecesCount < 2:
                if not self.board.pieces[(x, y)] is None:
                    obstructs.append((player.relativePosition((x, y)), self.board.pieces[(x, y)]))
                    piecesCount += 1
                x += 1
        elif d_x < 0 and d_y == 0:
            while x > 0 or piecesCount < 2:
                if not self.board.pieces[(x, y)] is None:
                    obstructs.append((player.relativePosition((x, y)), self.board.pieces[(x, y)]))
                    piecesCount += 1
                x -= 1
        else:
            raise ValueError(f"Direction not support: {direction}")
        return obstructs

    def _slotsInDirection(self, ix, iy, x, y, dist_x, dist_y): 
        if ix == 0 and iy > 0:
            return [(0, i) for i in range(1, dist_y-y+1)]
        elif ix == 0 and iy < 0:
            return [(0, i) for i in range(-1, dist_y-y-1, -1)]
        elif ix > 0 and iy == 0:
            return [(i, 0) for i in range(1, dist_x-x+1)]
        elif ix < 0 and iy == 0:
            return [(i, 0) for i in range(-1, dist_x-x-1, -1)]
        else:
            raise ValueError(f"Direction not support: {ix}, {iy}")