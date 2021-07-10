from .Controller.BoardController import BoardController


class EnvApi:
    def __init__(self, controller):
        self.controller = controller

    def post(self):
        memory = self.controller.memory
        validMoves = memory.moves
        states = [state.pieces for state in memory.history]
        gameOver = not self.controller.alive
        winner = None
        if gameOver:
            winnerString = self.controller.GetWinner()
            if winnerString == '红色':
                winner = 1
            elif winnerString == '黑色':
                winner = -1
            else:
                winner = 0
        steps = self.controller.memory.step
        return {
            "valid_moves": validMoves,
            "states": states,
            "game_over": gameOver,
            "winner": winner,
            "steps": steps
        }
