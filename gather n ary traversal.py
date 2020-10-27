"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root : return []
        
        cur = []
        next = []
        result = []
        cur.append(root)
        
        while cur:
            each_level = []
            for node in cur:
                each_level.append(node.val)
                for child in node.children:
                    next.append(child)
            cur = next
            result.append(each_level)
            next = []
        
        
        return result