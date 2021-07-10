from .IPiece import IPiece

class General(IPiece):
    def __init__(self, isRed, board, pid, x=-1, y=-1):
        name = '将'
        img = '将.png'
        if isRed:
            name = '帥'
            img = '帥.png'
        super().__init__(isRed, name, pid, x, y)
        self.board = board
        self.img = img

    def GetDirections(self, position, player):
        x, y = position[0], position[1]
        directions = []
        if y > 0 and player.pieces[(x, y-1)] == None:
            directions.append((0, -1))
        if y < 2 and player.pieces[(x, y+1)] == None:
            directions.append((0, 1))
        if x > 3 and player.pieces[(x-1, y)] == None:
            directions.append((-1, 0))
        if x < 5 and player.pieces[(x+1, y)] == None:
            directions.append((1, 0))
        winable, enemyGeneralPosition = self.IseeYou(x, y, player)
        if winable:
            e_x, e_y = enemyGeneralPosition[0], enemyGeneralPosition[1]
            directions.append((e_x - x, e_y - y))
        return directions

    def IseeYou(self, x, y, player):
        enemy_x, player_y = player.Max_X - x, player.Max_y - y
        for i in range(0, 3):
            if isinstance(player.enemy.pieces[(enemy_x, i)], General):
                for j in range(i + 1, player_y):
                    if not player.board.pieces[player.enemy.relativePosition((enemy_x, j))] == None:
                        return False, None
                else:
                    return True, (x, player.Max_y - i)
        return False, None