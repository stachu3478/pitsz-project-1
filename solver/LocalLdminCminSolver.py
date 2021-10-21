from solver.ProperSolver import ProperSolver

class LocalLdminCminSolver(ProperSolver):
    # I add tasks that minimize l max first
    def task_order(self, instance):
        task_order = []
        tasks_used = [0 for i in range(instance.n)]
        current_l_max = None
        time = 0
        current_task = None
        for j in range(instance.n):
            ld_min = None
            c_min = None
            cd_min = None
            best_task_l = None
            best_task_c = None
            best_task = None
            for i in range(instance.n):
                if tasks_used[i] == 1:
                    continue
                c = self.end_time(instance, time, current_task, i)
                cd = c - self.end_time(instance, 0, current_task, i)
                ld = cd - instance.d[i]
                if (ld_min is None) or (ld < ld_min):
                    best_task_l = i
                    #print("Default l " + str(best_task_l))
                    ld_min = ld
                if (c_min is None) or (c < c_min):
                    best_task_c = i
                    #print("Default c " + str(best_task_l))
                    c_min = c
                if (cd_min is None) or (cd < cd_min):
                    cd_min = cd
            if cd_min < 0:
                raise RuntimeError('Cd min is lower than zero!')
            if (current_l_max is None) or (cd_min > 0):
                current_l_max = ld_min
                best_task = best_task_l
            else:
                print('cd is 0')
                best_task = best_task_c
            #print("best " + str(j) + " task " + str(best_task))
            #print("lmax " + str(l_max))
            time = self.end_time(instance, time, current_task, best_task)
            #print("c " + str(time))
            current_task = best_task
            tasks_used[best_task] = 1
            task_order.append(best_task)
        return task_order