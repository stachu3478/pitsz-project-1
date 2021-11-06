from solver.ProperSolver import ProperSolver

class SijCmaxSolver(ProperSolver):
    # I solve problem as there would be no due date
    def task_order(self, instance):
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
        
