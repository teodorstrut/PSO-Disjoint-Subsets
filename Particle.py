from random import random

from Setup import Setup


class Particle:
    def __init__(self):
        self._s = Setup()
        length = len(self._s.getSet())
        # randomly generate byte array
        self.position = []
        for i in range(length):
            if random() > 0.5:
                self.position.append(0)
            else:
                self.position.append(1)
        # generate the velocity
        self._velocity = [random() for i in range(length)]
        # define best global,best neighbor and best personal
        self._bestGlobal = None
        self.bestPersonal = self.position
        self._bestFitness = self.fitness()

    def fitness(self):
        fit = 0
        set1 = set()
        set2 = set()
        l = list(self._s.getSet())

        for i in range(len(self._s.getSet())):
            if self.position[i] == 0:
                set1.add(l[i])
            else:
                set2.add(l[i])

        for i in self._s.getSubSets():
            if i.issubset(set1) or i.issubset(set2):
                fit -= 1

        return fit

    def setBestGlobal(self, particle):
        self._bestGlobal = particle.position

    def getBestGlobal(self):
        return self._bestGlobal

    def setBestPersonal(self, particle):
        self.bestPersonal = particle.position

    def getBestPersonal(self):
        return self.bestPersonal

    def getPosition(self):
        return self.position

    def evaluate(self):
        f = self.fitness()
        if (f > self._bestFitness):
            self.bestPersonal = self.position
            self._bestFitness = f

    def update(self, particle, w, c1, c2):
        for i in range(len(self.position)):
            val = w * self._velocity[i] + c1 * random() * Setup.xor(self._bestGlobal[i], self.position[
                i]) + c2 * random() * Setup.xor(particle.position[i], particle.bestPersonal[i])
            self._velocity[i] = val

        for i in range(len(self._velocity)):
            if random() < Setup.sigmoid(self._velocity[i]).real:
                self.position[i] = particle.position[i]
