#this module contains .nec geometry, to simle use in main generator
from math import sqrt

class necLine:
    """Class for line, to use in GW  card of nec file"""
    def __init__ (self, start=[0,0,0], end=[0,0,0], segs=15, radius=0.002):
        self.start=start
        self.end=end
        self.segs=segs
        self.radius=radius
        
    def setStart (self, start):
        """Sets line start point [X,Y,Z]"""
        self.start=start
        
    def setEnd (self, end):
        """Sets line end point [X,Y,Z]"""
        self.end=end
        
    def setSegs (self, segs):
        """Sets line segments count int"""
        self.segs=segs
        
    def getStart (self):
        """Returns line start coords [X,Y,Z]""" 
        return self.start
        
    def getEnd (self):
        """Returns line end coords [X,Y,Z]"""
        return self.end
        
    def getSegs (self):
        """Returns line segments count int"""
        return self.segs
        
    def getLength (self):
        """Returns lenght of line float"""
        length_temp=0.0
        for i in range(3):
            length_temp+=(self.end[i]-self.start[i])**2
        return sqrt(length_temp)
        
