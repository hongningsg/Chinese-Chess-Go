from .GameController import GameController

def CannonScript1():
    game = GameController(True)
    print(game.red)
    game.Red_Move(1, 2, 2, 2)
    # print(game.GetMoveOption(2, 2, game.red))
    print(game.board)
    game.Black_Move(7, 2, 8, 2)
    print(game.board)
    game.Red_Move(2, 2, 2, 6)
    print(game.board)
    game.Black_Move(8, 2, 8, 3)
    print(game.redNext)
    game.Red_Move(2, 6, 2, 7)
    print(game.board)
    game.Black_Move(8, 2, 8, 6)
    print(game.board)
    game.Red_Move(2, 6, 6, 6)
    print(game.board)
    game.Black_Move(8, 6, 4, 6)
    print(game.board)
    game.Red_Move(6, 6, 7, 6)
    print(game.board)
    game.Black_Move(1, 2, 1, 7)
    print(game.board)