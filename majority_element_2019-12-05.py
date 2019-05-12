class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c= {}; v =[]; m= len(nums)/3
        for num in nums:
            c[num] = 1 if num not in c.keys() else c[num]+1
            if c[num] > m:
                v.append(num)
                c[num] = - float('inf')
        return v

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v =[]; m= len(nums)/3
        for num in nums: 
            if num in v or nums.count(num) <= m: continue
            else: v.append(num)
        return v
        
        