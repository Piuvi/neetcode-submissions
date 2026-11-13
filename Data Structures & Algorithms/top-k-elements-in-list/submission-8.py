class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
        j = k
        for n in nums:
            seen[n] = 1 + seen.get(n, 0)
        
        result = sorted(seen, key=seen.get, reverse=True)

        return result[:k]