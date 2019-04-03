from md1 import geo

class geo2(geo):
    def __init__(self,wit,high) :
        super().__init__(wit,high)

    def add(self):
        return self.wit + self.high


a = geo2(3,5)

print(a.multiply())
print(a.add())
