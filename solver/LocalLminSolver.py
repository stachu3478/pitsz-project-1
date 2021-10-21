from solver.ProperSolver import ProperSolver

class LocalLminSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        time = 0
        current_task = None
        for _ in range(instance.n):
            l_min = None
            best_task_l = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                l = c - instance.d[i]
                if (l_min is None) or (l < l_min):
                    best_task_l = i
                    l_min = l
            task_order.append(best_task_l)
            time = self.end_time(instance, time, current_task, best_task_l)
            current_task = best_task_l
            tasks_used[best_task_l] = 1
        return task_order