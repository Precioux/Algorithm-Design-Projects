"""
Algorithm Design - HW1 - Samin Mahdipour
"""
answer = []
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    total_nums = len(nums)
    if not total_nums:
        return None

    mid_node = total_nums // 2
    return TreeNode(
        nums[mid_node],
        sortedArrayToBST(nums[:mid_node]), sortedArrayToBST(nums[mid_node + 1:])
    )


# Function to  print level order traversal of tree
def levelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        currentLevel(root, i)


# Print nodes at a current level
def currentLevel(root, level):
    if root is None:
        return
    if level == 1:
        answer.append(root.val)
    elif level > 1:
        currentLevel(root.left, level - 1)
        currentLevel(root.right, level - 1)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


if __name__ == '__main__':

    # Getting input keys
    keys = []
    while True:
        user_input = input()
        if len(user_input) > 0:
            keys.append(int(user_input))
        else:
            break

    keys.sort()
    root = sortedArrayToBST(keys)
    levelOrder(root)
    print(answer)
