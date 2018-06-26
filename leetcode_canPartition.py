#思路：动态规划，转换成0-1背包问题
#理解为：每个数字看成一件物品，最终的目的就是利用这些物品能否装满背包
#每一件物品的重量，每件物品的价值都等于数字的大小，背包的重量等于所有数字的和的一半
#很无语的一点：python3超时，python2 却AC（只需要将python3代码中的range改为xrange，//改为/即可AC）
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumD=sum(nums)
        if sumD%2:
            return False
        V=sumD//2
        F=[0]*(V+1)
        for i in range(0,len(nums)):
            for v in range(V,nums[i]-1,-1):
                F[v]=max(F[v],F[v-nums[i]]+nums[i])
                if F[v]==V:
                    return True
        return False