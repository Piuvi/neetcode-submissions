class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # We create a hashmap in which were gonna 
        # save the instances of every number we see

        # were gonna go thrugh all the numbers and write the number of apeareances of each
        for n in nums:
            seen[n]= 1 + seen.get(n,0) # we add +1 if we see the nummber

        # 1. Sort the keys (the numbers) based on their frequencies (their values) in 
        # descending order
        sorted_nums = sorted(seen.keys(), key=lambda x: seen[x], reverse=True)
        
        # 2. Return the first k elements from the sorted list
        return sorted_nums[:k]

