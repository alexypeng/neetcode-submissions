class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)

        for task in tasks:
            counter[task] += 1
        
        max_heap = list(counter.values())

        heapq.heapify_max(max_heap)
        res = 0

        while max_heap:
            tasks_ran = 0
            to_add = []

            while max_heap and tasks_ran < n +1 :
                task = heapq.heappop_max(max_heap)
                if task > 1:
                    to_add.append(task - 1)
                
                tasks_ran += 1
            
            for elem in to_add:
                heapq.heappush_max(max_heap, elem)
            res += n + 1 if max_heap else tasks_ran
        
        return res
