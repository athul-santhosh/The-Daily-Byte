class Solution:
    def identical_tree(self,t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return t1.val == t2.val and self.identical_tree(t1.left,t2.left) and self.identical_tree(t1.right,t2.right)