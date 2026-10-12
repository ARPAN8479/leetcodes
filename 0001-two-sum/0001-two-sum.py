class Solution(object):
    def twoSum(self, nums, target):
        hashmap ={}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return[hashmap[difference] ,i]
            hashmap[nums[i]] = i
        return []
        