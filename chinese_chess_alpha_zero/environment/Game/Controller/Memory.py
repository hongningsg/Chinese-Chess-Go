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

    def enqueue(self, state):
        if len(self.history) >= self.window:
            self.history.pop(0)
        self.history.append(state)

    def record(self, isRed, board, direction, pieceLeft):
        state = BoardState(isRed, board, direction)
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
        if self.repetition >= self.maxRepetition or self.noProgressCount >= self.maxNoProgress:
            return True
        return False

