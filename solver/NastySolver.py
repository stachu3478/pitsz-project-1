from solver.Solver import Solver

class NastySolver(Solver):
    def task_order(self, instance):
        return range(instance.n)

    def l_max(self, instance, task_order):
        return 0
