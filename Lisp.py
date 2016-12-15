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

def parse_command(command):
    # LISP commands are nested and formatted using brackets
    # We need to check the parantheses are balanced
    assert are_par_balanced(command)

command = "(first (list 1 (+ 2 3) 9))"
parse_command(command)

