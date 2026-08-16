class Solution(object):
    def maximumSum(self, arr):
        no_delete=arr[0]
        one_delete=float('-inf')
        ans=arr[0]
        for i in range(1,len(arr)):
            x=arr[i]
            one_delete=max(no_delete,one_delete+x)
            no_delete=max(x,no_delete+x)
            ans=max(ans,no_delete,one_delete)
        return ans
        