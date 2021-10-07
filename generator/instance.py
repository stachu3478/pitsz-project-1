import math
import random

class Instance:
    def create(self, size):
        instance = Instance(size)
        return instance

    def __init__(self, n):
        self.n = n
        self._task_range = range(n)
        self.p = [0 for _ in self._task_range]
        self.r = [0 for _ in self._task_range]
        self.d = [0 for _ in self._task_range]
        self.s = [[0 for _ in self._task_range] for _ in self._task_range]

    def save(self, path):
        f = open(path, "w")
        f.write(str(self.n) + '\n')
        f.write('\n'.join(map(lambda j: str(self.p[j]) + ' ' + str(self.r[j]) + ' ' + str(self.d[j]), self._task_range)) + '\n')
        f.write('\n'.join(map(lambda s_i: ' '.join(s_i))) + '\n')
        f.close()

    def _randomize(self, total_processing_time=None, min_window=None, max_window=None, min_ready_time_add=None, max_ready_time_add=None, min_min_s=None, min_max_add_s=None, max_min_add_s=None, max_max_add_s=None):
        if total_processing_time is None:
            total_processing_time = random.randint(self.n ** 2, self.n ** 3)
        if min_ready_time_add is None:
            min_ready_time_add = random.randint(0, math.sqrt(total_processing_time))
        if max_ready_time_add is None:
            max_ready_time_add = random.randint(0, total_processing_time)
        if min_window is None:
            min_window = random.randint(0, math.sqrt(total_processing_time))
        if max_window is None:
            max_window = random.randint(0, total_processing_time)
        # todo s + impl.


Instance.create = classmethod(Instance.create)