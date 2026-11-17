#ideas
#custom exception for popping from empty Treque
#BIG  all other methods from deque, rotate, maxlen, slicin, remove(x) removes the first x
#instead of reversing whole thing, reverse from both ends to the middle
#e.g. 20,40,80,60,30
#sorted(deque)
#deque comprehension
#peek?
#quadreque
#all types in one
#keque
#wreque
#heque
#peque
#cheque
#beque
#greque
#meque
#jeque

from collections import deque 
from functools import total_ordering
# dir(deque)

class Treque:
    #right-facing implemented Treque

    def __init__(self, data=None):
        self.dl = deque()
        self.dr = deque()
        if isinstance(data, (list, tuple, set)):
            for i in data: self.append(i)
        else:
            if data is not None: self.append(data)

    def __len__(self):
        return len(self.dl) + len(self.dr)
    
    def __iter__(self):   
        for i in self.dl: yield i
        for i in self.dr: yield i    

    def display(self):
        print(f"{list(self.dl)} {list(self.dr)}")

    def __str__(self):
        return f"{list(self.dl)} {list(self.dr)}"

    def balance(self):
        if(len(self.dr) > len(self.dl) + 1):
            self.dl.append(self.dr.popleft())
        elif(len(self.dl) > len(self.dr) + 1):
            self.dr.appendleft(self.dl.pop())

    #def extend(self, data):

    #def extendleft(self, data):

    def append(self, data):
        self.dr.append(data)
        self.balance()
    
    def appendleft(self, data):
        self.dl.appendleft(data)
        self.balance()
    
    def appendmid(self, data, mode="r"):
        if(mode in ("l","left",0)):
            self.dl.append(data)
        elif(mode in ("r","right",1)):
            self.dr.appendleft(data)
        elif(mode in ("m","mid","middle",2)):
            if isinstance(data, (list, tuple, set)):
                if(len(data)==2):
                    dl.append(data[0])
                    dr.appendleft(data[1])
                else:
                    print("bruh length of data is not 2...")
            else:
                dl.append(data)
                dr.appendleft(data)
        else:
            print("bruh invalid mode")
        self.balance()

    def pop(self):
        if(len(self.dr) > 0):
            popped = self.dr.pop()
            self.balance()
            return popped
        elif(len(self.dl) > 0):
            return self.dl.pop()
        else:
            print("bruh popping from empty Treque")
    
    def popleft(self):
        if(len(self.dl) > 0):
            popped = self.dl.popleft()
            self.balance()
            return popped
        elif(len(self.dr) > 0):
            return self.dr.popleft()
        else:
            print("bruh popping from empty Treque")
    
    def popmid(self, mode="l"):
        #odd length
        if(len(self.dl) > len(self.dr)):
            return self.dl.pop()
        elif(len(self.dl) < len(self.dr)):
            return self.dr.popleft()
        #even length
        else:
            if len(self)==0:
                print("bruh popping from empty Treque")
                return
            if(mode in ("l","left",0)):
                return self.dl.pop()
            elif(mode in ("r","right",1)):
                return self.dr.popleft()
            elif(mode in ("m","mid","middle",2)):
                return [self.dl.pop(), self.dr.popleft()]
            else:
                print("bruh invalid mode")

    def __eq__(self, other):
        if not isinstance(other, Treque):
            return NotImplemented
        return len(self) == len(other)

    def __lt__(self, other):
        if not isinstance(other, Treque):
            return NotImplemented
        return len(self) < len(other)

    def __getitem__(self, key):
        # 0 1 2 | 3 4
        # a b c | d e
        if(key < 0 or key > len(self)-1):
            print("bruh invalid index")
            return
        if(key <= len(self.dl)-1):
            return self.dl[key]
        else:
            return self.dr[key - len(self.dl)]

    def __setitem__(self, key, value):
        if(key < 0 or key > len(self)-1):
            print("bruh invalid index")
            return
        if(key <= len(self.dl)-1):
            self.dl[key] = value
        else:
            self.dr[key - len(self.dl)] = value
    
    def __delitem__(self, key):
        if(key < 0 or key > len(self)-1):
            print("bruh invalid index")
            return
        if(key <= len(self.dl)-1):
            del self.dl[key]
        else:
            del self.dr[key - len(self.dl)]
    


