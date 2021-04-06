from ..Controller.BoardController import BoardController
import os
import pygame

class BoardGUI:
    def __init__(self, width=1000, height=1200, bg=(153, 102, 0)):
        self.width = width
        self.height = height
        self.bg = bg
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'Assets')
        self.asset_path = filename
        self.screen = None
        self.game = None

    def Start(self):
        self.game = BoardController(True)
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode([self.width, self.height])
        left_pad = self.width*0.03
        top_pad = self.height*0.03
        horizontal, vertical = self.width * 0.94 , self.height*0.94
        x_gap, y_gap = horizontal//8, vertical//9
        piece_hori, piece_vert = self.width//10, self.height//10
        self.screen = screen
        running = True
        isSelecting = False
        selectingPosition = None
        selectedPiece = None
        mousePosition = None
        dropPiece = False
        end_location = None
        potentials = []
        while running:
            screen.fill(self.bg)
            self.DrawBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clickPosition = self.GridPosition(self.Position(pygame.mouse.get_pos()))
                    if not self.game.alive:
                        self.game.ResetGame()
                        isSelecting = False
                        selectingPosition = None
                        selectedPiece = None
                        mousePosition = None
                        dropPiece = False
                        end_location = None
                        potentials = []
                        break
                    if not isSelecting:
                        selectable, potentials = self.game.Select(clickPosition)
                        if selectable and clickPosition in self.game.board.positions:
                            selectingPosition = clickPosition
                            selectedPiece = self.game.board.pieces[selectingPosition]
                            mousePosition = pygame.mouse.get_pos()
                            isSelecting = True
                    else:
                        end_position = clickPosition
                        x, y, new_x, new_y = selectingPosition[0], selectingPosition[1], end_position[0], end_position[1]
                        if self.game.MovePiece(x, y, new_x, new_y):
                            end_location = self.PositionToLocation(end_position)
                            dropPiece = True
                            isSelecting = False
                            selectingPosition = None
                if isSelecting and event.type == pygame.MOUSEMOTION:
                    mousePosition = pygame.mouse.get_pos()
                if isSelecting and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    isSelecting = False
                    selectingPosition = None
            self.DrawPieces(piece_hori, piece_vert, screen, selectingPosition)
            if self.game.alive:
                if isSelecting:
                    self.DrawPotentials(screen, potentials)
                    self.DrawMovingPieces(piece_hori, piece_vert, screen, selectedPiece, mousePosition)
                if dropPiece:
                    dropPiece = False
                    self.DrawPiece(piece_hori, piece_vert, screen, selectedPiece, end_location)
            else:
                myfont = pygame.font.SysFont('SimHei', 72)
                winner = self.game.GetWinner()
                color = (0, 0, 0)
                if self.game.GetWinner() == '红色': 
                    color = (250, 0, 0)
                winner = myfont.render(f'{self.game.GetWinner()}方赢了', False, color)
                screen.blit(winner,(self.width//3, self.height//2 - y_gap//3))
                myfont = pygame.font.SysFont('SimHei', 24)
                text = myfont.render('点击鼠标左键继续', False, color)
                screen.blit(text,(self.width//2 - 96, self.height//2 - y_gap//3 + 72))
            pygame.display.flip()
        pygame.quit()

    def DrawPotentials(self, screen, potentials):
        radius = int(min(self.height, self.width)//30)
        for potential in potentials:
            location = self.PositionToLocation(potential)
            location = (int(location[0] + radius + 20), int(location[1] + radius + 20))
            pygame.draw.circle(screen, (23, 207, 84), location, radius, 0)


    def DrawMovingPieces(self, piece_hori, piece_vert, screen, selectedPiece, mousePosition):
        selectingLocation = (mousePosition[0] - piece_hori//2, mousePosition[1] - piece_vert//2)
        selectImg = pygame.image.load(os.path.join(self.asset_path, selectedPiece.img))
        selectImg = pygame.transform.scale(selectImg, (piece_vert, piece_hori))
        screen.blit(selectImg, selectingLocation)

    def DrawPiece(self, piece_hori, piece_vert, screen, piece, location):
        image = pygame.image.load(os.path.join(self.asset_path, piece.img))
        image = pygame.transform.scale(image, (piece_vert, piece_hori))
        screen.blit(image, location)

    def DrawBoard(self):
        left_pad = self.width*0.03
        top_pad = self.height*0.03
        horizontal, vertical = self.width * 0.94 , self.height*0.94
        x_gap, y_gap = horizontal//8, vertical//9
        for i in range(10):
            y = top_pad + y_gap * i
            self.DrawLine(left_pad, y, left_pad + horizontal, y)
        for i in range(9):
            x = left_pad + x_gap * i
            if i == 0 or i == 8:
                self.DrawLine(x, top_pad, x, top_pad + vertical)
            else:
                self.DrawLine(x, top_pad, x, top_pad + (vertical - y_gap)//2)
                self.DrawLine(x, top_pad + (vertical - y_gap)//2 + y_gap, x, top_pad + vertical)
            if i == 1 or i == 7:
                padding = 10
                length = y_gap//3
                self.DrawCannonBase(x - padding, top_pad + (vertical - y_gap)//4 - padding - length, x - padding, top_pad + (vertical - y_gap)//4 - padding)
                self.DrawCannonBase(x + padding, top_pad + (vertical - y_gap)//4 - padding - length, x + padding, top_pad + (vertical - y_gap)//4 - padding)
                self.DrawCannonBase(x - padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding - length, x - padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding)
                self.DrawCannonBase(x + padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding - length, x + padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding)
                self.DrawCannonBase(x - padding, top_pad + (vertical - y_gap)//4 + padding, x - padding, top_pad + (vertical - y_gap)//4 + padding + length)
                self.DrawCannonBase(x + padding, top_pad + (vertical - y_gap)//4 + padding, x + padding, top_pad + (vertical - y_gap)//4 + padding + length)
                self.DrawCannonBase(x - padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding, x - padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding + length)
                self.DrawCannonBase(x + padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding, x + padding, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding + length)
                self.DrawCannonBase(x - padding - length + 2, top_pad + (vertical - y_gap)//4 - padding, x - padding + 2, top_pad + (vertical - y_gap)//4 - padding)
                self.DrawCannonBase(x + padding - 2, top_pad + (vertical - y_gap)//4 - padding, x + padding + length - 2, top_pad + (vertical - y_gap)//4 - padding)
                self.DrawCannonBase(x - padding - length + 2, top_pad + (vertical - y_gap)//4 + padding, x - padding + 2, top_pad + (vertical - y_gap)//4 + padding)
                self.DrawCannonBase(x + padding - 2, top_pad + (vertical - y_gap)//4 + padding, x + padding + length - 2, top_pad + (vertical - y_gap)//4 + padding)
                self.DrawCannonBase(x - padding - length + 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding, x - padding + 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding)
                self.DrawCannonBase(x + padding - 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding, x + padding + length - 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap - padding)
                self.DrawCannonBase(x - padding - length + 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding, x - padding + 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding)
                self.DrawCannonBase(x + padding - 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding, x + padding + length - 2, top_pad + (vertical - y_gap)//4 * 3 + y_gap + padding)
            if i == 3:
                self.DrawCannonBase(x, top_pad, x + x_gap, top_pad + y_gap)
                self.DrawCannonBase(x + x_gap, top_pad + y_gap, x, top_pad + 2 * y_gap)
                self.DrawCannonBase(x, top_pad + 7 * y_gap, x + x_gap, top_pad + 8 * y_gap)
                self.DrawCannonBase(x + x_gap, top_pad + 8 * y_gap, x, top_pad + 9 * y_gap)
            if i == 4:
                self.DrawCannonBase(x, top_pad + y_gap, x + x_gap, top_pad)
                self.DrawCannonBase(x, top_pad + y_gap, x + x_gap, top_pad + 2 * y_gap)
                self.DrawCannonBase(x, top_pad + 8 * y_gap, x + x_gap, top_pad + 7 * y_gap)
                self.DrawCannonBase(x, top_pad + 8 * y_gap, x + x_gap, top_pad + 9 * y_gap)

    def DrawPieces(self, piece_hori, piece_vert, screen, selectingPosition):
        if not self.game is None:
            board = self.game.board
            for position in board.positions:
                if not selectingPosition == position:
                    piece = board.pieces[position]
                    image = pygame.image.load(os.path.join(self.asset_path, piece.img))
                    image = pygame.transform.scale(image, (piece_vert, piece_hori))
                    screen.blit(image, self.PositionToLocation((piece.x, piece.y)))

    def GridPosition(self, location):
        x, y = location
        left_pad = self.width*0.03
        top_pad = self.height*0.03
        horizontal, vertical = self.width * 0.94 , self.height*0.94
        x_gap, y_gap = horizontal//8, vertical//9
        edge = min(y_gap//3, x_gap//3)
        x_step = (x - top_pad + edge)//x_gap
        y_step = (y - left_pad + edge)//y_gap
        return (int(x_step), int(y_step))   

    def PositionToLocation(self, position):
        x, y = position
        left_pad = self.width*0.03
        top_pad = self.height*0.03
        horizontal, vertical = self.width * 0.94 , self.height*0.94
        x_gap, y_gap = horizontal//8, vertical//9
        piece_hori, piece_vert = self.width//10, self.height//10
        x = left_pad + x * x_gap - piece_hori//2
        y = top_pad + (9 - y) * y_gap - piece_vert//2
        return (int(x), int(y))
    
    def DrawLine(self, x1, y1, x2, y2):
        pygame.draw.line(self.screen, (0, 0, 0), (x1, y1), (x2, y2), width=10)

    def DrawCannonBase(self, x1, y1, x2, y2):
        pygame.draw.line(self.screen, (0, 0, 0), (x1, y1), (x2, y2), width=5)

    def Position(self, position):
        x, y = position[0], position[1]
        return (x, self.height - y)