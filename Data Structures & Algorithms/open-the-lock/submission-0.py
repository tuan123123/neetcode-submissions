class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        if target == "0000" and "0000" not in dead:
            return 0
        visited = set("0000")
        q = deque(["0000"])
        moves = 0
        while q:
            for _ in range(len(q)):
                current = q.popleft()

                if current == target:
                    return moves
                for i in range(4):
                    digit = int(current[i])

                    up_digits = list(current)
                    up_digits[i] = str((digit + 1) % 10)
                    up_state = "".join(up_digits)

                    if up_state not in dead and up_state not in visited:
                        visited.add(up_state)
                        q.append(up_state)
                
                    down_digits = list(current)
                    down_digits[i] = str((digit - 1) % 10)
                    down_state = "".join(down_digits)

                    if down_state not in dead and down_state not in visited:
                        visited.add(down_state)
                        q.append(down_state)
            
            
            moves += 1

        return -1
            

            
        
        