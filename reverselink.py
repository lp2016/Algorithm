# -*- coding:utf-8 -*-
#python 2.7.3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        if listNode == None:
            return result
        else:
            p = listNode
            while p:
                result.append(p.val)
                p = p.next
            L = len(result)
            for i in xrange(0, int(L / 2)):
                result[i], result[L - 1 - i] = result[L - 1 - i], result[i]
            return result
