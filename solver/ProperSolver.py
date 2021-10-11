from solver.Solver import Solver

class ProperSolver(Solver):
    def l_max(self, instance, task_order):
        l_max = None
        time = 0
        current_task = None
        for i in task_order:
            wait_time = max(0, instance.r[i] - time)
            active_switch_time = 0
            if current_task is not None:
                active_switch_time = max(0, instance.s[current_task][i] - wait_time)
            time += wait_time + active_switch_time + instance.p[i]
            l = time - instance.d[i]
            if l_max is None:
                l_max = l
            else:
                l_max = max(l_max, l)
            current_task = i
        return l_max
        