
class t :
    def __init__(self,y):
        self.y = y
class tt:
    def __init__(self, x):
        self.x = x
    def test(self):
        b = self.x
        self.x = t(2)
        print()
        print(b.y)


t1=t(1)
s = tt(t1)
s.test()