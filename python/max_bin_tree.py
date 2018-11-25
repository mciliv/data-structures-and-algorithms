# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1 = TreeNode(2)
print(node1.val)
print(node1.left)
print(node1.right)
node2 = TreeNode(2)
assert(node1.val == node2.val)

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]

        :rtype: TreeNode
        """
        print(nums)
        root_idx = nums.index(max(nums))
        print(nums)
        print(root_idx)
        root = TreeNode(nums[root_idx])


        if root_idx > 0:
            print("in left")
            root.left = self.constructMaximumBinaryTree(nums[:root_idx])
            print("finished_left")


        if root_idx < len(nums) - 1:
            print("in right")
            root.right = self.constructMaximumBinaryTree(nums[root_idx + 1:])
            print("finished_right")


        return root

sol = Solution()
assert(sol.constructMaximumBinaryTree([1]) == TreeNode(1))
