from solver.ProperSolver import ProperSolver

class InsertionSolver(ProperSolver):
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
                    l_j_from_moving_task_forward = task_start_times[j] + instance.p[j] - instance.d[j]
                    l_task_from_moving_task_forward = j_end_time_before_task + instance.p[task] - instance.d[task]
                    l_max_from_moving_task_forward = max(l_task_from_moving_task_forward, l_j_from_moving_task_forward)
                    if (next_start_time < task_end_time_before_next):
                            base_start_time = j_end_time_before_task
                            if (self._l_max is None) or (l_max_from_moving_task_forward > self._l_max):
                                self._l_max = l_max_from_moving_task_forward
                            continue
                    l_j_from_moving_j_forward = task_end_time_before_j + instance.p[j] - instance.d[j]
                    l_task_from_moving_j_forward = base_start_time + instance.p[task] - instance.d[task]
                    l_max_from_moving_j_forward = max(l_task_from_moving_j_forward, l_j_from_moving_j_forward)
                    if l_max_from_moving_j_forward < l_max_from_moving_task_forward:
                        task_start_times[task] = base_start_time
                        task = j
                        base_start_time = task_end_time_before_j
                        if (self._l_max is None) or (l_max_from_moving_j_forward > self._l_max):
                            self._l_max = l_max_from_moving_j_forward
                    else:
                        base_start_time = j_end_time_before_task
                        if (self._l_max is None) or (l_max_from_moving_task_forward > self._l_max):
                            self._l_max = l_max_from_moving_task_forward
                        
            task_start_times[task] = base_start_time
            l = base_start_time + instance.p[task] - instance.d[task]
            if (self._l_max is None) or (l > self._l_max):
                self._l_max = l
            task_order.append(task_preinsertion_order[i])
            task_order.sort(key=lambda i: task_start_times[i])
        return task_order
