 #Lisp parser

#Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the code and the meaning of each token. For example, if your code is given "(first (list 1 (+ 2 3) 9))", it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

#During your interview, you will pair on writing an interpreter to run the AST. You can start by implementing a single built-in function (for example, +) and add more if you have time.

class Tree:
    def __init__(self, value, children=None):
        self.children = []
        self.value = value
        if children is not None:
            for child in children:
                self.add_child(child)
    def add_child(self, child):
        if not isinstance(child, Tree):
            print("Error: child is not an object of type Tree")
            return(-1)
        else:
            self.children.append(child)
            return(0)
    def __str__(self):
        tree = str(self.value)
        tree += "\n \t"
        if self.children is not None:
            for child in self.children:
                tree += child.__str__()
        return(tree)

testTree = Tree(2)
testTree2 = Tree(3)
testTree3 = Tree(4)

testTree .add_child(testTree2)
testTree .add_child(testTree3)

print(testTree)
