
class MathDojo(object):
    def __init__(self):
         self.result = 0

    def add(self, *x):
        self.addThis = 0
        for value in x:
                self.addThis += value
         self.result += self.addThis
         return self

    def subtract(self, *y):
         self.subThis = 0
            for value in y:
                self.subThis += value
         self.result -= self.subThis
        return self
md = MathDojo().add(2).add(2,5).subtract(3,2).result


print (md)
