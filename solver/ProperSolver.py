from solver.Solver import Solver

class ProperSolver(Solver):
    def l_max(self, instance, task_order):
        l_max = None
        time = 0
        current_task = None
        for i in task_order:
            time = max(time, instance.r[i])
            if current_task is not None:
                time += instance.s[current_task][i]
            time += instance.p[i]
            l = time - instance.d[i]
            if l_max is None:
                l_max = l
            else:
                l_max = max(l_max, l)
            current_task = i
        return l_max
        