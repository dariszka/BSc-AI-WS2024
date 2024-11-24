from avl_node import AVLNode


class AVLTree:
    class NodeGroup:
        def __init__(self):
            self.a = None
            self.b = None
            self.c = None
            self.t0 = None
            self.t1 = None
            self.t2 = None
            self.t3 = None

    def __init__(self):
        self.root = None
        self.size = 0
        self.to_restruct = None

    def getTreeRoot(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root

    def getTreeHeight(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        return -1 if self.size==0 else self.root.height

    def getSize(self):
        """Return number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size

    def find_by_key(self, key):
        """Returns value of node with given key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        if key is None:
            raise ValueError("Cannot search for null key!")
        current = self.root
        while current is not None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left

        return None

    def insertNode(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. Must not be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if key is None:
            raise ValueError("Null keys are not allowed!")

        n = None # changed it so I can access the node after BST insert loop executes else I'd have to find it again or implement something more complicated for the AVL fixes
        if self.root is None:
            n = AVLNode(key, value)
            self.root = n
        else:
            current = self.root
            while True:
                if current.key == key:
                    return False
                elif current.key < key:
                    if current.right is not None:
                        current = current.right
                    else:
                        n = AVLNode(key, value)
                        self.set_right(current, n)
                        break
                else:
                    if current.left is not None:
                        current = current.left
                    else:
                        n = AVLNode(key, value)
                        self.set_left(current, n)
                        break
        self.size += 1
        # TODO update heights, check AVL integrity, restructure if needed
        self.update_heights(n) # updates heights from inserted node upwards, while checking balance, 
                                # if it finds an imbalance, directly calls restructure without bothering upper nodes
        return True

    def removeNode(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if key is None:
            raise ValueError("Null key is not allowed!")

        parent = None
        current = self.root
        new_sub_root = None

        while not (current is None):
            if current.key == key:
                if parent is None:
                    self.root = self._remove_bst(current)
                    if self.root is not None:
                        self.root.parent = None
                elif parent.left == current:
                    new_sub_root = self._remove_bst(current)
                    self.set_left(parent, new_sub_root)
                elif parent.right == current:
                    new_sub_root = self._remove_bst(current)
                    self.set_right(parent, new_sub_root)
                else:
                    raise ValueError()

                self.size -= 1
                # to_restruct is the node from which the search for the first unbalanced node is started
                if self.to_restruct is not None:
                    while self.to_restruct is not None:
                        # TODO restructure tree until it is balanced
                        self.update_heights(self.to_restruct)
                        balanced = self.check_balance(self.root) # dummy check, since update_heights should always work
                        if balanced:
                            self.to_restruct = None
                return True
            else:
                parent = current
                if current.key > key:
                    current = current.left
                else:
                    current = current.right

        return False

    # auxiliary functions

    def _remove_bst(self, old_sub_root):
        new_sub_root = None
        if old_sub_root.left is None and old_sub_root.right is None:
            new_sub_root = None
            self.to_restruct = old_sub_root.parent
        elif old_sub_root.left is None:
            new_sub_root = old_sub_root.right
            self.to_restruct = new_sub_root
        elif old_sub_root.right is None:
            new_sub_root = old_sub_root.left
            self.to_restruct = new_sub_root
        elif old_sub_root.left.right is None:
            new_sub_root = old_sub_root.left
            self.set_right(new_sub_root, old_sub_root.right)
            self.to_restruct = new_sub_root
        elif old_sub_root.right.left is None:
            new_sub_root = old_sub_root.right
            self.set_left(new_sub_root, old_sub_root.left)
            self.to_restruct = new_sub_root
        else:
            new_sub_root = old_sub_root.left
            while new_sub_root.right is not None:
                new_sub_root = new_sub_root.right
            predecessor_p = new_sub_root.parent
            self.set_right(predecessor_p, new_sub_root.left)
            self.set_right(new_sub_root, old_sub_root.right)
            self.set_left(new_sub_root, old_sub_root.left)
            self.to_restruct = predecessor_p

        return new_sub_root

    def set_left(self, parent, child):
        parent.left = child
        if child is not None:
            child.parent = parent

    def set_right(self, parent, child):
        parent.right = child
        if child is not None:
            child.parent = parent

    def update_heights(self, n):
        current = n

        while current is not None:
            left_height = current.left.height if current.left else -1
            right_height = current.right.height if current.right else -1

            current.height = 1 + max(left_height, right_height)
            balance = abs(left_height - right_height)
            
            if balance > 1: 
                current = self.restructure(current)

            current = current.parent # go upwards and change parent heights

    def restructure(self, z):
        z_parent = z.parent 

        # CHOOSE X, Y, Z, A, B, C AND T0, T1, T2, T3
        z_left_height = z.left.height if z.left else -1
        z_right_height = z.right.height if z.right else -1
        y = z.left if z_left_height > z_right_height else z.right
        
        y_left_height = y.left.height if y.left else -1
        y_right_height =y.right.height if y.right else -1
        x = y.left if y_left_height > y_right_height else y.right
        
        nodes = [x,y,z]
        sorted_nodes = sorted(nodes, key=lambda x: x.key) # can just sort normally since it's inorder 
        a, b, c = sorted_nodes

        T0 = a.left
        if x.key<y.key<z.key: # single rotation
            T1 = a.right 
            T2 = b.right
        elif x.key>y.key>z.key: # single rotation
            T1 = b.left
            T2 = c.left
        else: # double rotation
            T1 = b.left
            T2 = b.right
        T3 = c.right

        # ROTATE (REASSIGN VALUES)
        a.parent = b
        a.left = T0
        if T0:
            T0.parent = a
        a.right = T1
        if T1:
            T1.parent = a 

        b.left = a
        b.right = c
        b.parent = z_parent

        c.parent = b
        c.left = T2
        if T2:
            T2.parent = c
        c.right = T3
        if T3:
            T3.parent = c

        if z_parent:
            if z_parent.left == z:
                z_parent.left = b
            else:
                z_parent.right = b
        else:
            self.root = b

        # FIX HEIGHTS
        a_left_height = a.left.height if a.left else -1
        a_right_height = a.right.height if a.right else -1
        a.height = 1 + max(a_left_height, a_right_height)

        c_left_height = c.left.height if c.left else -1
        c_right_height = c.right.height if c.right else -1
        c.height = 1 + max(c_left_height, c_right_height)

        b.height = 1 + max(b.left.height, b.right.height)

        return b

    def check_balance(self, current):
        # https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/ 
        # used this
        if current:
            left_height = current.left.height if current.left else -1
            right_height = current.right.height if current.right else -1

            if (abs(left_height - right_height) <= 1):
                if self.check_balance(current.left) is True and self.check_balance(current.right) is True:
                    return True

            return False
        else:
            return True  


