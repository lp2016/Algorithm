# -*- coding:utf-8 -*-
#思路：回溯法，全排列问题,不需要确保字典顺序输出结果
import copy
class Solution:
    def __init__(self):
        self.L=0
        self.data=[]
        self.used=[]   #标志某一个元素是否被访问过
        self.result=[]  #记录单个结果
        self.re=set()   #利用set记录全部结果，可去重
    def permuteUnique(self, ss):
        # write code here
        self.L=len(ss)
        if self.L == 0:
            return []
        else:
            self.data = ss
            self.used = [False] * self.L
            self.result = [0] * self.L
            self.PermutationHelper(1)
            return list(map(list,self.re))
    def PermutationHelper(self,level):
        for i in range(0,self.L):    #在每一层需要遍历全部元素
            if not self.used[i]:
                self.result[level-1]=self.data[i]
                self.used[i]=True
                if level!=self.L:
                    self.PermutationHelper(level+1)
                else:
                    self.re.add(tuple(self.result.copy()))
                self.used[i]=False


print(Solution().permuteUnique([3,3,0,3]))

