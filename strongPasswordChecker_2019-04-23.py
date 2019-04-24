​class Solution(object):
    def get_missing_type(self, str):
        lower = upper = digit = 1
        for ch in str:
            if ch.islower(): lower = 0
            elif ch.isupper(): upper = 0
            elif ch.isdigit(): digit = 0
        return (lower + upper + digit)
    
    def strongPasswordChecker(self, s):
        str_len= len(s)
        
        missing_type = self.get_missing_type(s)
        if str_len < 6: return max(missing_type, 6 - str_len)
        
        change = one = two= 0
        p = 2 
        while p < str_len:
            if s[p] == s[p-1] == s[p-2]: 
                length = 2
                while p < str_len and s[p] == s[p-1]:
                    length += 1
                    p += 1
                
                change += length / 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 2
            else:
                p += 1
        if str_len <= 20: return max(missing_type, change)
        
        delete = str_len - 20
        change -= min(delete, one)
        change -= min(max(delete - one, 0), two ) / 2
        change -= max(delete - one - two, 0) / 3
        return delete + max(missing_type, change)
