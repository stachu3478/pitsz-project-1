from solver.Solver import Solver

class ProperSolver(Solver):
    def l_max(self, instance, task_order):
        l_max = None
        worst_task = None
        time = 0
        current_task = None
        for i in task_order:
            time = self.end_time(instance,  time, current_task, i)
            l = time - instance.d[i]
            if (l_max is None) or (l > l_max):
                l_max = l
                worst_task = i
            current_task = i
        return l_max#, worst_task

    def end_time(self, instance, time, current_task, next_task):
        wait_time = max(0, instance.r[next_task] - time)
        active_switch_time = 0
        if current_task is not None:
            active_switch_time = max(0, instance.s[current_task][next_task] - wait_time)
        return time + wait_time + active_switch_time + instance.p[next_task]

    def lower_bound(self, instance):
        return min([instance.r[i] + instance.p[i] - instance.d[i] for i in range(instance.n)])