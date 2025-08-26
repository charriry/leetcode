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
    def pathSum(self,root:TreeNode,target):
        """
        维护n个值，分别表示以每个节点为起点的路径对应的和
        """
        self.ans = 0
        stack = [] #第i个元素表示第i个节点为起点，到目前访问的节点的路径和
        def dfs(node):
            nonlocal stack
            if not node:
                return []
            #stack.append(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(len(left)):
                left[i] += node.val
                if left[i] == target:
                    self.ans += 1
            for i in range(len(right)):
                right[i] += node.val
                if right[i] == target:
                    self.ans += 1
            return left + right + [node.val]
        dfs(root)
        return self.ans
    #一个节点的最近公共祖先
    def lowerCommonAncestor(self,root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
        node = root
        result = []
        #找到p和q的发现路径

        #使用循环找出根节点到目标节点的路径

        def find_path(root,p,q):
            find_p = False
            stack = [(root,[root])]
            while stack:
                node, path = stack.pop()
                if node is p:
                    if find_p:
                        result.append(path)
                        return result
                    find_p = True
                    p = q
                    result.append(path)
                    continue
                if node.right:
                    stack.append((node.right,path+[node.right]))
                if node.left:
                    stack.append((node.left,path+[node.left]))
        result = find_path(root,p,q)
        #path_q = find_path(root,q)
            

        # def find_path(node,p,path):
        #     if not node:
        #         return 
        #     path.append(node)
        #     if node is p:
        #         result.append(path[:])
        #     temp = []
        #     if node.left:
        #         temp.append(node.left)
        #     if node.right:
        #         temp.append(node.right)
        #     for n in temp:
        #         find_path(n,p,path)
        #         path.pop()

        # path_p = find_path(root,p)
        # find_path(root,q,path_q)
        i = 0
        n,m = len(result[0]),len(result[1])
        while i < min(n,m):
            if result[0][i] != result[1][i]:
                return result[0][i-1]
            i += 1
        return result[0][i-1]
            

    #二叉树的最大路径和
    def maxpathSum(self,root:TreeNode)->int:
        self.ans = -1001
        def dfs(node):
            """
            返回使用这个节点的最大路径和
            """
            if not node:
                return 0
            left= dfs(node.left)
            right= dfs(node.right)

            #判断是否是最大路径
            self.ans = max(left,right,left+node.val,left+node.val+right,right+node.val,self.ans)
            return max(node.val,left+node.val,right+node.val)
        dfs(root)
        return self.ans



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
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    #root.left.left.left = TreeNode(3)
    #root.left.left.right = TreeNode(-2)
    #root.left.right = TreeNode(2)
    #root.left.right.right = TreeNode(1)
    root.right.right = TreeNode(7)
    a = Solution()
    print(a.maxpathSum(root))
