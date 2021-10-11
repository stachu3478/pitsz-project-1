from generator.instance import Instance


class Solver:
    def solve(self, input_filename):
        instance = Instance().load(input_filename)
        task_order = self.task_order(instance)
        l_max = self.l_max(instance, task_order)
        output_filename = input_filename.replace('in', 'out')
        self._save(output_filename, task_order, l_max)

    def _save(self, output_filename, task_order, l_max):
        f = open(output_filename, 'w')
        f.write(str(l_max) + '\n')
        f.write(' '.join(map(lambda j: str(task_order[j]), range(len(task_order)))) + '\n')
        f.close()

    def task_order(self, instance):
        raise NotImplementedError('Not yet implemented!')

    def l_max(self, instance, task_order):
        raise NotImplementedError('Not yet implemented!')