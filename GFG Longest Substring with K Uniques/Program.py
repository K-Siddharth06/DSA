class Solution:
    def longestKSubstr(self, s, k):
        n=len(s)
        low=0
        freq={}
        res=-1
        for high in range(n):
            if s[high] in freq:
                freq[s[high]]+=1
            else:
                freq[s[high]]=1
            while len(freq)>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low=low+1
            if len(freq)==k:
                length=high-low+1
                res=max(res,length)
        return res
        
        
        
