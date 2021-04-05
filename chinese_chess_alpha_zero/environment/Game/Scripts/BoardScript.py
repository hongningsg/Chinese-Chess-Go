from ..Controller.BoardController import BoardController

def BoardScript1():
    game = BoardController(True)
    print(game.Select((0, 0)))
    print(game.Select((0, 1)))
    print(game.Select((1, 0)))
    print(game.Select((0, 9)))
    print(game.MovePiece(0, 9, 0, 8))
    print(game.MovePiece(0, 0, 0, 1))
    print(game.Select((0, 9)))
    print(game.MovePiece(0, 9, 0, 8))
    print(game.Select((0, 1)))
    game.MovePiece(0, 1, 3, 1)
    game.PrintBoard()
    print(game.Select((0, 8)))
    print(game.MovePiece(0, 8, 3, 8))
    print(game.Select((3, 1)))
    game.MovePiece(3, 1, 3, 8)

def BoardScript2():
    game = BoardController(True)
    game.MovePiece(0, 3, 0, 4)
    game.PrintBoard()
    game.MovePiece(0, 9, 0, 8)
    game.PrintBoard()
    game.MovePiece(0, 4, 0, 5)
    print(game.Select((0, 8)))
