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

    def printAll(self):
        while self.size()>0:
            print(self.pop(), end='')


def main():
    s=stack()

    #print forward and backward
    
    index=0
    mystr="RAJIB"
    for i in range(len(mystr)):
        s.push(mystr[i])
        print(mystr[i], end='')
    print("\n")
    #s.push("D")
    #s.push("A")
    #s.push("S")

    #print(s.peek())
    s.printAll()





main()