import math
import random

class BaseInstance:
    def create(self, size):
        instance = self(size)
        instance.randomize()
        return instance

    def __init__(self, n=None):
        self.n = n
        if n is not None:
            self.set_n(n)
        

    def save(self, path):
        f = open(path, 'w')
        f.write(str(self.n) + '\n')
        self.write()
        f.close()

    def load(self, path):
        f = open(path, 'r')
        self._set_n(int(f.readline().strip()))
        self.read()
        return self

    def _random_p(self, total_processing_time):
        total_processing_time_cuts = [0]
        for _ in range(self.n - 1):
            total_processing_time_cuts.append(random.randint(0, total_processing_time))
        total_processing_time_cuts.sort()
        total_processing_time_cuts.append(total_processing_time)
        p = [total_processing_time_cuts[i + 1] - total_processing_time_cuts[i] for i in self._task_range]
        try:
            p.index(0) # should not have any 0 time tasks
        except ValueError:
            return p
        return self._random_p(total_processing_time)

    def set_n(self, n):
        self.n = n
        self._task_range = range(n)
        self.p = [0 for _ in self._task_range]

    def randomize(self):
        raise NotImplementedError('Abstract method!')

    def write(self):
        raise NotImplementedError('Abstract method!')

    def read(self):
        raise NotImplementedError('Abstract method!')


BaseInstance.create = classmethod(BaseInstance.create)