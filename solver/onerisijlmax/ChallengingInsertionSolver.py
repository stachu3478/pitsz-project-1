from solver.ProperSolver import ProperSolver

class ChallengingInsertionSolver(ProperSolver):
    # I'm insertion. I insert tasks in my own way.
    def task_order(self, instance):
        task_preinsertion_order = [i for i in range(instance.n)]
        task_preinsertion_order.sort(key=lambda i: instance.d[i] + instance.r[i] - instance.p[i])
        task_start_times = [None for i in range(instance.n)]
        task_order = []
        self._l_max = None
        for i in range(instance.n):
            task = task_preinsertion_order[i]
            base_start_time = instance.r[task]
            k = 0
            j = task_order[k]
            j_end_time_before_task = task_start_times[j] + instance.p[j] + instance.s[j][task]
            while j_end_time_before_task < base_start_time:
                k += 1
                j = task_order[k]
                j_end_time_before_task = task_start_times[j] + instance.p[j] + instance.s[j][task]
            #new_task_order = []
            for k, j in enumerate(task_order):
                j_end_time_before_task = task_start_times[j] + instance.p[j] + instance.s[j][task]
                task_end_time_before_j = base_start_time + instance.p[task] + instance.s[task][j]
                task_end_time_before_next = 0
                next_start_time = 0
                if len(task_order) > (k + 1):
                    task_end_time_before_next = base_start_time + instance.p[task] + instance.s[task][task_order[k + 1]]
                    next_start_time = task_start_times[task_order[k + 1]]
                j_overlaps_task = ((task_start_times[j] >= base_start_time) and (task_end_time_before_j > task_start_times[j]))
                if j_overlaps_task or ((task_start_times[j] <= base_start_time) and (j_end_time_before_task > base_start_time)):
                    #print('Conflict: ' + str(task) + " with " + str(j))
                    l_j_from_moving_task_forward = task_start_times[j] + instance.p[j] - instance.d[j]
                    l_task_from_moving_task_forward = j_end_time_before_task + instance.p[task] - instance.d[task]
                    l_max_from_moving_task_forward = max(l_task_from_moving_task_forward, l_j_from_moving_task_forward)

                    if (next_start_time < task_end_time_before_next):
                            base_start_time = j_end_time_before_task
                            #print('Multiple overlap: ' + str(task) + " moved forward as task with l max " + str(l_max_from_moving_task_forward) + ' and could start at ' + str(base_start_time))
                            if (self._l_max is None) or (l_max_from_moving_task_forward > self._l_max):
                                self._l_max = l_max_from_moving_task_forward
                            continue
                    #print('When i move task forward, j starts ' + str(task_start_times[j]) + ', ends at ' + str(task_start_times[j] + instance.p[j]) + ' and will be late ' + str(l_j_from_moving_task_forward) + ' then task starts ' + str(j_end_time_before_task) + ', ends ' + str(j_end_time_before_task + instance.p[task]) + ' and will be late ' + str(l_task_from_moving_task_forward))
                    l_j_from_moving_j_forward = task_end_time_before_j + instance.p[j] - instance.d[j]
                    l_task_from_moving_j_forward = base_start_time + instance.p[task] - instance.d[task]
                    l_max_from_moving_j_forward = max(l_task_from_moving_j_forward, l_j_from_moving_j_forward)
                    #print('When i move j forward, task starts ' + str(base_start_time) + ', ends at ' + str(base_start_time + instance.p[task]) + ' and will be late ' + str(l_task_from_moving_j_forward) + ' then j starts ' + str(task_end_time_before_j) + ', ends ' + str(task_end_time_before_j + instance.p[j]) + ' and will be late ' + str(l_j_from_moving_j_forward))
                    if l_max_from_moving_j_forward < l_max_from_moving_task_forward:
                        
                        task_start_times[task] = base_start_time
                        task = j
                        #print(str(j) + " moved forward as j with l max " + str(l_max_from_moving_j_forward) + ' and task starts at ' + str(base_start_time))
                        base_start_time = task_end_time_before_j
                        
                        if (self._l_max is None) or (l_max_from_moving_j_forward > self._l_max):
                            self._l_max = l_max_from_moving_j_forward
                    else:
                        base_start_time = j_end_time_before_task
                        #print(str(task) + " moved forward as task with l max " + str(l_max_from_moving_task_forward) + ' and could start at ' + str(base_start_time))
                        if (self._l_max is None) or (l_max_from_moving_task_forward > self._l_max):
                            self._l_max = l_max_from_moving_task_forward
                        
            task_start_times[task] = base_start_time
            l = base_start_time + instance.p[task] - instance.d[task]
            if (self._l_max is None) or (l > self._l_max):
                self._l_max = l
            task_order.append(task_preinsertion_order[i])
            #print('Insert task ' + str(task) + ' with l = ' + str(l) + ' at ' + str(base_start_time))
            task_order.sort(key=lambda i: task_start_times[i])
            #self.verify_start_time_conflicts(instance, task_order, task_start_times)
            #if self._l_max < self.l_max(instance, task_order):
            #    raise RuntimeError('Invalid l max, expected ' + str(self.l_max(instance, task_order)) + ', got ' + str(self._l_max))
            #print(str(task) + ' starts ' + str(base_start_time - instance.r[task]) + ' later')
            #l = 
            #if (self._l_max is None) or ()

        #print('done with lmax ' + str(self._l_max))
        return task_order

    def verify_start_time_conflicts(self, instance, task_order, start_times):
        for i in range(1, len(task_order)):
            prev_task = task_order[i - 1]
            current_task = task_order[i]
            previous_start_time = start_times[prev_task]
            prepare_time = previous_start_time + instance.p[prev_task] + instance.s[prev_task][current_task]
            if prepare_time > start_times[current_task]:
                raise RuntimeError('Task ' + str(current_task) + ' should start at least at ' + str(prepare_time) + ' after ' + str(prev_task) + ', starts at ' + str(start_times[current_task]) + ' instead')
