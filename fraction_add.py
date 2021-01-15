class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def check(self):
        n = self.num
        d = self.den

        if type(n) != int or type(d) != int:
            n=int(n)
            d=int(d)
            return n,d
        else:
            return n,d

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

    def __add__(self, other):

        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):

        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum=self.num*other.num
        newden=self.den*other.den
        return Fraction(newnum,newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __gt__(self, other):

        f1=float(self.num)/self.den
        f2= float(other.num)/other.den
        print f1, f2
        if f1>f2:
            print "First fraction is greater than second!"
        elif f1<f2:
            print  "Second fraction is greater than first!"
        else:
            print "both equal"

def main():
    try:
        #user inputs
        num1=int(raw_input("num1:"))
        den1=int(raw_input("den1:"))
        num2=int(raw_input("num2:"))
        den2=int(raw_input("den2:"))
        #print type(num1)
        #object creation
        myf1 = Fraction(num1, den1)
        myf2 = Fraction(num2, den2)
        #to simple form
        print myf1.lowestForm()
        print myf2.lowestForm()
        #add
        f3 = myf1 + myf2
        print "add:" + str(f3.lowestForm())
        #sub
        f3 = myf1 - myf2
        print "sub:" + str(f3.lowestForm())
        #mul
        f3 = myf1 * myf2
        print "mul:" + str(f3.lowestForm())
        #div
        f3 = myf1.__truediv__(myf2)
        print "div:" + str(f3.lowestForm())
        #compare
        f3 = myf1.__gt__(myf2)
        str(f3)

    except:
        print "Invalid input! Please try again."
        main()

main()

