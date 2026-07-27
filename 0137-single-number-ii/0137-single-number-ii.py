class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v==1:
                return k
        '''

        val = sorted(nums)
        for i in range(0,len(val)-1,3):
            if val[i] != val[i+1]:
                return val[i]
        return val[-1]
            
        