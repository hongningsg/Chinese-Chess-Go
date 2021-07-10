class BoardState:
    def __init__(self, isRed, board, pieceInfo, direction):
        self.isRed = isRed
        self.pieces = []
        self.board = board
        self.Snapshot(board, isRed)
        self.direction = direction
        self.pieceInfo = pieceInfo

    def Snapshot(self, board, isRed):
        stateMap = {
            '砲0': 0,
            '砲1': 1,
            '車0': 2,
            '車1': 3,
            '象0': 4,
            '象1': 5,
            '将0': 6,
            '士0': 7,
            '士1': 8,
            '馬0': 9,
            '馬1': 10,
            '卒0': 11,
            '卒1': 12,
            '卒2': 13,
            '卒3': 14,
            '卒4': 15,
            '炮0': 16,
            '炮1': 17,
            '俥0': 18,
            '俥1': 19,
            '相0': 20,
            '相1': 21,
            '帥0': 22,
            '仕0': 23,
            '仕1': 24,
            '傌0': 25,
            '傌1': 26,
            '兵0': 27,
            '兵1': 28,
            '兵2': 29,
            '兵3': 30,
            '兵4': 31,
            '颜色': 32
        }
        value = 0
        if isRed:
            value = 1
        for _ in range(len(stateMap) - 1):
            self.pieces.append(self.CreatePlaceHolder(0))
        self.pieces.append(self.CreatePlaceHolder(value))
        for y in range(board.num_y):
            for x in range(board.num_x):
                piece = board.pieces[(x, y)]
                if not piece is None:
                    self.pieces[stateMap[piece.name + str(piece.id)]][y][x] = 1

    @staticmethod
    def CreatePlaceHolder(value):
        placeHolder = []
        for i in range(10):
            placeHolder.append([value for _ in range(9)])
        return placeHolder

    def equal(self, state):
        if self.pieceInfo == state.pieceInfo:
            if state.direction[0] + self.direction[0] == 0 and state.direction[1] + self.direction[1] == 0:
                return True
        return False

    def copy(self):
        return BoardState(self.isRed, self.board, self.pieceInfo, self.direction)
