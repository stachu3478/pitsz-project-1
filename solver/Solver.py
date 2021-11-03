from generator.instance import Instance

class Solver:
    def solve(self, input_filename, output_filename=None):
        instance = Instance().load(input_filename)
        task_order = self.task_order(instance)
        l_max = self.l_max(instance, task_order)
        if output_filename is None:
            student_id_index = input_filename.find("in_") + 3
            student_id = input_filename[student_id_index:(student_id_index + 6)]
            output_filename = 'out_' + student_id + '_146889_' + str(instance.n) + '.txt'
        self._save(output_filename, task_order, l_max)
        return l_max

    def _save(self, output_filename, task_order, l_max):
        f = open(output_filename, 'w')
        f.write(str(l_max) + '\n')
        f.write(' '.join(map(lambda j: str(task_order[j]), range(len(task_order)))) + '\n')
        f.close()

    def task_order(self, instance):
        raise NotImplementedError('Not yet implemented!')

    def l_max(self, instance, task_order):
        raise NotImplementedError('Not yet implemented!')