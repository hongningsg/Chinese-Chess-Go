from .IPiece import IPiece

class Horse(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '馬'
        if isRed:
            name = '傌'
        super().__init__(isRed, name, x, y)
        self.board = board

    def GetDirections(self, position, player):
        x, y = position[0], position[1]
        directions = []
        for ix, iy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self._Movable(ix, iy, x, y, player):
                potentials = self._Destination(ix, iy, x, y, player)
                for potential in potentials:
                   directions.append((potential[0] - x, potential[1] - y))
        return directions

    def _Movable(self, ix, iy, x, y, player):
        if x + ix >= 0 and x + ix < self.board.num_x and y + iy >= 0 and y + iy <  self.board.num_y:
            abs_x, abs_y = player.relativePosition((x + ix, y + iy))
            return self.board.pieces[(abs_x, abs_y)] == None
        return False

    def _Destination(self, ix, iy, x, y, player):
        dists = []
        dist_x, dist_y = x + ix * 2, y + iy * 2
        if ix == 0 and dist_y < self.board.num_y and dist_y > -1:
            dist_x1 = dist_x + 1
            if dist_x1 > -1 and dist_x1 < self.board.num_x and player.pieces[((dist_x1, dist_y))] == None:
                dists.append((dist_x1, dist_y))
            dist_x2 = dist_x - 1
            if dist_x2 > -1 and dist_x2 < self.board.num_x and player.pieces[((dist_x2, dist_y))] == None:
                dists.append((dist_x2, dist_y))
        if iy == 0 and dist_x < self.board.num_x and dist_x > -1:
            dist_y1 = dist_y + 1 
            if dist_y1 > -1 and dist_y1 < self.board.num_y and player.pieces[((dist_x, dist_y1))] == None:
                dists.append((dist_x, dist_y1))
            dist_y2 = dist_y - 1
            if dist_y2 > -1 and dist_y2 < self.board.num_y and player.pieces[((dist_x, dist_y2))] == None:
                dists.append((dist_x, dist_y2))
        assert len(dists) < 3, "Incorrect lenth of potential distinations."
        return dists
