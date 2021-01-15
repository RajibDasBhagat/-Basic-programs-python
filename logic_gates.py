class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(raw_input("Enter PinA:"+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(raw_input("Enter PinB:"+ self.getLabel()+"-->"))

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None

    def getPin(self):
        return int(raw_input("Enter Pin input: "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPin()
        if a==0:
            return 1
        else:
            return 0

class NandGate(BinaryGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 1
        else:
            return 0

class HalfAdder(BinaryGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if (a==0 and b==0) or (a==1 and b==1):
            return 0
        else:
            return 1

g1 = AndGate("G1")
print "And: ",g1.getOutput()

g2 = OrGate("G2")
print "Or: ",g2.getOutput()

g3 = NotGate("G3")
print "Not: ",g3.getOutput()

g4 = NandGate("G4")
print "Nand: ",g4.getOutput()

g5 = NorGate("G5")
print "Nor: ",g5.getOutput()

g6 = HalfAdder("G6")
print "HalfAdder: ", g6.getOutput()
