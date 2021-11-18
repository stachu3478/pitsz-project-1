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

    def _randomize(self, total_processing_time=None, total_base_ready_time=None, min_window=0, max_window=0, min_ready_time_sub_rate=1.0, max_ready_time_sub_rate=1.0, weight_multiplier=random.randint(2, 10)):
        self.b = [1] + [1 + abs(random.normalvariate(0, 1)) for _ in range(3)]
        total_b =  sum(self.b)
        if total_processing_time is None:
            total_processing_time = random.randint(self.n ** 2, self.n ** 3)
        if max_ready_time_sub_rate is None:
            max_ready_time_sub_rate = min_ready_time_sub_rate + random.random() * ((int(math.sqrt(self.n) / total_b)) - min_ready_time_sub_rate)
        if max_window is None:
            max_window = random.randint(0, int(total_processing_time / self.n))
        if min_window is None:
            min_window = random.randint(0, max_window)
        if total_base_ready_time is None:
            total_base_ready_time = int(total_processing_time / total_b)
        machine_cuts = []
        cut_total = 0
        for i in range(3):
            cut_total += int(round(total_processing_time * self.b[i] / total_b))
            machine_cuts.append(cut_total)
        print(machine_cuts, total_processing_time)
        self.p, cuts = self._random_p(total_processing_time, cut_count=self.n - 4, cuts=machine_cuts)
        machine_cut_index = 0
        task_delay_change = 0
        machine_ids = []
        print([cuts.index(machine_cuts[i]) for i in range(3)])
        for i, cut in enumerate(cuts[1:]):
            if (machine_cut_index < 3) and (cut > machine_cuts[machine_cut_index]):
                task_delay_change = machine_cuts[machine_cut_index]
                machine_cut_index += 1
            cuts[i] -= task_delay_change
            machine_ids.append(machine_cut_index)
        #print(cuts)
        ready_time_sub_rate_min_to_max = max_ready_time_sub_rate - min_ready_time_sub_rate
        self.r = [max(0, round(cuts[i] / self.b[machine_ids[i]] - random.random() * ready_time_sub_rate_min_to_max)) for i, p in enumerate(self.p)]
        self.d = [self.r[i] + self.p[i] + random.randint(min_window, max_window) for i in self._task_range]
        self.w = [weight_multiplier ** math.floor(abs(random.normalvariate(0, 1))) for _ in self._task_range]
        print(machine_ids.count(0), machine_ids.count(0) + machine_ids.count(1), machine_ids.count(0) + machine_ids.count(1) + machine_ids.count(2), machine_ids.count(0) + machine_ids.count(1) + machine_ids.count(2) + machine_ids.count(3))
        shuffled_ids = [i for i in self._task_range]
        random.shuffle(shuffled_ids)
        self.p = [self.p[i] for i in shuffled_ids]
        self.r = [self.r[i] for i in shuffled_ids]
        self.d = [self.d[i] for i in shuffled_ids]
        self.w = [self.w[i] for i in shuffled_ids]
        