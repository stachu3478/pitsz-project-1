from solver.ProperSolver import ProperSolver

class LocalLmax0CminSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        current_l_max = None
        time = 0
        current_task = None
        for j in range(instance.n):
            l_max = None
            c_min = None
            best_task_l = None
            best_task_c = None
            best_task = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                l = c - instance.d[i]
                if (l_max is None) or (l > l_max):
                    best_task_l = i
                    #print("Default l " + str(best_task_l) + " with " + str(l))
                    l_max = l
                if (c_min is None) or (c < c_min):
                    best_task_c = i
                    #print("Default c " + str(best_task_l) + " with " + str(c))
                    c_min = c
            if ((current_l_max is None) or (l_max > current_l_max)) and (l_max > 325):
                current_l_max = l_max
                best_task = best_task_l
            else:
                best_task = best_task_c
            #print("best " + str(j) + " task " + str(best_task))
            #print("lmax " + str(current_l_max))
            time = self.end_time(instance, time, current_task, best_task)
            #print("c " + str(time))
            current_task = best_task
            tasks_used[best_task] = 1
            task_order.append(best_task)
        return task_order