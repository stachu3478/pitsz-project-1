
from solver.BalancingSolver import BalancingSolver

class BalancingBubbleSolver(BalancingSolver):
    # I'm balancing. I try different weights to find perfect center of window for the tasks.
    def task_order(self, instance):
        best_task_order = super().task_order(instance)
        least_l_max = self.l_max(instance, best_task_order)
        for i in range(instance.n - 1):
            new_task_order = best_task_order.copy()
            new_task_order[i], new_task_order[i + 1] = new_task_order[i + 1], new_task_order[i]
            l_max = self.l_max(instance, new_task_order)
            if l_max < least_l_max:
                least_l_max = l_max
                best_task_order = new_task_order
        return best_task_order
