from util import MouseMode as mMode


class ActionManager:

    def __init__(self) -> None:
        self.mouse_mode = mMode.MouseMode.eNothing

    # Main
    def doService(self, gesture):
        self.setPlaymode(gesture['MouseMode'])

        mgesture = {0:self.doNothing(), 1:self.doPagescroll(), 2:self.doClick(), 3:self.doForwardPage(), 4:self.doBackPage(), 5:self.doMouseControl()}
        
        mgesture[self.mouse_mode.value]
        
        return


    def setPlaymode(self, MouseMode=None):
        self.mouse_mode = MouseMode


    def getPlaymode(self):
        return self.mouse_mode


    def doNothing(self):
        return 'nothing'


    def doPagescroll(self):
        return 'pscroll'


    def doClick(self):
        return 'click'


    def doForwardPage(self):
        return 'forward'
    

    def doBackPage(self):
        return 'back'


    def doMouseControl(self):
        return 'mouse'
