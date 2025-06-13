from modules.CLI import *

# v0.3

"""
HEY VSAUCE... RAY HERE...
I'M INSIDE YOUR HOUSE... 
I'M KIDDING... OR AM I???

I SUCK AT MATRIX MULTIPLICATION
SO I THOUGHT I SHOULD CRAFT THIS...

NOW I'VE COME TO KNOW... 
I SUCK AT THIS TOO, BRUH!!!
"""

matrix = list[list[int]]

def shape(M: matrix) -> str:
    """
    HER EXPERTISE IS IDENTIFYING "THE SHAPE" (NOT MICHAEL),
    "THE SHAPE" OF THE GIVEN MATRIX.
    """
    if all(all(cell == 0 for cell in row) for row in M):
        return "NULL MATRIX"
    nR, nC = size(M)
    if nR == 1 and nC == 1:
        return "SINGLETON MATRIX"
    elif nR == nC:
        diag = all(M[i][j] == 0 for i in range(nR) for j in range(nC) if i != j)
        if diag:
            if all(M[i][i] == 1 for i in range(nR)):
                return "IDENTITY MATRIX"
            return "DIAGONAL MATRIX"
        return "SQUARE MATRIX"
    elif nR == 1:
        return "ROW MATRIX"
    elif nC == 1:
        return "COLUMN MATRIX"
    return "RECTANGULAR MATRIX"


def size(M: matrix) -> list:
    """
    SHE'LL GIVES YOU
    SIZE OF THE MATRIX!!!
    """
    return [len(M), len(M[0])]


def isValid(M: matrix) -> bool:
    """
    SHE CHECKS IF THE GIVEN MATRIX IS REALLY A MATRIX OR...
    (LONG PAUSE) .... NOT!
    """
    if not M or not isinstance(M, list) or not all(isinstance(row, list) for row in M):
        return False
    nC = len(M[0])
    return all(len(row) == nC for row in M)


def fromMatrix(M: matrix) -> list:
    """
    UH... SHE CONVERTS A MATRIX INTO A JUICY LIST!
    """
    if isValid(M):
        return [element for row in M for element in row]
    return []

def toMatrix(Mlist: list, nRC: list) -> list | None:
    """
    VICE-VERSA
    """
    if isinstance(Mlist, list):
        nR, nC = nRC
        if len(Mlist) != nR * nC:
            return None
        M = [Mlist[i*nC:(i+1)*nC] for i in range(nR)]
        if isValid(M):
            return M
    return None

def addM(A: matrix, B: matrix) -> matrix:
    """
    A: matrix + B: matrix = C: matrix (C for combination)
    """
    MlistA, MlistB = fromMatrix(A), fromMatrix(B)
    return toMatrix([a + b for a, b in zip(MlistA, MlistB)], size(A))

def subM(A: matrix, B: matrix) -> matrix:
    """
    subtractMATRIX()
    """
    MlistA, MlistB = fromMatrix(A), fromMatrix(B)
    return toMatrix([a - b for a, b in zip(MlistA, MlistB)], size(A))

def mulM(A: matrix, B: matrix) -> matrix | str:
    """
    MULTIPLICATION IS ALWAYS A PAIN IN THE ASS
    """
    if not (isValid(A) and isValid(B)):
        return f"{RED}E:{RST} INVALID INPUT"
    rA, cA = size(A)
    rB, cB = size(B)
    if cA != rB:
        return f"{BRIGHT_RED}E:{RST} NOT POSSIBLE TO MULTIPLY!"
    return [[sum(A[i][k] * B[k][j] for k in range(cA)) for j in range(cB)] for i in range(rA)]

def inputM():
    """
    SOON... SHE'LL TAKE AN INPUT AND SEEMLESSLY
    (HOPEFULLY) AND CONVERT HER INTO A MATRIX
    FOR THE COMPUTER TO UNDERSTAND AND COMPUTE.
    """
    pass

def printM(M: matrix, name: str = "M") -> None:
    """
    SHE'LL GIVE AN OUTPUT LIKE:
    M = [1, 2]    A - B = [1, 0, 0]
        [3, 4] OR         [0, 1, 0]
        [5, 6]            [0, 0, 1]
    """
    if not isValid(M):
        print(f"{RED}E:{RST} INVALID MATRIX")
        return
    print(f"{name} = [{', '.join(map(str, M[0]))}]")
    for row in M[1:]:
        print(f"{' ' * (len(name) + 3)}[{', '.join(map(str, row))}]")

def trnsp(M: matrix) -> matrix | str:
    """
    [1, 2, 3]                    [1, 4, 7]
    [4, 5, 6] SHE'LL MAKE HER TO [2, 5, 8]
    [7, 8, 9]                    [3, 6, 9]

    ROW BECOMES COLUMN AND VICE-VERSA
    """
    if not isValid(M):
        return f"{BRIGHT_RED}E:{RST} INVALID MATRIX"
    return [list(row) for row in zip(*M)]

def isEqual(A: matrix, B: matrix) -> bool:
    """
    SHE CHECKS IF THE MATRCIES ARE = OR NOT
    THE SHE'LL GIVE THE BOOLEAN VALUE FOR THE SAME.
    """
    if not (isValid(A) and isValid(B)):
        return False
    return A == B

# soon i'll start using *args and shit... rn, just bare with it... 

HELP += f"""
ADD | PLUS ------------ COMBINES THE GIVEN MATRICES
SUB | MINUS ----------- DEDUCTS THE GIVEN MATRICES
MUL | TIMES ----------- MULTIPLIES THE GIVEN MATRICES
TYPE | SHAPE ---------- TELLS THE SHAPE OF THE MATRIX
SIZE | nRC ----- SHOWS MATRIX nRC
{RST}""" # sorry but it won't work... just now

def main() -> None:
    clear()
    penny()
    print(f"{CYAN}YOU'VE STEPPED INTO MATRIX DOME\n{RST}")
    time.sleep(1)

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9] # edit from here... 
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nRC_A = [3, 3]
    nRC_B = [3, 3] # to here
    A = toMatrix(A, nRC_A)
    B = toMatrix(B, nRC_B) 
    
    printM(A, "A")
    printM(B, "B")

    printM(trnsp(A), "A")
    printM(trnsp(B), "B")

    print(f"""
    A == B = {isEqual(A, B)}

    SHAPE OF A = {shape(A, nRC_A)}
    SHAPE OF B = {shape(B, nRC_B)}

    SHAPE OF A = {size(A)}
    SHAPE OF B = {size(B)}
    """)
    
    printM(addM(A, B), "A + B")
    printM(subM(A, B), "A - B")

    printM(mulM(A, B), "A * B")
    printM(mulM(B, A), "B * A")

if __name__ == "__main__":
    main()

"""
FUCK SCHOOL...
IT'S MY WAY OR THE HIGHWAY...
BUT WHAT IF I AM THE ONE...
WHO'LL BE LIVING ON THE HIGHWAY...
A YEAR FROM NOW?

NOTHING IS CERTAIN 

(YOU WON'T GET IT... TRY SEARCHING 
FOR THAT TERM IN YOUTUBE MUSIC AND 
LOOK FOR A MOVIE SCORE!!! THAT'S 
NOT ONE OF THE GOOD ONES IN THE 
FRANCHISE BUT IT'S WATCHABLE. THEY
SAY ITS THE FINAL BUT I HOPE NOT)
"""
