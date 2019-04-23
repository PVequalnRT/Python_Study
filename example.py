"""
class Foo:
    def moo(self):
        return 1

class Boo(Foo):
    def zoo(self):
        return 2

obj = Boo()

r1 = obj.moo()
r2 = obj.zoo()
#"""

"""
a = [2,7,1,7,4]
r1 = a.index(7)
r2 = a.index(7, 2)
r3 = a.count(7)
#"""


a = [3,2]
r = [1,4]

if a[1] < r[1]:
    r.append(a)
else:
    r.append([5,6])
