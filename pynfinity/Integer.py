class Integer(object):
    BASE = 10

    def __init__(self, num=""):

        self.storage = []
        for i in reversed(range(len(num))):
            self.storage.append(ord(num[i]) - ord("0"))
        while len(self) > 0 and self[-1] == 0:
            self.storage.pop()

    def __len__(self):

        return len(self.storage)

    def __getitem__(self, index):

        return self.storage[index]

    def iszero(self):

        return len(self) == 0

    def __add__(self, other):

        """ Add two Integer objects
        :param other: Integer
        :return: Integer storing the result of add
        """
        i = 0
        carry = 0
        res = Integer()
        while i < len(self.storage) or i < len(other.storage) or carry != 0:
            carry = carry + (self.storage[i] if i < len(self.storage) else 0) +\
                (other.storage[i] if i < len(other.storage) else 0)
            res.storage.append(carry % self.BASE)
            carry /= self.BASE
            i += 1

        return res

    def __sub__(self, other):

        """ Subtract two Integer objects
        :param other: Integer
        :return: Integer storing the result of subtract
        """
        res = Integer()
        t = 0
        for i in range(len(self)):

            res.storage.append(self[i] - (other[i] if i < len(other) else 0) - t)
            if res[-1] < 0:
                t = 1
                res.storage[-1] += self.BASE
            else:
                t = 0

        while len(res) > 0 and res[-1] == 0:
            res.storage.pop()

        if t < 0:
            return None
        return res

    def __mul__(self, other):

        """ Multiply two Integer objects
        :param other: Integer
        :return: Integer storing the result of multiply
        """
        res = Integer()
        a = 0
        for i in range(len(self)):

            b = a
            j = 0
            t = 0
            while j < len(other) or t > 0:

                if b >= len(res):
                    res.storage.append(0)
                t += res[b] + (self[i] * other[j] if j < len(other) else 0)
                res.storage[b] = t % self.BASE
                b += 1
                t /= self.BASE
                j += 1
            a += 1

        return res

    def __divmod__(self, other):

        """ Quotient and remainder of two Integer objects
        :param other: Integer
        :return: (Integer, Integer) storing the quotient and remainder respectively
        """
        if other.iszero():
            return None, None

        div, mod = Integer(), Integer()

        for i in reversed(range(len(self))):

            div.storage.append(0)
            mod.storage.insert(0, self[i])
            while mod >= other:
                div.storage[-1] += 1
                mod = mod.__sub__(other)

        div.storage = div.storage[::-1]
        while len(div) > 0 and div[-1] == 0:
            div.storage.pop()

        return div, mod

    def __div__(self, other):

        return self.__divmod__(other)[0]

    def __mod__(self, other):

        return self.__divmod__(other)[1]

    def __eq__(self, other):

        return self.__cmp__(other) == 0

    def __le__(self, other):

        return self.__cmp__(other) < 1

    def __ge__(self, other):

        return self.__cmp__(other) > -1

    def __lt__(self, other):

        return self.__cmp__(other) == -1

    def __gt__(self, other):

        return self.__cmp__(other) == 1

    def __cmp__(self, other):

        if len(self) < len(other):
            return -1
        elif len(self) > len(other):
            return 1
        else:
            for i in range(len(self)):
                if self[i] < other[i]:
                    return -1
                if self[i] > other[i]:
                    return 1
            return 0

    def __repr__(self):

        return "Integer" "(" + str(self) + ")"

    def __str__(self):

        return ''.join(str(x) for x in reversed(self.storage))