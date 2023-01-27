"""
Algorithm Design - HW1 - Samin Mahdipour
"""
answer = []
# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


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
        answer.append(root.data)
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


# Function to construct balanced BST from the given sorted list
def construct(keys, low, high, root):
    # base case
    if low > high:
        return root

    # find the middle element of the current range
    if (low + high) % 2 == 0:
        mid = (low + high) // 2
    else:
        mid = ((low + high) // 2) + 1

    # construct a new node from the middle element and assign it to the root
    root = Node(keys[mid])

    # left subtree of the root will be formed by keys less than middle element
    root.left = construct(keys, low, mid - 1, root.left)

    # right subtree of the root will be formed by keys more than the middle element
    root.right = construct(keys, mid + 1, high, root.right)

    return root


# Function to construct balanced BST from the given unsorted list
def constructBST(keys):
    # sort the keys first
    keys.sort()

    # construct a balanced BST and return the root node of the tree
    return construct(keys, 0, len(keys) - 1, None)


if __name__ == '__main__':

    # Getting input keys
    keys = []
    while True:
        user_input = input()
        if len(user_input) > 0:
            keys.append(int(user_input))
        else:
            break

    # construct a balanced binary search tree
    root = constructBST(keys)
    # level order bst
    levelOrder(root)
    # print level ordered bst
    print(answer)
