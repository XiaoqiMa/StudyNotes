# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, upper))

        return True

        # def helper(node, lower=float('-inf'), upper=float('inf')):
        #     if node is None:
        #         return True
        #     if node.val <= lower or node.val >= upper:
        #         return False
        #     if not helper(node.left, lower, node.val):
        #         return False
        #     if not helper(node.right, node.val, upper):
        #         return False
        #     return True
        #
        # return helper(root)






        
# leetcode submit region end(Prohibit modification and deletion)
