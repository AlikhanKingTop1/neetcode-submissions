# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        Solution.max_sum = root.val
        def maxPathSumAtNode(node):
            if not node:
                return 0

            left_sum = max(0, maxPathSumAtNode(node.left))
            right_sum = max(0, maxPathSumAtNode(node.right))

            local_sum = node.val + left_sum + right_sum
            Solution.max_sum = max(Solution.max_sum, local_sum)
            return node.val + max(left_sum,right_sum)

        maxPathSumAtNode(root)
        return  Solution.max_sum