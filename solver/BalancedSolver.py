from solver.ProperSolver import ProperSolver

class BalancedSolver(ProperSolver):
    # I'm balanced. I try to find perfect center of window for the tasks.
    def task_order(self, instance):
        task_order = [i for i in range(instance.n)]
        task_order.sort(key=lambda i: instance.d[i] + instance.r[i])
        return task_order