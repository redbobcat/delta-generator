#this module contains .nec geometry, to simle use in main generator

class necLine:
    def __init__ (self, start=[0,0,0], end=[0,0,0], segs=15, radius=0.002):
        self.start=start
        self.end=end
        self.segs=segs
        self.radius=radius
        
    def setStart (self, start):
        self.start=start
        
    def setEnd (self, end):
        self.end=end
        
    def setSegs (self, segs):
        self.segs=segs
        
    def getStart (self):
        return self.start
        
    def getEnd (self):
        return self.end
        
    def getSegs (self):
        return self.segs
        
    def getLenght (self):
        
