from generator.instance import Instance
from solver.ProperSolver import ProperSolver

class TaskNotFoundError(RuntimeError):
    pass

class LazySolver(ProperSolver):
    # I'm lazy. I prefer to do avalilable tasks with fastest switch.
    def task_order(self, instance):
        self.first_task = instance.r.find(0)
        self.done = { [self.first_task]: True }
        self.current_task = self.first_task
        self.current_time = 0
        self.tasks = [i for i in range(instance.n)]
        if self.first_task == -1:
            raise TaskNotFoundError
        task_order = [self.first_task]
        for _ in range(instance.n - 1):
            self.current_task = self._next_task()
            task_order.append(self.current_task)
            self.done[self.current_task] = True
        return task_order

    def _next_task(self, instance):
        heuristic_min = None
        heuristic_best = None
        for i in range(instance.n):
            if self.done.get(i, None) is None:
                continue
            heuristic_value = self._heurisic_value(i)
            if (heuristic_min is None) or (heuristic_value < heuristic_min):
                heuristic_min = heuristic_value
                heuristic_best = i
        return heuristic_best

    def _heurisic_value(self, task):
        pass