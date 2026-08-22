class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for asteroid in asteroids:
            alive = True

            while alive and stk and stk[-1] > 0 and asteroid < 0:
                if abs(asteroid) < stk[-1]:
                    alive = False
                
                elif abs(asteroid) == stk[-1]:
                    stk.pop()
                    alive = False
                
                else:

                    stk.pop()
            if alive:
                stk.append(asteroid)
        
        return stk
        