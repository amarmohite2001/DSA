class Solution:
    def calPoints(self, operations: List[str]) -> int:
#         final = deque()
#         i=0
#         while i<len(operations):
#             if operations[i]=='+':
#                 a=final[-2]+final[-1]
#                 final.append(a)
#             elif operations[i]=='D':
#                 b = final[-1]*2
#                 final.append(b)
#             elif operations[i]=='C':
#                 final.pop()
#             else:
#                 final.append(int(operations[i]))
#             i+=1
#         return sum(final)
    
            score_stack = []

            for o in operations:


                # it is +, D, or C
                # if stack isn't of sufficient length, then operation is voided
                if o == "+" and len(score_stack) >= 2:
                    summed = score_stack[-2] + score_stack[-1]
                    score_stack.append(summed)

                elif o == "D" and len(score_stack) >= 1:
                    doubled = score_stack[-1] * 2
                    score_stack.append(doubled)

                elif o == "C" and len(score_stack) >= 1:
                    score_stack.pop() 

                else: 
                    score_stack.append(int(o))

            return sum(score_stack)