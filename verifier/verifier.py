from generator.instance import Instance
from solver.onerisijlmax.ProperSolver import ProperSolver
from verifier.VerifierBase import VerifierBase

class Verifier(VerifierBase):
    def __init__(self, instance_filename, output_filename, instance_klass=Instance, comparison_class=ProperSolver, solver=None):
        super().__init__(instance_filename, output_filename, instance_klass=instance_klass, comparison_class=comparison_class, solver=solver)

    def read_solution(self, f):
        self.task_order = list(map(lambda i: int(i), f.readline().strip().split(' ')))
