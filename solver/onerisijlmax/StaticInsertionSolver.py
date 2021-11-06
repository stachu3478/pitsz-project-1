from solver.ProperSolver import ProperSolver

class StaticInsertionSolver(ProperSolver):
    # I'm insertion. I insert tasks in my own way.
    def task_order(self, instance):
        task_preinsertion_order = [i for i in range(instance.n)]
        task_preinsertion_order.sort(key=lambda i: instance.d[i] + instance.r[i] - instance.p[i])
        task_start_times = [None for i in range(instance.n)]
        task_order = []
        for i in range(instance.n):
            task = task_preinsertion_order[i]
            base_start_time = instance.r[task]
            for k, j in enumerate(task_order):
                j_end_time_before_task = task_start_times[j] + instance.p[j] + instance.s[j][task]
                task_end_time_before_j = base_start_time + instance.p[task] + instance.s[task][j]
                j_overlaps_task = ((task_start_times[j] >= base_start_time) and (task_end_time_before_j > task_start_times[j]))
                if j_overlaps_task or ((task_start_times[j] <= base_start_time) and (j_end_time_before_task > base_start_time)):
                        base_start_time = j_end_time_before_task
                        
            task_start_times[task] = base_start_time
            task_order.append(task_preinsertion_order[i])
            task_order.sort(key=lambda i: task_start_times[i])
        return task_order
