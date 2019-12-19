# coding=utf-8

'''

非递归有难度,我是从别人的C++代码改的

前序数组第一个值是根节点的
中序数组第一个值是左子树叶子节点的

我们用一个栈保存已经遍历过的节点，遍历前序遍历的数组，一直作为当前根节点的左子树，直到当前节点和中序遍历的数组的节点相等了，那么我们正序遍历中序遍历的数组，倒着遍历已经遍历过的根节点（用栈的 pop 实现），找到最后一次相等的位置，把当前前序遍历的节点作为该节点的右子树。

'''

# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not preorder and not inorder:
      return
    root = TreeNode(preorder[0])
    S = []
    S.append(root)
    # 前序的索引
    i = 1
    # 中序的索引
    j = 0
    while i < len(preorder):
      back = None
      while S and S[0].val == inorder[j]:
        back = S[0]
        del S[0]
        j += 1
      curr = TreeNode(preorder[i])
      if back:
        back.right = curr
      else:
        S[0].left = curr
      S.insert(0, curr)
      i += 1
    return root
