import math

class Line:
    def __init__(self, xcoordinate1, xcoordinate2, ycoordinate1, ycoordinate2):
        self.xcoordinate1 = xcoordinate1
        self.ycoordinate1 = ycoordinate1
        self.xcoordinate2 = xcoordinate2
        self.ycoordinate2 = ycoordinate2
    def slope(self):
        slope = (self.ycoordinate1 - self.ycoordinate2) / (self.xcoordinate1 - self.xcoordinate2)
        return(str(slope))
    def length(self):
        length = math.sqrt((self.xcoordinate2 - self.xcoordinate1)**2 + (self.ycoordinate2 - self.ycoordinate1)**2)
        return(str(length))

line1 = Line(2,1,6,5,)
print(line1.slope())
print(line1.length())