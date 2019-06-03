from Swarm import Swarm


class Iteration:
    def __init__(self):
        self._swarm=Swarm(10)
        self._w = 0.15
        self._c1 = 0.15
        self._c2 = 0.15

    def run(self):
        bestParticle = self._swarm.getBestParticle()
        for p in self._swarm.getSwarm():
            p.setBestGlobal(bestParticle)

        for p in self._swarm.getSwarm():
            p.update(bestParticle,self._w,self._c1,self._c2)
            p.evaluate()

    def getSwarm(self):
        return self._swarm.getSwarm()