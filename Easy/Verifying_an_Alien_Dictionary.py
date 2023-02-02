class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            j = i+1
            ret = False
            len1 = len(words[i])
            len2 = len(words[j])
            for k in range(min(len1,len2)):
                idx1 = order.index(words[i][k])
                idx2 = order.index(words[j][k])
                if idx1<idx2:
                    ret = True
                    break
                else:
                    if idx1>idx2:
                        return False
            if len1>len2 and ret==False:
                return False
        return True
