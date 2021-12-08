from solver.Q4riwu.ProperSolver import ProperSolver

class StaticInsertionDLLPTHWSM(ProperSolver):
    # I'm Static Insertion Dead Lined Least Processing Time Highest Weight Slowest Machine. I insert tasks in my own way.
    def task_order(self, instance):
        task_preinsertion_order = [i for i in range(instance.n)]
        task_preinsertion_order.sort(key=lambda i: instance.p[i] * instance.w[i] - instance.d[i] + instance.r[i], reverse=True)
        machine_insertion_order = [i for i in range(4)]
        machine_insertion_order.sort(key=lambda i: instance.b[i])
        task_start_times = [None for i in range(instance.n)]
        task_order = [[], [], [], []]
        late_tasks = []
        for i in range(instance.n):
            task = task_preinsertion_order[i]
            inserted = False
            for j, _ in enumerate(task_order):
                conflict = False
                machine_id = machine_insertion_order[j]
                speed = instance.b[machine_id]
                base_start_time = instance.d[task] - instance.p[task] / speed
                for _, l in enumerate(task_order[machine_id]):
                    l_end_time = task_start_times[l] + instance.p[l] / speed
                    task_end_time = base_start_time + instance.p[task] / speed
                    l_overlaps_task = ((task_end_time >= task_start_times[l]) and (task_start_times[l] >= base_start_time))
                    if l_overlaps_task or ((task_start_times[l] <= base_start_time) and (base_start_time <= l_end_time)):
                        base_start_time = task_start_times[l] - instance.p[task] / speed
                        if base_start_time < instance.r[task]:
                            conflict = True
                            break
                if conflict == False:
                    inserted = True
                    task_order[machine_id].append(task)
                    #print(str(task) + ' at ' + str(machine_id) + ' from ' + str(base_start_time) + ' to ' + str(base_start_time + instance.p[task] / speed))
                    task_start_times[task] = base_start_time
                    task_order[machine_id].sort(key=lambda i: -task_start_times[i])
                    #if self.criterion_value(instance, task_order) != self.expected_value(instance, late_tasks):
                    #    raise RuntimeError('Invalid is ' + str(self.expected_value(instance, late_tasks)) + ' should be ' + str(self.criterion_value(instance, task_order)))
                    break
            if inserted == False:
                late_tasks.append(task)
        for ordering in task_order:
            ordering.sort(key=lambda i: task_start_times[i])
        task_order[0] += late_tasks
        return task_order

    def expected_value(self, instance, late_tasks):
        return sum(map(lambda i: instance.w[i], late_tasks))
