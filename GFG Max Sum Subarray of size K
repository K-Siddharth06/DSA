class Solution:
    def maxSubarraySum(self, arr, k):
        low=0
        high=k-1
        win_sum=0
        for i in range(low,high+1):
            win_sum=win_sum+arr[i]
            n=len(arr)
        res=win_sum
        while high<n:
            res=max(res,win_sum)
            low=low+1
            high=high+1
            if high==n:
                break
            win_sum=win_sum-arr[low-1]
            win_sum=win_sum+arr[high]
        return res
        
