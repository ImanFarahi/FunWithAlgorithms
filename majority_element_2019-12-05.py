class Solution1(object):
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
                c[num] = -sys.maxsize - 1 # -float('inf')
        return v

    
class Solution2(object):
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
        
        
class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = collections.defaultdict(int); v =[]; m= len(nums)/3
        for num in nums:
            c[num] += 1
            if c[num] > m:
                v.append(num)
                c[num] = - sys.maxsize -1
        return v
    
  
 class Solution4(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v = []; m= len(nums)/3
        for num, c in collections.Counter(nums).items(): 
            if c <= m: continue
            else: v.append(num)
        return v
    
      
class Solution5(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums) / 3; v, t, c = [], [0, 0], [0, 0]
        for num in nums:
            if t[0] == num:
                c[0] += 1 
            elif t[1] == num:
                c[1] += 1 
            elif c[0] == 0:
                t[0], c[0] = num, 1 
            elif c[1] == 0:
                t[1], c[1] = num, 1
            else:
                c[0] -= 1
                c[1] -= 1
                
        c = [0, 0]
        for num in nums:
            if num == t[0]:
                c[0] += 1 
                continue
            if num == t[1]:
                c[1] += 1
                continue
        
        v.append(t[0]) if c[0] > m else None
        v.append(t[1]) if c[1] > m else None
               
        return v
