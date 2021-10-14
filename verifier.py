from solver.ProperSolver import ProperSolver
from generator.instance import Instance

class Verifier:
    def __init__(self, instance_filename, output_filename, solver=None):
        self.instance = Instance().load(instance_filename)
        if solver is not None:
            solver.solve(instance_filename)
        self._load_solution(output_filename)

    def _load_solution(self, filename):
        f = open(filename, 'r')
        self.l_max = int(f.readline())
        self.task_order = list(map(lambda i: int(i), f.readline().split(' ')))

    def verify(self):
        if len(self.task_order) != self.instance.n:
            print('Invalid task order length: ' + str(len(self.task_order)) + '. Should be ' + str(self.instance.n))
            return 2
        if len(list(set(self.task_order))) != len(self.task_order):
            print('Provided task order has repetive values. Should be no such values.')
            return 3
        proper_solver = ProperSolver()
        valid_l_max = proper_solver.l_max(self.instance, self.task_order)
        if valid_l_max != self.l_max:
            print('Invalid l_max provided: ' + str(self.l_max) + '. Should be ' + str(valid_l_max))
            return 1
        return 0