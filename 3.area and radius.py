class area:
          def __init__(self,a):
                    self.a=a
          def sarea(self):
                    c=self.a*self.a
                    return c
narea=area(10)
print("area value = 10")
print("use area to find square area = ",narea.sarea())
class perimeter:
          def __init__(self,p):
                    self.p=p
          def r(self):
                    r1=self.p/3.14
                    return r1
radius=perimeter(501)
print("perimeter value = 501")
print("use perimeter to find radius = ",radius.r())
