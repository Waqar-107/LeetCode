# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.ans = 0
        self.depth = 0
    
    def depthCalc(self, nestedList, level):
        self.depth = max(self.depth, level)
        
        for lst in nestedList:
            if not lst.isInteger():
                self.depthCalc(lst.getList(), level + 1)
        
    def solve(self, nestedList, level):
        for lst in nestedList:
            if lst.isInteger():
                self.ans += lst.getInteger() * level
            else:
                self.solve(lst.getList(), level - 1)
                
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.depthCalc(nestedList, 1)
        self.solve(nestedList, self.depth)
        
        return self.ans
