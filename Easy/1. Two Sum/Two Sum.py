class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        anca = {}
        for i, num in (enumerate(nums)):
            saad = target - num
            if saad in anca:
                return [anca[saad], i]
            else:
                anca[num] = i
