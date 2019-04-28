# Author: http://professionalProgrammer.ir
def strongPasswordChecker(s):
    get_missing_type = lambda ch: (-1 if ch.islower() or ch.isupper() or ch.isdigit() else 0)
    change = triple = seq = temp_triple = 0
    i = 2 
    str_len = len(s)
    delete = str_len - 20
    missing_type = 3
    
    missing_type += get_missing_type(s[0]) + get_missing_type(s[1])
    
    while i < str_len:
        if s[i] == s[i-1] and s[i] == s[i-2]: 
            length = 2
            while i < str_len and s[i] == s[i-1]:
                length += 1
                missing_type += get_missing_type(s[i])
                i += 1
            triple = length / 3
            
            if delete > 0 and triple != 0:
                temp_triple = triple
                seq = length % 3
                
                if seq == 0 and triple >= delete: triple -= delete
                elif seq == 1 and triple >= (delete / 2): triple -= (delete / 2)
                elif seq == 2 and triple >= (delete / 3): triple -= (delete / 3)
                else: triple = 0
                
                delete -= temp_triple - triple
                
            change += max(triple, 0) 
        else:
            missing_type += get_missing_type(s[i])
            i += 1
            
    missing_type = max(missing_type, 0) 

    if str_len < 6: return max(missing_type, 6 - str_len)
    if str_len <= 20: return max(missing_type, change)
    delete = str_len - 20
    return delete + max(missing_type, change)
