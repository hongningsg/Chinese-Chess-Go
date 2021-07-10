from .BoardState import BoardState


class GameMemory:
    def __init__(self, window, maxNoProgress, maxRepetition):
        self.noProgressCount = 0
        self.maxNoProgress = maxNoProgress
        self.predecessor = None
        self.repetition = 0
        self.maxRepetition = maxRepetition
        self.pieceLeft = 32
        self.history = []
        self.window = window
        self.moves = []
        self.step = 0

    def initialState(self, isRed, board):
        state = BoardState(isRed, board, None, (0, 0))
        for _ in range(4):
            self.history.append(state.copy())

    def enqueue(self, state):
        if len(self.history) >= self.window:
            self.history.pop(0)
        self.history.append(state)

    def record(self, isRed, board, pieceInfo, direction, pieceLeft):
        state = BoardState(isRed, board, pieceInfo, direction)
        if len(self.history) > 2:
            if state.equal(self.history[-2]):
                self.repetition += 1
            else:
                self.repetition = 0
        self.enqueue(state)
        if pieceLeft == self.pieceLeft:
            self.noProgressCount += 1
        else:
            self.pieceLeft = pieceLeft
            self.noProgressCount = 0
        self.step += 1
        if self.repetition >= self.maxRepetition or self.noProgressCount >= self.maxNoProgress:
            return True
        return False

    def getMoves(self, options):
        self.moves = options
