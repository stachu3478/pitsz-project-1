from solver.ProperSolver import ProperSolver

class LocalCminSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        time = 0
        current_task = None
        for j in range(instance.n):
            c_min = None
            best_task = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                if (c_min is None) or (c < c_min):
                    best_task = i
                    #print("Default c " + str(best_task_l))
                    c_min = c
            #print("best " + str(j) + " task " + str(best_task))
            #print("lmax " + str(l_max))
            time = self.end_time(instance, time, current_task, best_task)
            #print("c " + str(time))
            current_task = best_task
            tasks_used[best_task] = 1
            task_order.append(best_task)
        return task_order