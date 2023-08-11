class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final = deque()
        i=0
        while i<len(operations):
            if operations[i]=='+':
                a=final[-2]+final[-1]
                final.append(a)
            elif operations[i]=='D':
                b = final[-1]*2
                final.append(b)
            elif operations[i]=='C':
                final.pop()
            else:
                final.append(int(operations[i]))
            i+=1
        return sum(final)