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
    # Error Checking
    if not isinstance(command, str):
        raise ValueError
    # A Lisp command must start with "("
    if "(" != command[0]:
        raise SyntaxError

    par_stack = []
    for c in command:
        # If we find an open parantheses, we push it onto the stack
        # This allows us to track that we will need a corresponding closing parantheses
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
    assert isinstance(s, str)
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
    assert isinstance(s, str)
    try:
        float(s)
        return True
    except ValueError:
        return False

def atomic_expression(command):
    """
    Takes a string which represents a LISP command and translates it into a list of atomic expressions for further parsing
    PARAMETERS
    command: String, a legal LISP command
    RETURNS
    atoms: list, contains the atomic expressions of the LISP command
    """
    # Error Checking
    if not isinstance(command, str):
        raise ValueError
    # A LISP command must start with "("
    if "(" != command[0]:
        raise SyntaxError

    print("Original command pre-processing: " + command)

    # All the atomic expressions have spaces between them except "(" and ")" If we pad "(" and ")" with spaces, we can easily use .split(" ") to create a list of the atomic expressions
    command = command.replace("(", " ( ")
    command = command.replace(")", " ) ")
    atoms = command.split(" ")

    # We have some cells in the list that are just a blank space, so let's remove those
    while "" in atoms:
        atoms.remove("")

    # Typecasting the numbers
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
        i += 1
    print("Processed list of atomic expressions: " + str(atoms))
    return(atoms)

def abstract_syntax_tree(atoms):
    print(atoms)
    return(atoms)

def parse_command(command):
    """
    Takes an input program, verifies its syntax and translates it into an abstract syntax tree.
    PARAMETERS
    command: String, a legal LISP command
    RETURNS
    AST: List, an abstract syntax tree which represents the LIST command
    """
    # Syntax Assumption: Parantheses must be balanced
    if not are_par_balanced(command):
        raise SyntaxError

    atoms = atomic_expression(command)
    AST = abstract_syntax_tree(atoms)
    return(AST)

def execute_command(AST):
    # We'll be working on this during the pair programming assignment
    # Note: Strings will be represented as ' " ___ "  ', function calls and variable names will be represented '______'
    # In LISP, t --> True; nil --> False
    # We are assuming the numbers should already have been converted
    return(AST)

command = '("first" (list "1" (+ -2 3) 9.2))'
AST= parse_command(command)
#execute_command(abstractSyntaxTree)
