from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        '''
        给定一个二叉树 root ，返回其最大深度。
        二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

        示例:
            输入:root = [3,9,20,null,null,15,7]
            输出:3
        '''
        if root is None:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        return max(right, left) + 1
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        '''
        给定一个二叉树 root ，返回其最大深度。
        二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

        示例:
            输入:root = [3,9,20,null,null,15,7]
            输出:3
        '''
        a = 0
        def f(node: Optional[TreeNode], n: int) -> None:
            if node is None:
                return
            n += 1
            nonlocal a
            a = max(a, n)
            f(node.left, n)
            f(node.right, n)
        f(root, 0)
        return a
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
        如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

        示例:
            输入:p = [1,2,3], q = [1,2,3]
            输出:True
        '''
        if q == None or p == None:
            return q == p
        return q.val == p.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        给你一个二叉树的根节点 root , 检查它是否轴对称。
        
        示例:
            输入:root = [1,2,2,3,4,4,3]
            输出:true
        '''
        def f(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if q == None or p == None:
                return q == p
            return q.val == p.val and f(q.left, p.right) and f(q.right, p.left)
        return f(root.left ,root.right)
