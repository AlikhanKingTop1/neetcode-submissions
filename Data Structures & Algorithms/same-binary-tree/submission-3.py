# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            
            if not node:
                res.append(None)
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.func(p) == self.func(q)
    
        # res1 = []
        # stack1 = [p]
        # while stack1:
        #     node = stack1.pop()
        #     res1.append(node.val)
        #     if node.right:
        #         stack1.append(node.right)
        #     else:
        #         res1.append(None)
        #     if node.left:
        #         stack1.append(node.left)
        #     else:
        #         res1.append(None)

        # res2 = []
        # stack2 = [q]
        # while stack2:
        #     node = stack2.pop()
        #     res2.append(node.val)
        #     if node.right:
        #         stack2.append(node.right)
        #     else:
        #         res2.append(None)
        #     if node.left:
        #         stack2.append(node.left)
        #     else:
        #         res2.append(None)
        # return res1 == res2 
                