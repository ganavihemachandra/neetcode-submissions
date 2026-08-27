# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def inorderBuild(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left = inorderBuild(l, mid-1)
            root.right = inorderBuild(mid+1, r)
            return root
        return inorderBuild(0, len(inorder)-1)