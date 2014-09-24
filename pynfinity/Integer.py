class Integer:
    BASE = 10

    def __init__(self, num=""):

        self.storage = []
        if num != "" and num != "0":
            for i in reversed(range(len(num))):
                self.storage.append(ord(num[i]) - ord("0"))

    def __add__(self, other):

        """ Add two arbitrary-precision integer
        """
        i = 0
        carry = 0
        res = Integer()
        while i < len(self.storage) or i < len(other.storage) or carry != 0:
            carry = carry + (self.storage[i] if i < len(self.storage) else 0) + (
                other.storage[i] if i < len(other.storage) else 0)
            res.storage.append(carry % self.BASE)
            carry /= self.BASE
            i += 1

        return res

    def __repr__(self):

        return "Integer" "(" + str(self) + ")"

    def __str__(self):

        return ''.join(str(x) for x in reversed(self.storage))