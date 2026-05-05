from typing import Optional
from typing import List

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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        给定一个二叉树，判断它是否是 平衡二叉树

        示例:
            输入:root = [3,9,20,null,null,15,7]
            输出:true
        '''
        def get_hight(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0
            left = get_hight(node.left)
            if left == -1:
                return -1
            right = get_hight(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return get_hight(root) != -1
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        给定一个二叉树的 根节点 root,想象自己站在它的右侧
        按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    
        示例:
            输入:root = [1,2,3,null,5,null,4]
            输出:[1,3,4]
        '''
        ans = []
        def f(node: Optional[TreeNode], n: int) -> None:
            if node == None:
                return
            if n == len(ans):
                ans.append(node.val)
            f(node.right, n + 1)
            f(node.left, n + 1)
        f(root, 0)
        return ans
    
    def isValidBST_1(self, root: Optional[TreeNode], left = int('-inf'), right = int('inf')) -> bool:
        '''
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

        有效 二叉搜索树定义如下：

            节点的左子树只包含 严格小于 当前节点的数。
            节点的右子树只包含 严格大于 当前节点的数。
            所有左子树和右子树自身必须也是二叉搜索树。

        示例:
            输入:root = [2,1,3]
            输出:true
        '''
        if root == None:
            return True
        x = left < root.val < right
        v = self.isValidBST_1(root.left, left, root.val)
        n = self.isValidBST_1(root.right, root.val, right)
        return x and v and n
    
    p = int('-inf')
    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        '''
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

        有效 二叉搜索树定义如下：

            节点的左子树只包含 严格小于 当前节点的数。
            节点的右子树只包含 严格大于 当前节点的数。
            所有左子树和右子树自身必须也是二叉搜索树。

        示例:
            输入:root = [2,1,3]
            输出:true
        '''
        if root == None:
            return True
        if self.isValidBST_2(root.left) == False:
            return False
        if root.val <= self.p:
            return False
        self.p = root.val
        return self.isValidBST_2(root.right)
    
    def isValidBST_3(self, root: Optional[TreeNode]) -> bool:
        '''
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

        有效 二叉搜索树定义如下：

            节点的左子树只包含 严格小于 当前节点的数。
            节点的右子树只包含 严格大于 当前节点的数。
            所有左子树和右子树自身必须也是二叉搜索树。

        示例:
            输入:root = [2,1,3]
            输出:true
        '''
        def f(node: Optional[TreeNode]) -> List[int]:
            if node == None:
                return int('inf'), int('-inf')
            left_min, left_max = f(node.left)
            right_min, right_max = f(node.right)
            x = node.val
            if left_max >= x or right_min <= x:
                return int('-inf'), int('inf')
            return min(left_min, x), max(right_max, x)
        return f(root)[1] != int('inf')