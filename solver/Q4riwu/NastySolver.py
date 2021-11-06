from solver.Q4riwu.Solver import Solver

class NastySolver(Solver):
    def task_order(self, instance):
        base_div = int(instance.n / 4)
        # sprint(sum(instance.w))
        return [range(base_div), range(base_div, 2 * base_div), range(2 * base_div, 3 * base_div), range(3 * base_div, instance.n)]

    def criterion_value(self, instance, task_order):
        return 0
