import math
import random

from generator.instance import Instance

class F4EDInstance(Instance):
    def _set_n(self, n):
        self.n = n
        self._task_range = range(n)
        self.a = [0 for _ in self._task_range]
        self.b = [0 for _ in self._task_range]
        self.d = [0 for _ in self._task_range]
        self.p = [[0 for _ in range(4)] for _ in self._task_range]

    def save(self, path):
        f = open(path, 'w')
        f.write(str(self.n) + '\n')
        f.write('\n'.join(map(lambda j: ' '.join(self.p[j]) + ' ' + str(self.d[j]) + ' ' + str(self.a[j]) + ' ' + str(self.b[j]), self._task_range)) + '\n')
        f.close()

    def load(self, path):
        f = open(path, 'r')
        self._set_n(int(f.readline().strip()))
        pdabs = [f.readline().strip().split(' ') for _ in self._task_range]
        for i, pdab in enumerate(pdabs):
            pdab.p[i] = [int(pdab[0]), int(pdab[1]), int(pdab[2]), int(pdab[3])]
            pdab.d[i] = int(pdab[4])
            pdab.a[i] = int(pdab[5])
            pdab.b[i] = int(pdab[6])
        return self

    def _randomize(self, total_processing_time=None, min_dd=None, max_dd=None, weight_multiplier=random.randint(2, 10)):
        if total_processing_time is None:
            total_processing_time = random.randint(self.n ** 2, self.n ** 3)
        if max_dd is None:
            max_dd = random.randint(0, int(total_processing_time / self.n))
        if min_dd is None:
            min_dd = random.randint(0, min_dd)
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
        