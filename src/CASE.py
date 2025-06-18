from imf.hunt import HELP, limbo, regedit
from imf.rachel import *
import random

__version__ = "v0.8"

def T2L(txt: str) -> list:
    """
    (text: str) -> list

    HE'S THE WEIRD CHILD OF list() FUNCTION & .split() METHOD
    """
    return txt.casefold().replace("-", " ").replace("_", " ").split() if txt else []

def flatcase(txt: str) -> str:
    """
    HE NORMALIZES THE GIVEN TEXT (WHICH IS ALSO THE flatcase)
    """
    return "".join(
        char.casefold() for char in txt if (char.isalnum() and not char.isspace())
        ) if txt else ""

def switch(style: str, txt: str = "") -> str:
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
    return f"{BRIGHT_RED}E:{RST} NOT ENOUGH VALUES SUPPLIED"

HELP += f"""
{BOLD}CASE CONV. CMDS:{RST}{BRIGHT_GREEN}
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
CULLEN <TXT> ------- cullenCASE (inventedHIM)
ALTCULLEN <TXT> ---- ALTcullenCASE (INVENTEDhimTOO)
DOT <TXT> ---------- dot.case
PATH <TXT> --------- path/case
FLAT <TXT> --------- flatcase
UPPERFLAT <TXT> ---- UPPERFLATCASE
{RST}"""

regedit("HELP", lambda : print(HELP))

def main() -> None:
    limbo(plants=lambda cmd, parts: print(switch(cmd, txt = " ".join(parts[1:]) if len(parts) > 1 else "")))

if __name__ == "__main__":
    main()

RAY = """
HAVE YOU EVER USED FLOW LAUNCHER?
EVER ADDED A PLUGIN THAT CHANGES CASES?
THAT'S EXACTLY WHAT HE DOES...

ANYWAY, THIS WAS THE PERFECT WAY TO SHOWCASE 
cullenCASE & ALTcullenCASE...

HE MAYBE CALLED "CASE" BUT HE IS "TARS"
"""