from solver.Solver import Solver

class ProperSolver(Solver):
    def l_max(self, instance, task_order):
        l_max = None
        time = 0
        current_task = None
        for i in task_order:
            time = self.end_time(instance,  time, current_task, i)
            l = time - instance.d[i]
            if l_max is None:
                l_max = l
            else:
                l_max = max(l_max, l)
            current_task = i
        return l_max

    def end_time(self, instance, time, current_task, next_task):
        wait_time = max(0, instance.r[next_task] - time)
        active_switch_time = 0
        if current_task is not None:
            active_switch_time = max(0, instance.s[current_task][next_task] - wait_time)
        return time + wait_time + active_switch_time + instance.p[next_task]