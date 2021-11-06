from solver.ProperSolver import ProperSolver

class PanicSolver(ProperSolver):
    # I'm panic. I look for tasks that have to be done first.
    def task_order(self, instance):
        task_order = [i for i in range(instance.n)]
        task_order.sort(key=lambda i: instance.d[i])
        return task_order