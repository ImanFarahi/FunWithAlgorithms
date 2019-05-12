​def strongPasswordChecker(s):
    str_len = len(s); change, triple, seq, i, length, delete, types = 0,0,0,0,1, str_len -20, [1] * 4
    get_missing_type = lambda ch: 1 if ch.islower() else 2 if ch.isupper() else 3 if ch.isdigit() else 0
    while i < str_len:
        while i + length < str_len and s[i] == s[i + length]: length +=1
        types[get_missing_type(s[i])] = 0
        triple = length / 3
        if triple > 0:
            if delete >= 1:
                seq = length % 3
                if seq == 0 or (delete >= 2 and seq == 1):
                    triple -= 1
                    delete -= seq + 1
            change += triple
        i , length = length + i , 1
    missing_type = sum(types[1:])
    if str_len > 20:
        change -= delete / 3
        delete = str_len - 20
        return delete + max(missing_type, change)
    elif str_len >= 6: return max(missing_type, change)
    return max(missing_type, 6- str_len)
