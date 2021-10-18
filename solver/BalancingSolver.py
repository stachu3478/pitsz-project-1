from solver.ProperSolver import ProperSolver

class BalancingSolver(ProperSolver):
    # I'm balancing. I try different weights to find perfect center of window for the tasks.
    def task_order(self, instance):
        best_task_order = [i for i in range(instance.n)]
        best_task_order.sort(key=lambda i: instance.d[i] + instance.r[i])
        least_l_max = self.l_max(instance, best_task_order)
        r_weight = 0.5
        r_weight_change = 0.25
        for _ in range(instance.n):
            right_task_order = best_task_order.copy()
            right_r_weight = r_weight + r_weight_change
            right_task_order.sort(key=lambda i: (1 - right_r_weight) * instance.d[i] + right_r_weight * instance.r[i])
            right_l_max = self.l_max(instance, right_task_order)
            left_task_order = best_task_order.copy()
            left_r_weight = r_weight - r_weight_change
            left_task_order.sort(key=lambda i: (1 - left_r_weight) * instance.d[i] + left_r_weight * instance.r[i])
            left_l_max = self.l_max(instance, left_task_order)
            if right_l_max < left_l_max:
                r_weight = right_r_weight
            elif left_l_max < right_l_max:
                r_weight = left_r_weight
            elif r_weight < 0.5:
                r_weight = right_r_weight
            else:
                r_weight = left_r_weight
            if right_l_max < least_l_max:
                least_l_max = right_l_max
                best_task_order = right_task_order
            if left_l_max < least_l_max:
                least_l_max = left_l_max
                best_task_order = left_task_order
            r_weight_change /= 2
        return best_task_order