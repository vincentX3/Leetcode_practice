# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root==None:
            return 0

        #先序遍历
        here = self.trace(root, sum) #对于每个节点，视其为树根
        left = self.pathSum(root.left, sum)
        right = self.pathSum(root.right, sum)

        return here + left + right

    def trace(self, root, sum):
        # 求解树根节点到各个节点的路径和等于sum的个数
        if root == None:
            return 0
        else:
            left = self.trace(root.left, sum - root.val)
            right = self.trace(root.right, sum - root.val)
            here = 1 if root.val == sum else 0
            return left + right + here


class Solution_elegant(object):
    # coder: from leetcode @wonderlives
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0: 1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return
            # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1