class BoardState:
    def __init__(self, isRed, board, direction):
        self.isRed = isRed
        self.pieces = []
        self.Snapshot(board)
        self.direction = direction

    def Snapshot(self, board):
        stateMap = {
            '砲': 0,
            '車': 1,
            '象': 2,
            '将': 3,
            '士': 4,
            '馬': 5,
            '卒': 6,
            '炮': 7,
            '俥': 8,
            '相': 9,
            '帥': 10,
            '仕': 11,
            '傌': 12,
            '兵': 13
        }
        for _ in stateMap:
            self.pieces.append(self.CreatePlaceHolder())
        for y in range(board.num_y - 1, -1, -1):
            for x in range(board.num_x):
                if not board.pieces[(x, y)] is None:
                    self.pieces[stateMap[board.pieces[(x, y)].name]][y][x] = 1

    @staticmethod
    def CreatePlaceHolder():
        placeHolder = []
        for i in range(10):
            placeHolder.append([0 for _ in range(9)])
        return placeHolder

    def equal(self, state):
        if state.direction[0] + self.direction[0] == 0 and state.direction[1] + self.direction[1] == 0:
            return True
        return False
