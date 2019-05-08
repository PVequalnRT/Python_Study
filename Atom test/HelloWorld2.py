import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

class cal(object):
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

if __name__ == "__main__":
    print("정상작동")
