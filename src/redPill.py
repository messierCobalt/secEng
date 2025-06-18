from IMF.hunt import *

__version__ = "v0.3.2"

matrix = list[list[int]] # py_3.8 and below would choke on this...

def shape(M: matrix) -> str:
    """
    HE IS "THE SHAPE"... NO HE'S NOT MICHAEL MYERS...
    I MEANT... HE INDENTIFIES "THE SHAPE" OF THE GIVEN MATRIX...
    - 'NULL MATRIX' IF M = [0]
    - 'SINGLETON MATRIX' IF 1x1
    - 'IDENTITY MATRIX' OR 'DIAGONAL MATRIX' IF SQ. WITH ONLY DIAG. NON-0.
    - 'SQUARE MATRIX' IF SQ. BUT NOT DIAG.
    - 'ROW MATRIX' 1xC
    - 'COLUMN MATRIX' Rx1
    - 'RECTANGULAR MATRIX' OTHERWISE
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
    SHE'LL GIVES YOU SIZE OF THE MATRIX!!!
    LIKE: [2, 3] -- 2 ROWS, 3 COLS
    """
    return [len(M), len(M[0])]

def vCHECK(M: matrix) -> bool:
    """
    CHECKS IF THE GIVEN MATRIX IS REALLY A MATRIX OR...
    (LONG PAUSE) ... NOT!

    V-CHECK... KINDA LIKE THE V-CARD... NO NOT THAT V-CARD... 
    BUT THE VALIDITY-CARD... YOU ARE REALLY DIRTY-MINDED...
    """
    if not M or not isinstance(M, list) or not all(isinstance(row, list) for row in M):
        return False
    nC = len(M[0])
    return all(len(row) == nC for row in M)


def fromMatrix(M: matrix) -> list: # i once named my downloads folder that... ah, i once had a downloads folder
    """
    UH... IT CONVERTS THE MATRIX--THE MATRIX IS EVERYWHERE... INTO A JUICY LIST!
    """
    if vCHECK(M):
        return [element for row in M for element in row]
    return []

def toMatrix(flat: list, nRC: list) -> list | None:
    """
    AND VICE-VERSA
    """
    if isinstance(flat, list):
        nR, nC = nRC
        if len(flat) != nR * nC:
            return None
        M = [flat[i*nC:(i+1)*nC] for i in range(nR)]
        if vCHECK(M):
            return M
    return None

def love(A: matrix, B: matrix) -> matrix:
    """
    A: matrix + B: matrix -> C: matrix # (C for combination)
    """
    flatA, flatB = fromMatrix(A), fromMatrix(B)
    return toMatrix([a + b for a, b in zip(flatA, flatB)], size(A))

def hate(A: matrix, B: matrix) -> matrix:
    """
    subtractMATRIX(A: matrix - B: matrix) -> matrix
    """
    flatA, flatB = fromMatrix(A), fromMatrix(B)
    return toMatrix([a - b for a, b in zip(flatA, flatB)], size(A))

def bond(A: matrix, B: matrix) -> matrix | str:
    """
    MATRIX MULTIPLICATION IS ALWAYS A PAIN IN THE ASS
    """
    if not (vCHECK(A) and vCHECK(B)):
        return f"{RED}E:{RST} INVALID INPUT"
    rA, cA = size(A)
    rB, cB = size(B)
    if cA != rB:
        return f"{BRIGHT_RED}E:{RST} NOT POSSIBLE TO MULTIPLY!"
    return [[sum(A[i][k] * B[k][j] for k in range(cA)) for j in range(cB)] for i in range(rA)]

def take(Mname: str = "M = ") -> matrix:
    """
    SHE TAKES MATRIX VALUES FROM THE USER, FROM...
    """
    while True:
        try:
            Minput = input(f"{BRIGHT_CYAN}{Mname}{RST}").strip()
            M = [list(map(int, row.strip().split(','))) for row in Minput.strip().split(';')]
            if vCHECK(M):
                return M
            else:
                print(f"{BRIGHT_RED}E:{RST} INVALID MATRIX STRUCTURE")
        except ValueError:
            print(f"{BRIGHT_RED}E:{RST} NON-INTEGER VALUE FOUND")


def give(M: matrix, name: str = "M") -> None:
    """
    HE'LL GIVE AN OUTPUT LIKE:
    M = [1, 2]    A - B = [1, 0, 0]
        [3, 4] OR         [0, 1, 0]
        [5, 6]            [0, 0, 1]

    HE GIVES, SHE TAKES... :smirk-face-emoji
    OH BOY I REALLY NEED SOME GRASS TO TOUCH...
    """
    if not vCHECK(M):
        print(f"{RED}E:{RST} INVALID MATRIX")
        return
    print(f"{name} = [{', '.join(map(str, M[0]))}]")
    for row in M[1:]:
        print(f"{' ' * (len(name) + 3)}[{', '.join(map(str, row))}]")
    print()

def twist(M: matrix) -> matrix | str:
    """
    DO THE "TWIST"... I MEAN "T"... OR "TRANSPOSE"...

    [1, 2, 3]                    [1, 4, 7]
    [4, 5, 6] SHE'LL MAKE HER TO [2, 5, 8]
    [7, 8, 9]                    [3, 6, 9]

    ROW BECOMES COLUMN AND VICE-VERSA
    """
    if not vCHECK(M):
        return f"{BRIGHT_RED}E:{RST} INVALID MATRIX"
    return [list(row) for row in zip(*M)]

def eCHECK(A: matrix, B: matrix) -> bool:
    """
    CHECKS IF THE MATRCIES ARE = OR NOT
    THE IT'LL RETURN A BOOLEAN VALUE FOR THE SAME.
    """
    if not (vCHECK(A) and vCHECK(B)):
        return False
    return A == B

# soon i'll start using *args and shit... rn, just bare with it... 
# soon... :embarresed-laughing-emoji

HELP += f"""
MATRIX DOME CMDS:
ADD | PLUS ------------ COMBINES THE GIVEN MATRICES
SUB | MINUS ----------- DEDUCTS THE GIVEN MATRICES
MUL | TIMES ----------- MULTIPLIES THE GIVEN MATRICES
TYPE | SHAPE ---------- TELLS THE SHAPE OF THE MATRIX
SIZE | NRC ----- PRINTS SIZE OF THE MATRIX IN QUESTION
{RST}"""

def main() -> None:
    A = take("A = ")
    B = take("B = ") 

    regedit("HELP", lambda : print(HELP))
    regedit("ADD", lambda *args: give(love(A, B), "A + B"))
    regedit("SUB", lambda *args: give(hate(A, B), "A - B"))
    regedit("MULTI", lambda *args: give(bond(A, B), "A * B"))
    regedit("CROSS", lambda *args: give(bond(A, B), "A * B"))
    regedit("MUL", lambda *args: give(bond(A, B), "A * B"))
    regedit("SHAPE", lambda *args: print(f"SHAPE OF A = {shape(A)}\n"))
    regedit("TYPE", lambda *args: print(f"TYPE OF A = {shape(A)}\n"))
    regedit("TRANSPOSE", lambda *args: give(twist(A), "TRANSPOSE OF M"))
    regedit("T", lambda *args: give(twist(A), "TRANSPOSE OF M"))
    regedit("SIZE", lambda *args: print(f"SIZE OF A = {size(A)}\n"))
    regedit("NRC", lambda *args: print(f"SIZE OF A = {size(A)}\n"))

    while True:
        userInput = input("SO WHAT HAPPENS NOW? ").strip()
        uI_parts = userInput.split()
        cmd = uI_parts[0].upper()
        for key, value in registry.items():
            if cmd == key:
                if value.__code__.co_argcount == 2:
                    give(value(A, B), f"{cmd} = ")
                elif value.__code__.co_argcount == 1:
                    print(value(A))
                else:
                    value()
                break
    
if __name__ == "__main__":
    main()

RAY = """
I REALLY SUCKED AT MATRIX MULTIPLICATION
THEN IT CAME TO ME, WHY SHOULDN'T I MAKE THIS...
NOW I KNOW I SUCK AT THIS TOO... BRUH!!!

YOU KNOW WHAT? FUCK SCHOOL... THEY ARE LEGAL
VAMPIRES (NOT THE GOOD KIND--LIKE ED. CULLEN)
"""