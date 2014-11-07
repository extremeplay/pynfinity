from pynfinity.Integer import Integer
from numbertheory.Algorithms import lcm, gcd

class Rational(object):
    def __init__ (self, up = Integer("0"), down = Integer("1")):
        self.up = up
        self.down = down

    def __add__(self, other):
        return Rational( self.up + other.up, lcm(self.down + other.down) )
        pass

    def __sub__(self, other):
        raise Exception("Not yet supported")

    def __mul__(self, other):
        up, down = self.up * other.up, self.down * other.down
        return Rational (up / gcd(up, down), down / gcd(up, down))
        pass