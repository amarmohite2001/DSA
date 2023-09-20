class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            print(stones)
            a = -1 *heapq.heappop(stones)
            b = -1*heapq.heappop(stones)
            c = a-b
            if c>0:
                heapq.heappush(stones,-1*c)
        if len(stones)==0:
            return 0
        elif len(stones)==2:
            return -1*(stones[0]-stones[1])
        else:
            return -1*stones[0]
        