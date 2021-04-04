from .GameController import GameController

def GuardScript1():
    game = GameController(True)
    game.PrintBoard()
    print(game.GetMoveOption(3, 0, game.red))
    print(game.Red_Move(3, 0, 3, 1))
    game.Red_Move(3, 0, 4, 1)
    print(game.GetMoveOption(4, 1, game.red))
    game.PrintBoard()
    game.Black_Move(5, 0, 4, 1)
    game.PrintBoard()
    print(game.Red_Move(5, 0, 4, 1))