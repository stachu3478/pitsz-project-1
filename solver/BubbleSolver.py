from solver.ProperSolver import ProperSolver

class BubbleSolver(ProperSolver):
    # I'm bubble. Tasks flow in my list like bubbles.
    def task_order(self, instance):
        task_order = [i for i in range(instance.n)]
        task_order.sort(key=lambda i: instance.d[i] + instance.r[i])
        best_task_order = task_order
        least_l_max = self.l_max(instance, task_order)
        for i in range(instance.n - 1):
            new_task_order = task_order.copy()
            new_task_order[i], new_task_order[i + 1] = new_task_order[i + 1], new_task_order[i]
            l_max = self.l_max(instance, new_task_order)
            if l_max < least_l_max:
                least_l_max = l_max
                best_task_order = new_task_order
        return best_task_order