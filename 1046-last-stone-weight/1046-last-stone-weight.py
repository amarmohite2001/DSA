class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            print(stones)
            a = -1 *heapq.heappop(stones)
            b = -1*heapq.heappop(stones)
            c = a-b
            if c>0:
                heapq.heappush(stones,-1*c)
        stones.append(0)
        return abs(stones[0])