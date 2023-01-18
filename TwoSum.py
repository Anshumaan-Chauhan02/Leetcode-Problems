class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j=1
        for i in range(len(nums)) :
            if (j<len(nums) and j>i) :
                while j<len(nums) :
                    if(nums[i]+nums[j]==target):
                        return [i,j]
                    else :
                        j=j+1
            j=i+2
        return []
