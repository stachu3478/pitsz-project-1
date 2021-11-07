from generator.Q4rwuInstance import Q4rwuInstance
from solver.Q4riwu.ProperSolver import ProperSolver
from verifier.VerifierBase import VerifierBase

class Q4rwuVerifier(VerifierBase):
    def __init__(self, instance_filename, output_filename, instance_klass=Q4rwuInstance, comparison_class=ProperSolver, solver=None):
        super().__init__(instance_filename, output_filename, instance_klass=instance_klass, comparison_class=comparison_class, solver=solver)

    def read_solution(self, f):
        self.task_order = [self._read_line(f), self._read_line(f), self._read_line(f), self._read_line(f)]

    def _read_line(self, f):
        tasks = f.readline().strip().split(' ')
        if (tasks[0] == '') and (len(tasks) == 1): # no tasks inserted at this machine
            return []
        return list(map(lambda i: int(i), tasks))
