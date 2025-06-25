from IMF.hunt import HELP, limbo, bob, turtle
from IMF.rachel import *
import functools
import random

__version__ = "v0.3.9"

def T2L(txt: str) -> list:
    """
    (text: str) -> list

    He's the weird child of list() function and .split() method.
    """
    return txt.casefold().replace("-", " ").replace("_", " ").split() if txt else []

def flatcase(txt: str) -> str:
    """
    He normalizes the given text, converts them to flatcase.
    """
    return "".join(
        char.casefold() for char in txt if (char.isalnum() and not char.isspace())
        ) if txt else ""

def wSep(W: list, sep: str) -> str:
    """
    withSeperators(WordList, seperator)
    """
    return sep.join(W)

@functools.lru_cache
def switch(style: str, txt: str = "") -> str:
    """
    Everything resides here!
    """
    s = flatcase(style) # s = style
    W = T2L(txt) # W, w = words, word
    nW = "" # nW = newWord 

    if W and txt and s:
        if "up" in s and "f" not in s:
            nW = txt.upper()
        elif "low" in s:
            nW = txt.casefold()
        elif "title" in s or s == "t":
            nW = txt.title()
        elif "cap" in s:
            nW = txt.capitalize()
        elif "swap" in s or s == "swp":
            nW = txt.swapcase()
        elif ("alt" in s and not "c" in s) or s == "a":
            up = True
            for c in txt:
                if c.isalpha():
                    nW += c.upper() if up else c.casefold()
                    up = not up
                else:
                    nW += c
        elif "cam" in s or s == "c":
            nW = W[0].casefold() + "".join(
                w.capitalize() for w in W[1:])
        elif "pas" in s or s == "p":
            nW = "".join(
                w.capitalize() for w in W)
        elif any(c in s for c in {"snake", "scream", "constant", "s", "ss", "con"}):
            scream = "ss" in s or "con" in s or "scream" in s
            nW = "_".join(W).upper() if scream else "_".join(W).casefold()
        elif any(c in s for c in {"ke", "par"}):
            nW = wSep(W, "-")
        elif "dot" in s or s == "d":
            nW = wSep(W, ".")
        elif "path" in s or s == "pth":
            nW = wSep(W, "/")
        elif "tr" in s or "head" in s:
            nW = "-".join(w.capitalize() for w in W)
        elif "rand" in s or s == "r":
            nW = "".join(
                random.choice([c.upper(), c.casefold()]) if c.isalpha() else c for c in txt)
        elif "cul" in s or any(c in s for c in {"ac", "cu", "altc", "alternatec", "alternatingc"}):
            isAlt = "a" in s
            nW = "".join(
                w.upper() if (i % 2 == 0) == isAlt else w.casefold() for i, w in enumerate(W))
        elif any(c in s for c in {"f", "upf", "upperf", "uf"}):
            flat = flatcase(txt)
            nW = flat.upper() if "up" in s else flat
        else:
            return f"{BRIGHT_RED}err:{RST} case_'{s.casefold()}'_notFound"
        return nW
    return f"{BRIGHT_RED}err:{RST} notEnoughValuesSupplied"

HELP += f"""{BOLD}CASE conv. cmds:{RST}{BRIGHT_GREEN}
low [txt] --- lower case
up [txt] ---- UPPER CASE
t [txt] ----- Title Case
cap [txt] --- Capitalized case
swp [txt] --- Swap Case -> sWAP cASE
a [txt] ----- aLtErNaTiNg CaSe
c [txt] ----- camelCase
p [txt] ----- PascalCase
s [txt] ----- snake_case
ss [txt] ---- CONSTANT_SCREAMING_CASE
k [txt] ----- kebab-case
tr [txt] ---- Train-Case
r [txt] ----- rAnDOM cAse
cul [txt] --- cullenCASE (inventedHIM)
ac [txt] ---- ALTcullenCASE (INVENTEDhimTOO)
d [txt] ----- dot.case
pth [txt] --- path/case
f [txt] ----- flatcase
uf [txt] ---- UPPERFLATCASE{RST}

{BOLD}Notes:{RST} {BRIGHT_GREEN}
Yes, you can use similar commands.
This is just the tip of the iceberg.
{RST}"""

def main() -> None:
    limbo(lambda cmd, parts: turtle(switch(cmd, txt = " ".join(parts[1:]) if len(parts) > 1 else "")), HLP= HELP, v = __version__)

if __name__ == "__main__":
    main()

RAY = """
Ever used Flow Launcher?
Ever added that plugin that does what this does? 

Anyways, I made this to showcase cullenCASE & ALTcullenCASE

He maybe called CASE but he's more of TARS!
"""