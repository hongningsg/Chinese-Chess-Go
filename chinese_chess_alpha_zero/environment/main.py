import Game.Scripts.Script as Script
import Game.Scripts.SoldierScript as SoldierScript
import Game.Scripts.CannonScript as CannonScript
import Game.Scripts.HorseScript as HorseScript
import Game.Scripts.ElephantScript as ElephantScript
import Game.Scripts.GeneralScript as GeneralScript
import Game.Scripts.ChariotScript as ChariotScript
import Game.Scripts.GuardScript as GuardScript
import Game.Scripts.BoardScript as BoardScript
import Game.GUI.BoardGUI as BoardGUI

if __name__ == '__main__':
    # Script.PlayScript(BoardScript.BoardScript1)
    gui = BoardGUI.BoardGUI()
    gui.Start()