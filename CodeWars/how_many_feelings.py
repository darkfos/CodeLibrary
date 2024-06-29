"""
    You have two arguments: string - a string of random letters(only lowercase)
    and array - an array of strings(feelings). Your task is to return how many specific feelings are in the array. 
"""


def count_feelings(st, arr):
    #6 kyu

    cnt: int = 0

    for word in arr:
        l_cnt: int = 0
        local_st = list(st)
        for ch in word:
            if ch in local_st:
                l_cnt += 1
                local_st.pop(local_st.index(ch))
                continue
            else:
                break
        
        if l_cnt == len(word):
            cnt += 1
    
    return f"{cnt} feeling{'s' if cnt != 1 else ''}."