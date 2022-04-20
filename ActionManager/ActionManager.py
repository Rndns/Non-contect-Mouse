from util import MouseMode as mMode
import pyautogui as pag


class ActionManager:

    def __init__(self) -> None:
        self.mouse_mode = mMode.MouseMode.eNothing

    # Main
    def doService(self, gesture):
        point_history = gesture['point_history']
        x_loc = point_history[-1][0]
        y_loc = point_history[-1][1]

        mgesture = {0:self.doNothing(), 1:self.doPagescroll(x_loc, y_loc), 2:self.doClick(x_loc, y_loc), 3:self.doForwardPage(), 4:self.doBackPage(), 5:self.doMouseControl(x_loc, y_loc)}
        self.setPlaymode(gesture['MouseMode'])
        mgesture[self.mouse_mode.value]
        

    def setPlaymode(self, MouseMode=None):
        self.mouse_mode = MouseMode


    def getPlaymode(self):
        return self.mouse_mode


    def doNothing(self):
        return


    def doPagescroll(self, x_loc, y_loc):
        pag.dragTo(x_loc, y_loc, button='middle')
        return


    def doClick(self, x_loc, y_loc):
        pag.click(x=x_loc, y=y_loc, button='right')
        return


    def doForwardPage(self):
        pag.keyDown('alt')
        pag.press('right')
        pag.keyUp('alt')
        return
    

    def doBackPage(self):
        pag.keyDown('alt')
        pag.press('left')
        pag.keyUp('alt')
        return


    def doMouseControl(self, x_loc, y_loc):
        pag.moveTo(x_loc, y_loc)
        return
