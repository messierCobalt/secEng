from IMF.shell import *
import random

# v0.7.5

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
- cullenCASE (inventedHIM)
- ALTcullenCASE (INVENTEDhimTOO)
- dot.case
- path/case
- flatcase
- UPPERFLATCASE
"""

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

def T2L(txt: str) -> list:
    """
    TEXT BECOMES LIST

    HE'S THE WEIRD CHILD OF list() FUNCTION & .split() METHOD
    """
    return txt.casefold().replace("-", " ").replace("_", " ").split() if txt else []

def flatcase(txt: str) -> str:
    """
    HE'S IMPORTANT (THAT'S WHY HE IS HIS OWN FUNCTION)
    HE NORMALIZES THE GIVEN TEXT
    """
    return "".join(
        char.casefold() for char in txt if (char.isalnum() and not char.isspace())
        ) if txt else ""

def switch(style: str = "camel", txt: str = "") -> str:
    """
    HE'S THE MAIN DEAL...
    HE'S THE SWITCH!!!
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
    return f"{BRIGHT_RED}E:{RST} NOT ENOUGH VALUES SUPPLIED"

regedit("HELP", lambda : print(HELP))

def main() -> None:
    """
    LOOK ON DOWN FROM THE BRIDGE
    ...
    GOODBYE!
    """
    limbo(plants=lambda cmd, parts: print(switch(cmd, txt = " ".join(parts[1:]) if len(parts) > 1 else "")))

if __name__ == "__main__":
    main()

"""
HE MIGHT BE OF NO USE TO YOU BUT I NEEDED HIM...
AND THIS WAS THE PERFECT WAY TO SHOWCASE 
cullenCASE & ALTcullenCASE...

HE MAYBE NAMED "CASE" BUT HE IS MORE OF "TARS"
"""