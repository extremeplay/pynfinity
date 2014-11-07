from pynfinity import Integer


def gcd(a, b):
    if a == Integer("0") and b == Integer("0"):
        raise Exception("gcd(0,0) is undefined")
    return gcdHelper(a, b)


def gcdHelper(a, b):
    if b == Integer("0"):
        return a
    return gcdHelper(b, a % b)


def lcm(a, b):
    return a * b / gcd(a,b)