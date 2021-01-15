class stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def divideBy2(decNum,base):
    s=stack()

    while(decNum > 0):
        rem = decNum % base
        s.push(rem)
        decNum=decNum/base

    binstring=" "
    while not s.isEmpty():
        binstring=binstring+str(s.pop())
    return binstring


print(divideBy2(26,26))