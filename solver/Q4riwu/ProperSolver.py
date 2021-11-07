from solver.Q4riwu.Solver import Solver

class ProperSolver(Solver):
    def criterion_value(self, instance, task_order):
        late_weights = 0
        late_tasks = []
        for m, b in enumerate(task_order):
            time = 0
            for i in b:
                time = self.end_time(instance,  time, i, m)
                l = time - instance.d[i]
                if l > 0:
                    late_weights += instance.w[i]
                    late_tasks.append(i)
        return late_weights

    def end_time(self, instance, time, next_task, machine_id):
        wait_time = max(0, instance.r[next_task] - time)
        return time + wait_time + instance.p[next_task] / instance.b[machine_id]
