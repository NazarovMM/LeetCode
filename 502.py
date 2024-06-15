import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x: x[1])
        max_heap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(max_heap, -projects[i][0])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w


k = 1  # кол-во проектов
w = 0  # начальный бюджет
profits = [1, 2, 3]  # прибыль от проектов
capital = [1, 1, 2]  # бюджет от проектов

solution = Solution()
result = solution.findMaximizedCapital(k, w, profits, capital)
print(result)

"""
#Time Limit Exceeded
    def findMaxProjectProfit(w: int, profits: list[int], capital: list[int]) -> int:
        max_project_profit = 0
        selected_project = None
        for i in range(len(capital)):
            if capital[i] <= w:
                if max_project_profit < profits[i]:
                    max_project_profit = profits[i]
                    selected_project = i
        if selected_project == None:
            return w
        profits.pop(selected_project)
        capital.pop(selected_project)
        w += max_project_profit
        return w

    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        while k > 0:
            w = Solution.findMaxProjectProfit(w, profits, capital)
            k -= 1
        return w
"""
