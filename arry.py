class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        # import pdb;pdb.set_trace()
        val=list(A)
        val.sort()
        # while len(val)>1:
        for i in range(1,len(val)):
            if val[i-1]==val[i]:
                print(val[i])
            if i not in val:
                print(i)
            
if __name__=='__main__':
    a=Solution()
    a.repeatedNumber((3,1,2,5,3))