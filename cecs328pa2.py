#CECS 328 Programming Assignment 2: Ocean Explorer

#Required Class
class OceanNode:
    def __init__(self, animal = set(), left=None, right=None):
        self.animal = animal
        self.left = left
        self.right = right


def ocean_explore(area : OceanNode, animals):
    """
    Traverses area and looks for animals
    :param area: the binary tree's root node
    :param animals: the animals to look for
    :return: a tuple (defined x = (y,z)) where the first element indicates if the animals were found and the second element indicates at what depth.
    """
    #Define queue
    queue = []
    queue.append(area)
    #Keeping track of the depth with no reference to parents
    depth = 0
    next_cap = 0 #The number of nodes for the next depth
    depth_cap = 1 #number of nodes in current depth
    depth_progress = 0 #number of nodes traversed

    #Level-order traversal
    while len(queue) != 0:
        node = queue.pop()

        #check for animals
        count = 0
        for animal in animals:
            if animal in node.animal:
                count += 1
        if count == len(animals):
            return True, depth

        depth_progress += 1

        #add to the queue
        if node.left is not None:
            queue.append(node.left)
            next_cap += 1
        if node.right is not None:
            queue.append(node.right)
            next_cap += 1

        #Evaluate depth
        if depth_progress == depth_cap:
            depth+= 1
            depth_cap = next_cap
            next_cap = 0
            depth_progress = 0

    #Loop is over, animals not found
    return False,0
