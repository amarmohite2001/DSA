from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        p = deque(students)
        q= deque(sandwiches)
        count = len(p)
        served = 0
        while count>0 and served<count:
            if p[0]==q[0]:
                p.popleft()
                q.popleft()
                served=0
                count-=1
            else:
                if not p or not q:
                    break
                p.append(p.popleft())
                served+=1
        return len(p)
                
        
                
            
            
        