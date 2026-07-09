class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while cooldown or max_heap:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    cooldown.append((count, time + n))
                

            if cooldown and cooldown[0][1] == time:
                count, ready = cooldown.popleft()
                heapq.heappush(max_heap, count)
        
        return time