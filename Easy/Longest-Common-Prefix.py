class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ret=strs[0]
        if "" in strs:
            return ""
        for i in range(1,len(strs)):
            while strs[i].find(ret)!=0:
                ret = ret[:-1]
                if ret == "":
                    return ret
        return ret
