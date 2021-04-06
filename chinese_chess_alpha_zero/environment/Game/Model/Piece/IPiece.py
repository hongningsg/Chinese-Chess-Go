class IPiece(object):
    def __init__(self, isRed, name, x=-1, y=-1):
        self.x = x
        self.y = y
        self.isRed = isRed
        self.name = name
        self.dead = False
        self.img = None

    @staticmethod
    def NoImplementionException():
        raise Exception('Method not implemented.')

    def Move(self, direction):
        self.x += direction.x
        self.y += direction.y

    def GetDirections(self, position, player):
        self.NoImplementionException()

    def GetStatus(self):
        return self.dead
    
    def GetPosition(self):
        return self.x, self.y

    def Terminated(self):
        self.dead = True

    def SetPosition(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def Kill(chess):
        chess.Terminated()