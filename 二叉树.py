class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #二叉树直径
    def depth(self,node):
        self.diameter = 0
        if not node:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return max(left_depth, right_depth)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
    
    #二叉树的层序遍历
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(level)
            queue = next_queue
        return result
    # 将有序数组转为平衡二叉搜索树
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])#左子树比右子树更小
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
    #验证二叉搜索树
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root,lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.left,lower,root.val) and helper(root.right,root.val,upper)
        return helper(root)
    
    # 二叉树的中序遍历
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        node = root
        while node:
            if not node.left:
                result.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = node
                    node = node.left
                else:
                    result.append(node.val)
                    node = node.right
        return result
    
    #二叉搜索树中第k小的元素
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # """
        # 中序遍历到第k个元素即为第k小的元素
        # """
        # result = []
        # temp = []
        # while root or temp:
        #     while root:
        #         temp.append(root)
        #         root = root.left
        #     root = temp.pop()
        #     result.append(root.val)
        #     if len(result) == k:
        #         return root.val
        #     root = root.right
        # return -1  # 如果k大于树的节点数，返回-1或抛出异常
        """
        根据子树节点数量判断位置
        """
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        while root:
            left_count = count_nodes(root.left)
            if left_count == k - 1:
                return root.val
            elif left_count < k - 1:
                k -= left_count + 1
                root = root.right
            else:
                root = root.left
                #k -= 1
            return -1
    
    #树的右视图
    def rightSidewView(self,root):
        """
        层序遍历取最后一个元素
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(level[-1])
            queue = next_queue
        return result
    #二叉树展开为单向链表
    def flatten(self,root):
        """
        按照左边递归，无左边之后返回右递归
        """
        right_temp = []
        def dfs(node):
            if not node:
                return 
            if node.left:
                temp = node.right
                node.right = node.left
                node.left = None
                if temp:
                    right_temp.append(temp)
            else:
                if not node.right and right_temp:
                    node.right = right_temp.pop()
            dfs(node.right)
            
        dfs(root)
        return root
    
    #从中序遍历和前序遍历构建二叉树
    def buildTree(self,preorder:list[int],inorder:list[int])->TreeNode:

        #建立哈希映射
        dict_1 = {}
        for ele in preorder:
            dict_1[ele] = 0
        for i in range(len(inorder)):
            ele = inorder[i]
            dict_1[ele] = i
        
        n = len(preorder)
        
        def dfs(left_pre,right_pre,inorder_left,inorder_right):
            if left_pre<=right_pre:
                return None
            #preorder_root = left_pre

            #找出中序遍历之中根节点位置
            inorder_root = dict_1[preorder[left_pre]]

            #建立根节点
            root = TreeNode(preorder[left_pre])

            #获取左子树数目
            num_left = inorder_root - inorder_left

            root.left = dfs(left_pre+1,left_pre+num_left+1,inorder_left,inorder_root)
            root.right = dfs(left_pre+num_left+1,right_pre,inorder_root,inorder_right)
            return root
        return dfs(0,n-1,0,n-1)


#将二叉树转为数组
def tree_list_to_array(head):
    result = []
    if not head:
        return result
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
            if not node.left and not node.right:
                continue
            #result.append(None)
    return result
 
if __name__ == "__main__":
    preorde = [3,9,20,15,7]
    inorde = [9,3,15,20,7]
    a = Solution()
    # root.right.left.right = TreeNode(5)
    # root.right.left.left.left = TreeNode(6)
    print(a.buildTree(preorde,inorde))