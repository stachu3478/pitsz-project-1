from generator.instance import Instance
from solver.SolverBase import SolverBase

class Solver(SolverBase):
    def write(self, f, task_order):
        f.write(' '.join(map(lambda j: str(task_order[j]), range(len(task_order)))) + '\n')
