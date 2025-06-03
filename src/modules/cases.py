import random

"""
their are many character casing:
- lowercase
- UPPERCASE
- Title Case
- aLtErNaTiNg CaSe
- camelCase (myFav)
- PascalCase
- snake_case
- SCREAMING_SNAKE_CASE
- kebab-case
- Train-Case
- rAndOm CasE (toTaLlY RanDoM)
- cullenCASE (inventedIT)
- altCULLENcase (INVENTEDitTOO)
- dot.case
"""

def normalize(txt=" "):
    if txt == " ":
        return
    for sep in ["_", "-"]:
        txt = txt.replace(sep, " ")
    words = txt.lower().split()
    if not words:
        return ""
    return words

def camel(txt):
    for sep in ["_", "-"]:
        txt = txt.replace(sep, " ")
    words = txt.lower().split()
    if not words:
        return ""
    return words[0] + "".join(w.capitalize() for w in words[1:])

def pascal(txt):
    words = normalize(txt)
    return "".join(w.capitalize() for w in words) if words else ""

def alt(txt):
    result = []
    toggle = False
    for ch in txt:
        if ch.isalpha():
            result.append(ch.upper() if toggle else ch.lower())
            toggle = not toggle
        else:
            result.append(ch)
    return "".join(result)

def snake(txt):
    words = normalize(txt)
    return "_".join(words) if words else ""

def screamingSnake(txt):
    words = normalize(txt)
    return "_".join(words).upper() if words else ""

def kebab(txt):
    words = normalize(txt)
    return "-".join(words) if words else ""

def train(txt):
    words = normalize(txt)
    return "-".join(w.capitalize() for w in words) if words else ""

def randomCase(txt):
    result = []
    for ch in txt:
        if ch.isalpha():
            result.append(random.choice([True, False]) and ch.upper() or ch.lower())
        else:
            result.append(ch)
    return "".join(result)

def cullen(txt):
    length = len(txt)
    half = length // 2
    return txt[:half].lower() + txt[half:].upper()

def altCullen(txt):
    length = len(txt)
    half = length // 2
    return txt[:half].upper() + txt[half:].lower()

cases = {
    "lower": str.lower,
    "upper": str.upper,
    "title": str.title,
    "alternating": alt,
    "camel": camel,
    "pascal": pascal,
    "snake": snake,
    "screamingsnake": screamingSnake,
    "kebab": kebab,
    "train": train,
    "random": randomCase,
    "cullencase": cullen,
    "altcullencase": altCullen
}

def switch(txt, case):
    if not txt or not case:
        return "NOT ENOUGH VALUES WERE SUPPLIED!"
    key = case.lower()
    if key not in cases:
        return f"CASE '{case}' NOT FOUND!"
    transformer = cases[key]
    return transformer(txt)

def main():
    txt = input("~/cases.py$ ").strip()
    for case in cases:
        print(f"{case}: {switch(txt, case)}")

if __name__ == "__main__":
    main()