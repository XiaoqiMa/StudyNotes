# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  示例: 
# 
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(queue, xy_dif, xy_sum):
            p = len(queue)
            if p == n:
                ans.append(queue)
                return
            for q in range(n):
                if q not in queue and p-q not in xy_dif and p+q not in xy_sum:
                    backtrack(queue + [q], xy_dif + [p-q], xy_sum + [p+q])

        ans = []
        backtrack([], [], [])

        return [['.' * i + 'Q' + '.' * (n-i-1) for i in sol] for sol in ans]

        
# leetcode submit region end(Prohibit modification and deletion)
