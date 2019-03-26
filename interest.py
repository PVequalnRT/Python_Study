class calc(object) :
    def __init__(self, money, interest) :
        self.money = money
        self.interest = 0.01 * interest

    def total(self) :
        temp = self.money*self.interest*(1/12)

        i = 0
        total = 0
    
        while i < 12 :
            i += 1
            total+=100000
            total+=temp*i

        return total

money = int(input())
interest = int(input())
c1 = calc(money, interest)

print(c1.total())
