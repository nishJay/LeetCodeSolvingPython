from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, start, path, result):
        if len(path) >= 2:
            result.append(path)
        if start == len(nums):
            return 
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue
            if not path or nums[i] >= path[-1]:
                seen.add(nums[i])
                self.dfs(nums, i + 1, path + [nums[i]], result)
