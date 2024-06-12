import sys

class TreeNode:
    def __init__(val, left, right):
        self.val = val
        self.left = left
        self.right = right
    

class Tree:
    def __init__():
        pass
    
    '''
    def add(v):
        pass

    def remove(v):
        pass

    def modify(origal, target):
        pass
    '''

    def search(TreeNode):
        if TreeNode == None:
            return

        print(TreeNode.val)    
        search(TreeNode.left)
        search(TreeNode.right)