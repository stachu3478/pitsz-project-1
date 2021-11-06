from solver.onerisijlmax.Solver import Solver

class NastySolver(Solver):
    def task_order(self, instance):
        return range(instance.n)

    def cruterion_value(self, instance, task_order):
        return 0
