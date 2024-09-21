def scramble(s1, s2):
    s3 = len(s2)
    s1, s2 = list(s1), list(s2)
    cnt: int = 0
    for chr in range(len(s2)):
        if s2[chr] in s1:
            s1[s1.index(s2[chr])] = ""
            s2[chr] = ""
            cnt += 1
    s2 = "".join(s2)
    return cnt == s3 and len(s2) == 0