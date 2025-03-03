def maximum_diameter(root):
    diameter = 0
    
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        diameter = max(diameter, left+right)
        
        return 1+ max(left, right)
    
    dfs(root)
    
    return diameter