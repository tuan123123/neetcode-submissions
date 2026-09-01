class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        axyy
        try to put the biggest frequency character first
        """

        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        heap = []

        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))
        
        res = []
        prev_count = 0
        prev_char = ""

        while heap:
            count, char = heapq.heappop(heap)

            res.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            count += 1
            prev_count = count
            prev_char = char

        
        if len(s) != len(res):
            return ""
        
        return "".join(res)