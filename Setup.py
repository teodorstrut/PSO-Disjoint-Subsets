from cmath import exp


class Setup:
    def __init__(self):
        self._set = {}
        self._subsets = []
        f = open("data.in", "r")
        list = f.readline().strip().split(",")
        self._set = {int(i) for i in list[:]}

        for i in f.readlines():
            if i[0] == '':
                break
            l = i.strip().split(",")
            subset = {int(i) for i in l[:]}
            self._subsets.append(subset)

    def getSet(self):
        return self._set

    def getSubSets(self):
        return self._subsets

    @staticmethod
    def xor(a: int, b: int):
        if (a == 0 and b == 0):
            return 0
        elif (a == 0 and b == 1):
            return 1
        elif (a == 1 and b == 0):
            return 1
        elif (a == 1 and b == 1):
            return 0

    @staticmethod
    def sigmoid(i):
        return 1 / (1 + exp(-i))
