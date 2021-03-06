w# 给定一个二叉树，找出其最小深度。
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最小深度 2. 
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = collections.deque([(1, root)])
        while queue:
            depth, node = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))



        # if root is None:
        #     return 0
        # children = [root.left, root.right]
        # min_depth = float('inf')
        #
        # if not any(children):
        #     return 1
        # for c in children:
        #     if c:
        #         min_depth = min(self.minDepth(c), min_depth)
        # return min_depth + 1

        
# leetcode submit region end(Prohibit modification and deletion)
