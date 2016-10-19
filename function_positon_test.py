# if function is used before being defined, there is error

x = 2
y = 3

# print add(x,y)

def add(x,y):
    return x+y

class Add(object):
    x = 2
    y = 3
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.val = self.addtwo(x,y)

    def __repr__(self, val):
        return self.val

    def addtwo(self,x,y):
        return (x + y)

print Add(x,y).val