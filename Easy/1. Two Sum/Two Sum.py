class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in (enumerate(nums)):
            d = target - num
            if d in a:
                return [a[d], i]
            else:
                a[num] = i