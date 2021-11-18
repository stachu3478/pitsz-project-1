import math
import random

class Instance:
    def create(self, size):
        instance = self(size)
        instance._randomize()
        return instance

    def __init__(self, n=None):
        self.n = n
        if n is not None:
            self._set_n(n)
        

    def save(self, path):
        f = open(path, 'w')
        f.write(str(self.n) + '\n')
        f.write('\n'.join(map(lambda j: str(self.p[j]) + ' ' + str(self.r[j]) + ' ' + str(self.d[j]), self._task_range)) + '\n')
        f.write('\n'.join(map(lambda s_i: ' '.join(map(lambda s_i_j: str(s_i_j), s_i)), self.s)) + '\n')
        f.close()

    def load(self, path):
        f = open(path, 'r')
        self._set_n(int(f.readline().strip()))
        prds = [f.readline().strip().split(' ') for _ in self._task_range]
        for i, prd in enumerate(prds):
            self.p[i] = int(prd[0])
            self.r[i] = int(prd[1])
            self.d[i] = int(prd[2])
        self.s = [[s_i_j for s_i_j in map(lambda s_i_j: int(s_i_j), f.readline().strip().split(' '))] for _ in self._task_range]
        return self

    def _randomize(self, total_processing_time=None, total_base_ready_time=None, min_window=None, max_window=None, min_ready_time_sub_rate=1.0, max_ready_time_sub_rate=None, min_s=None, max_s=None):
        if total_processing_time is None:
            total_processing_time = random.randint(self.n ** 2, self.n ** 3)
        if total_base_ready_time is None:
            total_base_ready_time = total_processing_time
        if max_ready_time_sub_rate is None:
            max_ready_time_sub_rate = random.randint(min_ready_time_sub_rate, int(math.sqrt(self.n)))
        if min_window is None:
            min_window = random.randint(0, int(math.sqrt(total_processing_time)))
        if max_window is None:
            max_window = random.randint(min_window, total_processing_time)
        if min_s is None:
            min_s = random.randint(0, int(math.sqrt(min_window)))
        if max_s is None:
            max_s = random.randint(min_s, min_window)
        self.p = self._random_p(total_processing_time)
        ready_time_sub_rate_min_to_max = max_ready_time_sub_rate - min_ready_time_sub_rate
        self.r = [max(0, int(random.randint(0, total_base_ready_time) - self.p[i] * min_ready_time_sub_rate + random.random() * ready_time_sub_rate_min_to_max)) for i in self._task_range]
        self.d = [self.r[i] + self.p[i] + random.randint(min_window, max_window) for i in self._task_range]
        self.s = [[random.randint(min_s, max_s) for _ in self._task_range] for _ in self._task_range]
        for i in self._task_range:
            self.s[i][i] = 0
        

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
        return self._random_p(total_processing_time), total_processing_time_cuts

    def _set_n(self, n):
        self.n = n
        self._task_range = range(n)
        self.p = [0 for _ in self._task_range]
        self.r = [0 for _ in self._task_range]
        self.d = [0 for _ in self._task_range]
        self.s = [[0 for _ in self._task_range] for _ in self._task_range]



Instance.create = classmethod(Instance.create)