from generator.instance import Instance

class SolverBase:
    def solve(self, input_filename, output_filename=None, klass=Instance):
        instance = klass().load(input_filename)
        task_order = self.task_order(instance)
        criterion_value = self.criterion_value(instance, task_order)
        if output_filename is None:
            student_id_index = input_filename.find("in_") + 3
            student_id = input_filename[student_id_index:(student_id_index + 6)]
            output_filename = 'out_' + student_id + '_146889_' + str(instance.n) + '.txt'
        self._save(output_filename, task_order, criterion_value)
        return criterion_value

    def _save(self, output_filename, task_order, criterion_value):
        f = open(output_filename, 'w')
        f.write(str(criterion_value) + '\n')
        self.write(f, task_order)
        f.close()

    def write(self, f, task_order):
        raise NotImplementedError('Not yet implemented!')

    def task_order(self, instance):
        raise NotImplementedError('Not yet implemented!')

    def criterion_value(self, instance, task_order):
        raise NotImplementedError('Not yet implemented!')