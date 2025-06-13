from shlex import split
import os
import random
import readline # for CLI history and arrows stuff
import sys

# v0.6

"""
THE CHARACTER CASES I'LL BE FOCUSING ON:
- lowercase
- UPPERCASE
- Title Case
- Capitalized case
- sWAP case (from Swap CASE)
- aLtErNaTiNg CaSe
- camelCase (myFav)
- PascalCase
- snake_case
- SCREAMING_SNAKE_CASE (CONSTANT_CASE)
- kebab-case
- Train-Case
- RandoM case (eNtRopY IS VeRY hIGh--pUN IntEndEd... bMTh WoULD lOvE THIS!!!)
- cullenCASE (inventedHER)
- ALTcullenCASE (INVENTEDherTOO)
- dot.case
- path/case
- flatcase
- UPPERFLATCASE
"""

# ANSIcodes (THAT'SaltCULLEN4u)
BRIGHT_GREEN = "\033[92m"
BRIGHT_RED = "\033[91m"
BRIGHT_BLUE = "\033[94m"
RST = "\033[0m"

fileName = os.path.basename(sys.argv[0])

HELP_TEXT = f"""{BRIGHT_GREEN}
BASIC CMDS:
CLEAR | CLS ----------- CLEARS TERMINAL SCREEN!
ABORT | EXIT | QUIT --- KILLS {fileName}!
HELP ------------------ PRINTS THIS!

CASE CONV. CMDS:
LOWER <TXT> -------- lower case
UPPER <TXT> -------- UPPER CASE
TITLE <TXT> -------- Title Case
CAPITALIZE <TXT> --- Capitalized case
SWAP <TXT> --------- Swap Case -> sWAP cASE
ALT <TXT> ---------- aLtErNaTiNg CaSe
CAMEL <TXT> -------- camelCase
PASCAL <TXT> ------- PascalCase
SNAKE <TXT> -------- snake_case
SCREAM <TXT> ------- CONSTANT_SCREAMING_CASE
KEBAB <TXT> -------- kebab-case
TRAIN <TXT> -------- Train-Case
RANDOM <TXT> ------- rAnDOM cAse
CULLEN <TXT> ------- cullenCASE (inventedHER)
ALTCULLEN <TXT> ---- ALTcullenCASE (INVENTEDherTOO)
DOT <TXT> ---------- dot.case
PATH <TXT> --------- path/case
FLAT <TXT> --------- flatcase
UPPERFLAT <TXT> ---- UPPERFLATCASE
{RST}"""

def clear() -> None:
    """
    SHE CLEARS THE TERMINAL SCREEN
    CLEANIN'S IMPORTANT... BRO
    WHO AM I TO SAY? :embarrassed-emoji
    """
    os.system("cls" if os.name == "nt" else "clear")

def T2L(txt:str) -> list:
    """
    TEXT TO LIST

    SHE'S THE WEIRD CHILD OF list() FUNCTION & .split() METHOD
    """
    return txt.casefold().replace("-", " ").replace("_", " ").split() if txt else []

def flatcase(txt:str) -> str:
    """
    SHE'S IMPORTANT (THAT'S WHY SHE IS HER OWN FUNCTION)
    SHE NORMALIZES THE GIVEN TEXT
    """
    return "".join(
        char.casefold() for char in txt if (char.isalnum() and not char.isspace())
        ) if txt else ""

def switch(style: str = "camel", txt: str = "") -> str:
    """
    SHE'S THE MAIN DEAL... SHE'S THE SWITCH!!!
    TURN HER ON OR OFF... YOUR CALL
    """
    s = flatcase(style) # s = style
    W = T2L(txt) # W, w = words, word
    nW = "" # nW = newWord 

    if W and txt and s:
        if "upper" in s:
            nW = txt.upper()
        elif "lower" in s:
            nW = txt.casefold()
        elif "title" in s:
            nW = txt.title()
        elif "capital" in s:
            nW = txt.capitalize()
        elif "swap" in s:
            nW = txt.swapcase()
        elif "alt" in s and not "cullen" in s:
            nW = ""
            up = True
            for c in txt:
                if c.isalpha():
                    nW += c.upper() if up else c.casefold()
                    up = not up
                else:
                    nW += c
        elif "camel" in s:
            nW = W[0].casefold() + "".join(
                w.capitalize() for w in W[1:])
        elif "pascal" in s:
            nW = "".join(
                w.capitalize() for w in W)
        elif "snake" in s or "scream" in s or "constant" in s:
            scream = "scream" in s or "constant" in s
            nW = "_".join(W).upper() if scream else "_".join(W).casefold()
        elif "kebab" in s or "dot" in s or "path" in s:
            sep = "-" if "kebab" in s else "." if "dot" in s else "/"
            nW = sep.join(W)
        elif "train" in s:
            nW = "-".join(w.capitalize() for w in W)
        elif "rand" in s:
            nW = "".join(
                random.choice([c.upper(), c.casefold()]) if c.isalpha() else c for c in txt)
        elif "cullen" in s:
            isAlt = "alt" in s
            nW = "".join(
                w.upper() if (i % 2 == 0) == isAlt else w.casefold() for i, w in enumerate(W))
        elif "flat" in s:
            flat = flatcase(txt)
            nW = flat.upper() if "upper" in s else flat
        else:
            return f"{BRIGHT_RED}E:{RST} CASE '{s.upper()}' NOT FOUND"
        return nW
    return f"{BRIGHT_RED}E:{RST} ERROR OCCURRED"

def main() -> None:
    """
    FOR TESTING PURPOSES
    """
    clear() # clears the home before you step in 
    while True:
        try:
            userInput = input(f"{BRIGHT_BLUE}~/{fileName}$ {RST}").strip()
            if not userInput:
                continue
            parts = split(userInput)
            cmd = parts[0].upper()

            if cmd in {"ABORT", "CLOSE", "EXIT", "QUIT"}:
                exit(f"{BRIGHT_RED}GOODBYE!{RST}")
            elif cmd in {"CLEAR", "CLS"}:
                clear()
            elif cmd in {"HELP"}:
                print(HELP_TEXT)
            else:
                txt = " ".join(parts[1:]) if len(parts) > 1 else ""
                print(switch(cmd, txt))
        except Exception as e:
            print(f"E: {e}")

if __name__ == "__main__":
    main()

"""
SHE MIGHT BE OF NO USE TO YOU BUT I NEEDED HER...
AND THIS WAS THE PERFECT WAY TO SHOWCASE 
cullenCASE & ALTcullenCASE 
"""
