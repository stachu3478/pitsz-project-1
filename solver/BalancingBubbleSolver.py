
from solver.BalancingSolver import BalancingSolver

class BalancingBubbleSolver(BalancingSolver):
    # I'm balancing. I try different weights to find perfect center of window for the tasks.
    def task_order(self, instance):
        best_task_order = super().task_order(instance)
        least_l_max = self.l_max(instance, best_task_order)
        sij_task_order = self.solve_as_1_sij_cmax(instance)
        sij_l_max = self.l_max(instance, sij_task_order)
        if sij_l_max < least_l_max:
            print("better as cmax: " + str(sij_l_max))
            best_task_order = sij_task_order
            least_l_max = sij_l_max
        for i in range(instance.n - 1):
            new_task_order = best_task_order.copy()
            new_task_order[i], new_task_order[i + 1] = new_task_order[i + 1], new_task_order[i]
            l_max = self.l_max(instance, new_task_order)
            if l_max < least_l_max:
                least_l_max = l_max
                best_task_order = new_task_order
        best_task_order = self.bubble_plus(instance, best_task_order)
        self.bubble_progressive(instance, best_task_order)
        return best_task_order

    def bubble_plus(self, instance, task_order_to_opt):
        sorting_task_order = task_order_to_opt.copy()
        best_task_order = task_order_to_opt
        least_l_max = self.l_max(instance, task_order_to_opt)
        print("Current l max " + str(least_l_max))
        for _ in range(instance.n):
            task_order = sorting_task_order.copy()
            previous_time = 0
            previous_task = None
            time = self.end_time(instance, 0, None, task_order[0])
            for i in range(instance.n - 1):
                time_unchanged = self.end_time(instance, time, task_order[i], task_order[i + 1])
                previous_time_inversed = self.end_time(instance, previous_time, previous_task, task_order[i + 1])
                time_inversed = self.end_time(instance, previous_time_inversed, task_order[i + 1], task_order[i])
                l_left_unchanged = time - instance.d[task_order[i]]
                l_right_unchanged = time_unchanged - instance.d[task_order[i + 1]]
                l_left_reversed = previous_time_inversed - instance.d[task_order[i + 1]]
                l_right_reversed = time_inversed - instance.d[task_order[i]]
                if max(l_left_reversed, l_right_reversed) < max(l_left_unchanged, l_right_unchanged):
                    task_order[i], task_order[i + 1] = task_order[i + 1], task_order[i]
                    previous_time = previous_time_inversed
                    time = time_inversed
                else: 
                    previous_time = time
                    time = time_unchanged
                previous_task = task_order[i]
            new_l_max = self.l_max(instance, task_order)
            if new_l_max < least_l_max:
                least_l_max = new_l_max
                best_task_order = task_order
                print("Upgraeded l max " + str(least_l_max))
            sorting_task_order = task_order
        return best_task_order

    def bubble_progressive(self, instance, best_task_order):
        for _ in range(instance.n):
            previous_time = 0
            previous_task = None
            time = self.end_time(instance, 0, None, best_task_order[0])
            # l_max = self.l_max(instance, best_task_order)
            for i in range(instance.n - 1):
                time_unchanged = self.end_time(instance, time, best_task_order[i], best_task_order[i + 1])
                previous_time_inversed = self.end_time(instance, previous_time, previous_task, best_task_order[i + 1])
                time_inversed = self.end_time(instance, previous_time_inversed, best_task_order[i + 1], best_task_order[i])
                l_left_unchanged = time - instance.d[best_task_order[i]]
                l_right_unchanged = time_unchanged - instance.d[best_task_order[i + 1]]
                l_left_reversed = previous_time_inversed - instance.d[best_task_order[i + 1]]
                l_right_reversed = time_inversed - instance.d[best_task_order[i]]
                if (time_inversed <= time_unchanged) and max(l_left_reversed, l_right_reversed) < max(l_left_unchanged, l_right_unchanged):
                    best_task_order[i], best_task_order[i + 1] = best_task_order[i + 1], best_task_order[i]
                    previous_time = previous_time_inversed
                    time = time_inversed
                else: 
                    previous_time = time
                    time = time_unchanged
                previous_task = best_task_order[i]

    def solve_as_1_sij_cmax(self, instance):
        task_s_reservation = [0 for _ in range(instance.n)]
        least_r = instance.r[0]
        best_by_r = 0
        for j in range(1, instance.n):
            if instance.r[j] < least_r:
                least_r = instance.r[j]
                best_by_r = j
        task_order = [best_by_r]
        task_s_reservation[best_by_r] = 1
        for i in range(1, instance.n):
            task = task_order[i - 1]
            least_s = None
            best_j = None
            for j in range(0, instance.n):
                if task_s_reservation[j] == 1:
                    continue
                if (least_s is None) or (instance.s[task][j] < least_s):
                    least_s = instance.s[task][j]
                    best_j = j
            task_s_reservation[best_j] = 1
            task_order.append(best_j)
        return task_order
