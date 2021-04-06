from .IPiece import IPiece

class Chariot(IPiece):
    def __init__(self, isRed, board, x=-1, y=-1):
        name = '車'
        if isRed:
            name = '俥'
        super().__init__(isRed, name, x, y)
        self.board = board
        self.img = name + '.png'

    def GetDirections(self, position, player):
        x, y = position[0], position[1] 
        directions = []
        for ix, iy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            friendlyHasObstruct, friendlyObstruct = player.FriendlyObstruct(x, y, (ix, iy))
            friendlyObstruct = (friendlyObstruct[0] - 1 * ix, friendlyObstruct[1] - 1 * iy)
            enemyHasObstruct, enemyObstruct = player.EnemyObstruct(x, y, (ix, iy))
            if friendlyHasObstruct and enemyHasObstruct:
                obstructPosition = self._closestEnd(friendlyObstruct, enemyObstruct, (ix, iy))
                directions = self._append(directions, obstructPosition, ix, iy, x, y)
            elif friendlyHasObstruct:
                directions = self._append(directions, friendlyObstruct, ix, iy, x, y)
            else:
                directions = self._append(directions, enemyObstruct, ix, iy, x, y)
        return directions

    @staticmethod    
    def _closestEnd(friendly, enemy, direction):
        d_x, d_y = direction[0], direction[1]
        x_f, y_f = friendly[0], friendly[1]
        x_e, y_e = enemy[0], enemy[1]
        if (d_x * x_f + d_y * y_f) - (d_x * x_e + d_y * y_e) < 0:
            return (x_f, y_f)
        else:
            return (x_e, y_e)

    @staticmethod
    def _append(directions, obstruct, ix, iy, x, y):
        e_x, e_y = obstruct[0], obstruct[1]
        if iy == -1:
            directions.extend([(0, i) for i in range(-1, e_y-y-1, -1)])
        elif iy == 1:
            directions.extend([(0, i) for i in range(1, e_y-y+1)])
        elif ix == -1:
            directions.extend([(i, 0) for i in range(-1, e_x-x-1, -1)])
        elif ix == 1:
            directions.extend([(i, 0) for i in range(1, e_x-x+1)])
        else:
            raise ValueError(f"Direction not support: {ix, iy}")
        return directions