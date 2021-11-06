import math
import random

from generator.instance import Instance

class Q4rwuInstance(Instance):
    def _set_n(self, n):
        self.n = n
        self._task_range = range(n)
        self.b = [1.0 for _ in range(4)]
        self.p = [0 for _ in self._task_range]
        self.r = [0 for _ in self._task_range]
        self.d = [0 for _ in self._task_range]
        self.w = [0 for _ in self._task_range]

    def save(self, path):
        f = open(path, 'w')
        f.write(str(self.n) + '\n')
        f.write(' '.join(map(lambda b: str(b), self.b)) + '\n')
        f.write('\n'.join(map(lambda j: str(self.p[j]) + ' ' + str(self.r[j]) + ' ' + str(self.d[j]) + ' ' + str(self.w[j]), self._task_range)) + '\n')
        f.close()

    def load(self, path):
        f = open(path, 'r')
        self._set_n(int(f.readline().strip()))
        self.b = [b for b in map(lambda b: float(b), f.readline().strip().split(' '))]
        prdws = [f.readline().strip().split(' ') for _ in self._task_range]
        for i, prdw in enumerate(prdws):
            self.p[i] = int(prdw[0])
            self.r[i] = int(prdw[1])
            self.d[i] = int(prdw[2])
            self.w[i] = int(prdw[3])
        return self

    def _randomize(self, total_processing_time=None, total_base_ready_time=None, min_window=None, max_window=None, min_ready_time_sub_rate=1.0, max_ready_time_sub_rate=None, weight_multiplier=random.randint(2, 10)):
        if total_processing_time is None:
            total_processing_time = random.randint(self.n ** 2, self.n ** 3)
        if max_ready_time_sub_rate is None:
            max_ready_time_sub_rate = random.randint(min_ready_time_sub_rate, int(math.sqrt(self.n)))
        if min_window is None:
            min_window = random.randint(0, int(math.sqrt(total_processing_time)))
        if max_window is None:
            max_window = random.randint(min_window, total_processing_time)
        self.b = [1] + [1 + abs(random.normalvariate(0, 1)) for _ in range(3)]
        total_b =  sum(self.b)
        if total_base_ready_time is None:
            total_base_ready_time = int(total_processing_time / total_b)
        self.p = self._random_p(total_processing_time)
        ready_time_sub_rate_min_to_max = max_ready_time_sub_rate - min_ready_time_sub_rate
        self.r = [max(0, int(random.randint(0, total_base_ready_time) - self.p[i] * min_ready_time_sub_rate + random.random() * ready_time_sub_rate_min_to_max)) for i in self._task_range]
        self.d = [self.r[i] + self.p[i] + random.randint(min_window, max_window) for i in self._task_range]
        self.w = [weight_multiplier ** math.floor(abs(random.normalvariate(0, 1))) for _ in self._task_range]
        