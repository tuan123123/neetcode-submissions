class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ope in operations:
            if ope == '+':
                first, second = stk[-1], stk[-2]
                res = first + second
                stk.append(res)
            elif ope == 'D':
                res = stk[-1]
                res1 = res * 2
                stk.append(res1)
            elif ope == 'C':
                stk.pop()
            else:
                stk.append(int(ope))
        summ = 0
        for stkk in stk:
            summ += stkk
        
        return summ

