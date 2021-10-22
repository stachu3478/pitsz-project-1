from solver.ProperSolver import ProperSolver

class LocalLdmax0CminSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        time = 0
        current_task = None
        for _ in range(instance.n):
            ld_max = None
            worst_task_i = None
            c_min = None
            best_c = None
            l_max = None
            best_task = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                cd = c - self.end_time(instance, 0, current_task, i)
                ld = cd - instance.d[i]
                l = c - instance.d[i]
                if (ld_max is None) or (ld > ld_max):
                    worst_task_i = i
                    ld_max = ld
                    l_at = l
                if (l_max is None) or (l > l_max):
                    l_max = l
                if (c_min is None) or (c < c_min):
                    best_c = i
                    c_min = c
            if l_max < 0:
                best_task = best_c
                print('on time')
            else:
                best_task = worst_task_i
                print('late')
            print('ld_max ' + str(ld_max) + " l " + str(self.end_time(instance, time, current_task, best_task) - instance.d[best_task]))
            task_order.append(best_task)
            time = self.end_time(instance, time, current_task, best_task)
            current_task = best_task
            tasks_used[best_task] = 1
        return task_order