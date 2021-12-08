from verifier.flatten import flatten


class VerifierBase:
    def __init__(self, instance_filename, output_filename, instance_klass=None, comparison_class=None, solver=None):
        self.instance = instance_klass().load(instance_filename)
        self.comparison_class = comparison_class
        if solver is not None:
            solver.solve(instance_filename, klass=instance_klass)
        self._load_solution(output_filename)

    def _load_solution(self, filename):
        f = open(filename, 'r')
        self.criterion_value = int(f.readline())
        self.read_solution(f)

    def read_solution(self, f):
        raise NotImplementedError('Not yet implemented!')

    def verify(self):
        flattened_tasks = flatten(self.task_order)
        if len(flattened_tasks) != self.instance.n:
            print('Invalid task order length: ' + str(len(flattened_tasks)) + '. Should be ' + str(self.instance.n))
            return 2
        if len(list(set(flattened_tasks))) != len(flattened_tasks):
            print('Provided task order has repetive values. Should be no such values.')
            return 3
        proper_solver = self.comparison_class()
        if min(flattened_tasks) == 1: # detect enumerating from 1
            for i, _ in enumerate(self.task_order):
                if self.task_order[i] is not int:
                    for j, _ in enumerate(self.task_order[i]):
                        self.task_order[i][j] -= 1
                else:
                    self.task_order[i] -= 1
        valid_criterion_value = proper_solver.criterion_value(self.instance, self.task_order)
        if valid_criterion_value != self.criterion_value:
            print('Invalid criterion_value provided: ' + str(self.criterion_value) + '. Should be ' + str(valid_criterion_value))
            #print(valid_criterion_value)
            return 1
        print(valid_criterion_value)
        return 0