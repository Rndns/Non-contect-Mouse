import util.MouseMode as mMode


class ActionManager:

    def __init__(self) -> None:
        self.mouse_mode = mMode.MouseMode.eNothing

    def searchService(self):
        mDict = {0:self.doPagescroll(), 1:self.doNoting(), 2:self.doClick(), 3:self.doForwardPage(), 4:self.doBackPage(), 5:self.doMouseControl()}
        return mDict[self.mouse_mode.value]

    def setPlaymode(self, MouseMode=None):
        self.mouse_mode = MouseMode

    def getPlaymode(self):
        return self.mouse_mode

    def doPagescroll(self):
        pass

    def doNoting(self):
        pass

    def doClick(self):
        pass

    def doForwardPage(self):
        pass
    
    def doBackPage(self):
        pass

    def doMouseControl(self):
        pass
