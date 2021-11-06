from solver.SolverBase import SolverBase

class Solver(SolverBase):
    def write(self, f, task_order):
        f.write('\n'.join(map(lambda b: ' '.join(map(lambda bj: str(task_order[b][bj]), range(len(task_order[b])))), range(len(task_order)))) + '\n')
