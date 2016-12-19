 #Lisp parser

#Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the code and the meaning of each token. For example, if your code is given "(first (list 1 (+ 2 3) 9))", it could return a nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

#During your interview, you will pair on writing an interpreter to run the AST. You can start by implementing a single built-in function (for example, +) and add more if you have time.


def are_par_balanced(command):
    """
    Checks that the parantheses in the Lisp command are balanced
    PARAMETERS
    command: String, a Lisp command
    RETURNS
    True: If the parantheses are balanced
    False: If the parantheses are not balanced
    """
    ##### Error Checking#####
    if not isinstance(command, str):
        raise ValueError
    # A Lisp command must start with "("
    if "(" != command[0]:
        raise SyntaxError

    ##### Code #####
    par_stack = []
    for c in command:
        # If we find an open parantheses, we push it onto the stack
        # This allows us to keep track of how many open par.s will need a corresponding closing par.s
        if c == "(":
            par_stack.append(c)
        # If we find a close parantheses, we pop an open par off the stack
        # Because it has been matched
        elif c == ")":
            # If it is not possible to pop the stack to match every closing symbol, the parentheses are not balanced
            if par_stack == []:
                return(False)
            else:
                par_stack.pop()
    # At the end, the stack should be empty, because every open parantheses should have a match
    if par_stack == []:
        return(True)
    else:
        return(False)

def is_int(s):
    """
    Evaluates whether a string represents a positive integer.
    PARAMETERS
    s: String, a single word
    RETURNS
    True: If that word can be interpreted as a positive integer: Returns True for: '2', '10'
    False: If that word cannot be intepreted as a positive integer: Returns False for: ' "2" ', '2.3', '-2'
    """
    ###### Error Checking #####
    assert isinstance(s, str)

    ###### Code #####
    return s.isdigit()

def is_float(s):
    """
    Evaluates whether a string represents a number
    PARAMETERS
    s: String, a single word
    RETURNS
    True: If that word can be interpreted as a number: Returns True for '2.3', '-2'
    False: If that word does not represent a number: Returns False for ' "2.3" ', 'cabbages'
    """
    ##### Error Checking #####
    assert isinstance(s, str)
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_bool_true(s):
    """
    Evaluates whether a string represents the LISP boolean value for True
    PARAMETERS
    s: String, a single word
    RETURNS
    True: If the string represents the LISP literal for True
    False: Otherwise
    """
    assert isinstance(s, str)
    if s == "t":
        return True

def is_bool_false(s):
    """
    Evaluates whether a string represents the LISP boolean value for False
    PARAMETERS:
    s: String, a single word
    RETURNS
    True: If the string represents the LISP literal for False
    False: Otherwise
    """
    assert isinstance(s, str)
    if s == "nil":
        return True

def atomic_expression(command):
    """
    Takes a string which represents a LISP command and translates it into a list of atomic expressions for further parsing
    An atomic expression is an expression which can't be broken down further e.g. 1, 'A', +, '(', ')'
    This stage is known as "lexical analysis"
    PARAMETERS
    command: String, a legal LISP command PLEASE
    RETURNS
    atoms: list, contains the atomic expressions of the LISP command
    """
    ##### Error Checking #####
    if not isinstance(command, str):
        raise ValueError
    # A LISP command must start with "("
    if "(" != command[0]:
        raise SyntaxError

    ##### Code #####
    # To avoid silent failures. We like to fail loudly in these parts.
    print("Original command pre-processing: " + command)

    # All the atomic expressions have spaces between them except "(" and ")" If we pad "(" and ")" with spaces, we can use .split(" ") to create a list of the atomic expressions
    command = command.replace("(", " ( ")
    command = command.replace(")", " ) ")
    atoms = command.split(" ")

    # We have some cells in the list that are just a blank space, so let's remove those
    while "" in atoms:
        atoms.remove("")

    # We are going to use this opportunity to identify the atoms representing LISP numbers and convert them from Python Strings into Python numbers
    i = 0
    for atom in atoms:
        # Does the atom represent an integer?
        if is_int(atom):
            atoms[i] = int(atom)
            i += 1
            continue
        # Does this atom represent a floating point number?
        elif is_float(atom):
            atoms[i] = float(atom)
            i += 1
            continue
        elif is_bool_true(atom):
            atoms[i] = True
        elif is_bool_false(atom):
            atoms[i] = False
        i += 1

    # Compare with the pre-processed expression to ensure that everything looks fine.
    print("Final processed sequence of atomic expressions: " + str(atoms))

    assert isinstance(atoms, list)
    assert atoms[0] == "("
    assert atoms[-1] == ")"
    return(atoms)

def abstract_syntax_tree(atoms):
    """
    Takes a sequence of atomic expressions and assembles them into an abstract syntax tree.
    This is a container for the recursive function that actually does the work.
    PARAMETERS
    atoms: List, a sequence of LISP atomic expressions
    RETURNS
    ast: List, a nested array which represents the abstract syntax tree based on the atoms
    """
    ##### Error Checking #####
    assert isinstance(atoms, list)

    ##### Code #####
    # blank is an additional return value that the recursive function needs to work but the user only really requires the tree.
    ast, blank = abstract_syntax_tree_rec(atoms)

    assert isinstance(ast, list)
    return(ast)

def abstract_syntax_tree_rec(atoms):
    """
    The recursive function for which abstract_syntax_tree is a container for.
    For each '(' assembles a sub-expression in an abstract syntax tree until a ')'
    PARAMETERS
    atoms: List, a sequence of atomic expressions for which we wish to build a tree
    RETURNS
    ast: The abstract syntax sub-tree that represents atomic expressions between a '(' and ')'
    i: Index into the particular ')' in atoms for which the current ast was built
    """

    ##### Error Checking #####
    # This code assumes that the sub-expression its evaluating is bounded by match par.s
    # If those matching par.s aren't there, everything breaks.
    # So let's make sure they're there.
    assert atoms[0] == "("
    assert atoms[-1] == ")"

    ##### Code #####
    # We begin by building a new tree
    ast = []
    i = 1
    #print("Starting a new sub-tree.")
    # Until we hit a closing par.s
    while atoms[i] != ")":
        # We look at the current atom
        atom = atoms[i]
        #print("Current atom: "+ str(atom))
        # If it is a new open par.s
        if atom == "(":

            #print("AST before recursion: " + str(ast))

            # We start building a brand new sub-tree and obtain the index that tells us where that sub-expression ends in our atomic expression sequence
            subTree, iUpdate = abstract_syntax_tree_rec(atoms[i:])
            # Add the sub-tree to our abstract syntax tree
            ast.append(subTree)

            #print("New AST after recursion" + str(ast))

            # We update our index so that we can move on to the next atomic expression
            i += iUpdate

            assert i < len(atoms)

        # If the atom isn't a '(' or a ')'
        else:
            # Add it to the abstract syntax tree
            ast.append(atom)
            #print("New ast after adding atom:" + str(ast))
        i += 1

    # If we hit a closing ')', we want to return the current sub-tree and the index in the atomic expression sequence that we just finished processing
    #print("Returning AST:" + str(ast))
    return(ast, i)

def parse_command(command):
    """
    Takes an input program, verifies its syntax and translates it into an abstract syntax tree.
    PARAMETERS
    command: String, a legal LISP command
    RETURNS
    ast: List, an abstract syntax tree which represents the LISP command
    """

    ##### Error Checking #####
    # Syntax Assumption: Parantheses must be balanced
    if not are_par_balanced(command):
        raise SyntaxError

    ##### Code #####
    # Obtains the sequence of atomic expressions
    atoms = atomic_expression(command)
    # Translates that sequence in an abstract syntax tree
    ast = abstract_syntax_tree(atoms)

    print("Final abstract syntax tree: " + str(ast))

    return(ast)

def execute_command(ast):
    # We'll be working on this during the pair programming assignment
    # Note: Strings will be represented as ' " ___ "  ', function calls and variable names will be represented '______'
    # In LISP, t --> True; nil --> False
    # We are assuming the numbers should already have been converted
    return(ast)

# The LISP command we want to execute
command = '(first (list 1 (+ 2 3) 9))'
# First we want  to convert the command into an abstract syntax tree
ast= parse_command(command)
print("Correct answer is ['first', ['list', 1, ['+', 2, 3], 9]]")

# Then we wish to execute the command
#execute_command(abstractSyntaxTree)
