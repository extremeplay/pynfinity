class Integer:
    BASE = 10

    def __init__(self, num=""):

        self.storage = []
        if num != "" and num != "0":
            for i in reversed(range(len(num))):
                self.storage.append(ord(num[i]) - ord("0"))

    def __len__(self):
        return len(self.storage)

    def __getitem__(self, index):
        return self.storage[index]

    def __add__(self, other):
        """ Add two Integer objects
        :param other: Integer
        :return: Integer storing the result of add
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
                t /= 10
                j += 1
            a += 1

        return res

    def __eq__(self, other):
        return self.storage == other.storage

    def __repr__(self):

        return "Integer" "(" + str(self) + ")"

    def __str__(self):

        return ''.join(str(x) for x in reversed(self.storage))