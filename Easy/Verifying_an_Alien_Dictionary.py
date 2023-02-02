class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                ret = False
                len1 = len(words[i])
                len2 = len(words[j])
                for k in range(min(len1,len2)):
                    idx1 = order.index(words[i][k])
                    idx2 = order.index(words[j][k])
                    print(words[i][k], idx1, words[j][k], idx2)
                    if idx1>idx2:
                        ret = False
                        return False
                    else:
                        if idx1==idx2:
                            continue
                        else:
                            ret = True
                            break
                if len1>len2 and ret==False:
                    return False
        return True
