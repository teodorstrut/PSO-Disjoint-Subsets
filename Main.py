from Iteration import Iteration


class Main:
    def __init__(self, iterations):
        self._iterations = iterations
        self._iter = Iteration()

    def main(self):
        for i in range(self._iterations):
            self._iter.run()
        for i in self._iter.getSwarm():
            print(i.fitness(), i.position)


main = Main(6)
main.main()
