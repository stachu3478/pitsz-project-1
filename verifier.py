from solver.ProperSolver import ProperSolver
from generator.instance import Instance
from solver.NastySolver import NastySolver

class Verifier:
    def __init__(self, instance_name, solver=None):
        instance_filename = 'in_' + instance_name
        self.instance = Instance().load(instance_filename)
        if solver is not None:
            solver.solve(instance_name)
        self._load_solution('out_' + instance_name)

    def _load_solution(self, filename):
        f = open(filename, 'r')
        self.l_max = int(f.readline())
        self.task_order = list(map(lambda i: int(i), f.readline().split(' ')))

    def verify(self):
        proper_solver = ProperSolver()
        valid_l_max = proper_solver.l_max(self.instance, self.task_order)
        if valid_l_max == self.l_max:
            return 0
        print('Invalid l_max provided: ' + str(self.l_max) + '. Should be ' + str(valid_l_max))
        return 1

