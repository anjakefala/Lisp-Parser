 #Lisp parser

#Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the code and the meaning of each token. For example, if your code is given "(first (list 1 (+ 2 3) 9))", it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

#During your interview, you will pair on writing an interpreter to run the AST. You can start by implementing a single built-in function (for example, +) and add more if you have time.

class Tree:
    """
    A generic tree build.
    """
    def __init__(self, value, children=None):
        self.children = []
        self.value = value
        if children is not None:
            self.add_children(children)
    def add_children(self, children):
        for child in children:
            if not isinstance(child, Tree):
                print("Error: child is not an object of type Tree")
                return(0)
            else:
                self.children.append(child)
        return(1)
    def __str__(self, level=0):
        tree = "\t"*level + str(self.value) + "\n"
        if self.children is not None:
            for child in self.children:
                tree += child.__str__(level+1)
        return(tree)

tree1 = Tree("+", [Tree(2), Tree(3)])
tree2 = Tree("list", [Tree(1), tree1, Tree(9)])
tree3 = Tree("first", [tree2])



print(tree3)
