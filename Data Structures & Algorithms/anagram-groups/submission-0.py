class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            sortS = "".join(sorted(str))
            res[sortS].append(str)
        return list(res.values()) 
        #res.values(). 返回 dict_values([group1, group2, group3]) 不是list