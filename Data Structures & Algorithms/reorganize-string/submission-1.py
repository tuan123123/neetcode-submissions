class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        heap = []

        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))

        res = []
        count = 0
        prev = ""

        while heap:
            count1, char = heapq.heappop(heap)

            res.append(char)

            if count < 0:
                heapq.heappush(heap, (count, prev))
            
            count1 += 1

            count = count1
            prev = char
        
        if len(res) != len(s):
            return ""
        
        return "".join(res)

