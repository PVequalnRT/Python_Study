import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')



import HelloWorld2

class cal2(HelloWorld2.cal) :
    def subtract(self):
        return self.num1 - self.num2

c = cal2(10,7)
print(c.subtract())
print(c.add())
