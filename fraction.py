class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def gcd(self):
        x = self.num
        y = self.den
        while(y):
            x, y = y, x % y
        return x

    def lowestForm(self):
        temp=self.gcd()
        if temp==1:
            x = self.num
            y = self.den
        else:
            x=self.num/temp
            y=self.den/temp
        return x, y


myfraction = Fraction(3, 75)
print myfraction.lowestForm()