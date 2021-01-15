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


def check(symbolString):
    s=stack()
    balance=True
    index=0
    while index < len(symbolString) and balance:
        symbol=symbolString[index]
        if symbol=='(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance=False
            else:
                s.pop()

        index += 1

    if balance and s.isEmpty():
         return True
    else:
         return False


print(check('(((')) #false
print(check('(())(')) #false
