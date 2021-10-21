from solver.ProperSolver import ProperSolver

class LocalCdmaxCminSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        time = 0
        current_task = None
        for _ in range(instance.n):
            cd_max = None
            worst_task_cd = None
            c_min = None
            best_task_c = None
            best_task = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                cd = c - self.end_time(instance, 0, current_task, i)
                if (cd_max is None) or (cd > cd_max):
                    worst_task_cd = i
                    cd_max = cd
                if (c_min is None) or (c < c_min):
                    best_task_c = i
                    c_min = c
            if cd_max == 0:
                best_task = best_task_c
            else:
                best_task = worst_task_cd
            print("cdmax " + str(cd_max) + " cmin " + str(c_min))
            task_order.append(best_task)
            time = self.end_time(instance, time, current_task, best_task)
            current_task = best_task
            tasks_used[best_task] = 1
        return task_order