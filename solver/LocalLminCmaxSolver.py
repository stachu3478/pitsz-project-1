from solver.ProperSolver import ProperSolver

class LocalLminCmaxSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        l_max = None
        time = 0
        current_task = None
        for j in range(instance.n):
            l_min = None
            c_min = None
            best_task_l = None
            best_task_c = None
            best_task = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                l = c - instance.d[i]
                if (l_min is None) or (l < l_min):
                    best_task_l = i
                    #print("Default l " + str(best_task_l))
                    l_min = l
                if (c_min is None) or (c < c_min):
                    best_task_c = i
                    #print("Default c " + str(best_task_l))
                    c_min = i
            if (l_max is None) or (l_min > l_max):
                l_max = l_min
                best_task = best_task_l
            else:
                best_task = best_task_c
            #print("best " + str(j) + " task " + str(best_task))
            print("lmax " + str(l_max))
            time = self.end_time(instance, time, current_task, best_task)
            print("c " + str(time))
            current_task = best_task
            tasks_used[best_task] = 1
            task_order.append(best_task)
        return task_order