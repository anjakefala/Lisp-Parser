 #Lisp parser

#Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the code and the meaning of each token. For example, if your code is given "(first (list 1 (+ 2 3) 9))", it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

#During your interview, you will pair on writing an interpreter to run the AST. You can start by implementing a single built-in function (for example, +) and add more if you have time.

# TODO: RC problem description suggested working with a nested array. Is that a better strategy than working with a Tree object? PROBABLY. But clear-cut objects are how my mind works. Let's try both and see which is easier to work with.

class Tree:
    """
    A generic tree build.
    """

    def __init__(self, value, children=None):
        """
        Initialises a new generic tree build
        PARAMETERS
        value: contains any form of data, depending on the type of data we're tracking with the tree.
        children: type Tree - Pointers to the children of the current node.
        RETURNS
        An initiated Tree object
        """
        self.children = []
        self.value = value
        if children is not None:
            self.add_children(children)

    def add_children(self, children):
        """
        Adds children to a node
        PARAMETERS
        children: A list of tree objects - We need to expand this so it works for adding a single child.
        RETURNS
        int 1; The tree node with had its children record updated with the new children.
        int 0; You didn't give me Tree nodes and so I give you NOTHING.
        """
        for child in children:
        # TODO: this assumes that we are iterating through a list and will crash if children is not a list object
            # We don't want to add a node that isn't a Tree object, now do we? That would be silly.
            if not isinstance(child, Tree):
                print("Error: child is not an object of type Tree")
                return(0)
            else:
                self.children.append(child)
        return(1)

    def __str__(self, level=0):
        """
        A human readable print-out of the tree. This is fairly rudimentary and probably won't be clear if the tree gets more complicated.
        PARAMETERS
        level: The level of the tree that the function is currently printing - used to calculate how much to tab the node's value.
        """
        tree = "\t"*level + str(self.value) + "\n"
        if self.children is not None:
            for child in self.children:
                tree += child.__str__(level+1)
        return(tree)

# Testing testing 1 2 3
tree1 = Tree("+", [Tree(2), Tree(3)])
tree2 = Tree("list", [Tree(1), tree1, Tree(9)])
tree3 = Tree("first", [tree2])

tree3.add_children(tree2)


print(tree3)
