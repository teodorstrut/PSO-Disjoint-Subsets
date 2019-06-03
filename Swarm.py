from Particle import Particle


class Swarm:
    def __init__(self, num):
        self._particles = []
        for i in range(num):
            self._particles.append(Particle())

    def getSwarm(self):
        return self._particles

    def getBestParticle(self):
        return max(self._particles, key=lambda p: p.fitness())

s=Swarm(10)
