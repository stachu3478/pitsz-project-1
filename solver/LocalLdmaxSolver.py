from solver.ProperSolver import ProperSolver

class LocalLdmaxSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        time = 0
        current_task = None
        for _ in range(instance.n):
            ld_max = None
            worst_task_i = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                cd = self.end_time(instance, time, current_task, i) - self.end_time(instance, 0, current_task, i)
                ld = cd - instance.d[i]
                if (ld_max is None) or (ld > ld_max):
                    worst_task_i = i
                    ld_max = ld
            task_order.append(worst_task_i)
            time = self.end_time(instance, time, current_task, worst_task_i)
            current_task = worst_task_i
            tasks_used[worst_task_i] = 1
        return task_order