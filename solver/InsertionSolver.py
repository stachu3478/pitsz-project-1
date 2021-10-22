from solver.ProperSolver import ProperSolver

class InsertionSolver(ProperSolver):
    # I'm insertion. I insert tasks in my own way.
    def task_order(self, instance):
        task_preinsertion_order = [i for i in range(instance.n)]
        task_preinsertion_order.sort(key=lambda i: instance.p[i] / float(instance.r[i] - instance.d[i]))
        task_start_times = [None for i in range(instance.n)]
        task_order = []
        self._l_max = None
        for i in range(instance.n):
            task = task_preinsertion_order[i]
            base_start_time = instance.r[task]
            for _, j in enumerate(task_order):
                j_end_time_before_task = task_start_times[j] + instance.p[j] + instance.s[j][task]
                task_end_time_before_j = base_start_time + instance.p[task] + instance.s[task][j]
                if ((task_start_times[j] >= base_start_time) and (task_end_time_before_j > task_start_times[j])) or ((task_start_times[j] <= base_start_time) and (j_end_time_before_task > base_start_time)):
                    #print('Conflict: ' + str(task) + " with " + str(j))
                    l_j_from_moving_task_forward = task_start_times[j] + instance.p[j] - instance.d[j]
                    l_task_from_moving_task_forward = j_end_time_before_task + instance.p[task] - instance.d[task]
                    l_max_from_moving_task_forward = max(l_task_from_moving_task_forward, l_j_from_moving_task_forward)
                    #print('When i move task forward, j starts ' + str(task_start_times[j]) + ', ends at ' + str(task_start_times[j] + instance.p[j]) + ' and will be late ' + str(l_j_from_moving_task_forward) + ' then task starts ' + str(j_end_time_before_task) + ', ends ' + str(j_end_time_before_task + instance.p[task]) + ' and will be late ' + str(l_task_from_moving_task_forward))
                    l_j_from_moving_j_forward = task_end_time_before_j + instance.p[j] - instance.d[j]
                    l_task_from_moving_j_forward = base_start_time + instance.p[task] - instance.d[task]
                    l_max_from_moving_j_forward = max(l_task_from_moving_j_forward, l_j_from_moving_j_forward)
                    #print('When i move j forward, task starts ' + str(base_start_time) + ', ends at ' + str(base_start_time + instance.p[task]) + ' and will be late ' + str(l_task_from_moving_j_forward) + ' then j starts ' + str(task_end_time_before_j) + ', ends ' + str(task_end_time_before_j + instance.p[j]) + ' and will be late ' + str(l_j_from_moving_j_forward))
                    if l_max_from_moving_j_forward < l_max_from_moving_task_forward:
                        task_start_times[task] = base_start_time
                        task = j
                        base_start_time = task_end_time_before_j
                        #print(str(j) + " moved forward with l max " + str(l_max_from_moving_j_forward))
                        if (self._l_max is None) or (l_max_from_moving_j_forward > self._l_max):
                            self._l_max = l_max_from_moving_j_forward
                        #print('Moving j forward')
                    else:
                        base_start_time = j_end_time_before_task
                        #print(str(task) + " moved forward with l max " + str(l_max_from_moving_task_forward))
                        if (self._l_max is None) or (l_max_from_moving_task_forward > self._l_max):
                            self._l_max = l_max_from_moving_task_forward
                        #print('Moving task forward')
                        
            task_start_times[task] = base_start_time
            l = base_start_time + instance.p[task] - instance.d[task]
            if (self._l_max is None) or (l > self._l_max):
                self._l_max = l
            task_order.append(task_preinsertion_order[i])
            #print('Insert task ' + str(task) + ' with l = ' + str(l))
            task_order.sort(key=lambda i: task_start_times[i])
            #if self._l_max < self.l_max(instance, task_order)[0]:
            #    raise RuntimeError('Invalid l max, expected ' + str(self.l_max(instance, task_order)) + ', got ' + str(self._l_max))
            #print(str(task) + ' starts ' + str(base_start_time - instance.r[task]) + ' later')
            #l = 
            #if (self._l_max is None) or ()

        #print('done with lmax ' + str(self._l_max))
        return task_order

    #def verify_start_time_conflicts(self, instance, task_order, start_times):
    #    for i in range(1, instance.n):



    def l_max(self, instance, task_order):
        return super().l_max(instance, task_order)