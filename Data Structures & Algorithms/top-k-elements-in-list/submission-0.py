class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_items = sorted(count.items(), key=lambda pair: pair[1],    reverse=True)
        k_nums = sorted_items[0:k]
        result = []
        for x in k_nums:
            result.append(x[0])
        return result